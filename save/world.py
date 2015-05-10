"""
save/world.py
"""

import glob  # file ops
import os  # file ops
import xml.etree.ElementTree as Et  # save file ops
import logging

from .entities import load_entity_from_tree
from .entities.asteroid import Asteroid
from .entities.character import Character
from .entities.floating import FloatingObject
from .entities.grid import Grid
from .entities.meteor import Meteor

ALL_ENTITY_TYPES = ['asteroid', 'character', 'floating_object',
                    'grid', 'meteor']

CHECKPOINT_FILE_NAME = 'Sandbox.sbc'
SECTOR_FILE_NAME = 'SANDBOX_0_0_0_.sbs'
LAST_LOADED_FILE_NAME = 'LastLoaded.sbl'

XML_NAMESPACES = {
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

for prefix, namespace in XML_NAMESPACES.items():
    Et.register_namespace(prefix, namespace)

from ..utility.coordinate_math import distance_between


class World:
    """
    Interface for all of the data in a save folder
    Deals with file saving/backup, xml, etc
    """
    def __init__(self, world_dir, backup_dir=None, logger=None):
        self.logger = logger or logging
        self.__world_dir__ = world_dir
        self.__backup_dir__ = backup_dir
        self.__world_file_paths__ = {
            'checkpoint': os.path.join(world_dir, CHECKPOINT_FILE_NAME),
            'sector': os.path.join(world_dir, SECTOR_FILE_NAME),
            'asteroids': glob.glob(os.path.join(world_dir, '*asteroid*.vx2')),
            'last_loaded': os.path.join(world_dir, LAST_LOADED_FILE_NAME),
        }
        self.__trees__ = {
            'checkpoint': None,
            'sector': None,
            'last_loaded': None,
        }
        self.__entities__ = {
            'asteroid': {},
            'character': {},
            'floating_object': {},
            'grid': {},
            'meteor': {}
        }
        self.logger.info('Loading world from {0}'.format(world_dir))
        self.logger.debug('trees init as {0}'.format(self.__trees__))
        self.load_trees()
        self.load_entities()
        self.log_state()
        self.logger.info('Finished initializing world'.format(world_dir))

    #
    # XML Data Trees
    #
    def load_trees(self):
        for key in self.__trees__:
            self.logger.debug('load tree {0}'.format(key))
            path = self.__world_file_paths__[key]

            if os.path.exists(path):
                self.__trees__[key] = Et.parse(path)
                self.logger.debug('tree {0}'.format(self.__trees__[key].getroot()))
            else:
                if not key == 'last_loaded':
                    raise IOError('World file missing at {0}'.format(path))

    #def tree(self, key):
    #    return self.__trees__[key]

    #def trees(self):
    #    return self.__trees__

    #
    # In-Game Entities
    #
    def load_entities(self):
        self.logger.debug("Indexing Entities")

        sector_tree = self.__trees__['sector'].getroot()
        entity_trees = sector_tree.findall("SectorObjects/MyObjectBuilder_EntityBase")
        if not entity_trees:
            raise BlockingIOError('Unable to load world entity_trees')

        for entity_tree in entity_trees:
            entity = load_entity_from_tree(entity_tree, self.logger)
            self.__entities__[entity.type][entity.e_id] = entity

    def asteroids(self):
        return self.__entities__['asteroid']

    def entities_within(self, radius, entity, entity_types=ALL_ENTITY_TYPES):
        results = []
        position = entity.position
        for type in entity_types:
            for other_e_id, other_entity in self.__entities__[type].items():
                if other_entity != entity:
                    distance = distance_between(position, other_entity.position)
                    if distance < radius:
                        results.append(other_entity)

        return results

    def grids_within(self, radius, entity):
        return self.entities_within(radius, entity, entity_types=['grid'])


    def log_state(self):
        self.logger.info(' ----- Current world state: ----- ')
        self.logger.info(' --- {0} Asteroids, {1} Characters, {2} Floating Objects, {3} Grids, {4} Meteors --- '.format(
            len(self.__entities__['asteroid'].keys()),
            len(self.__entities__['character'].keys()),
            len(self.__entities__['floating_object'].keys()),
            len(self.__entities__['grid'].keys()),
            len(self.__entities__['meteor'].keys()),
        ))
        self.logger.info(' Asteroids: ')
        for stored_id, asteroid in self.asteroids().items():
            self.logger.info(stored_id)
            self.logger.info(asteroid.e_id)
            self.logger.info(asteroid.name())
            self.logger.info(asteroid.position())
            self.logger.info('')
        self.logger.info(' -------------------------------- ')

