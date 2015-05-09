"""
save/world.py
"""

import glob  # file ops
import os  # file ops
import xml.etree.ElementTree as Et  # save file ops
import logging

CHECKPOINT_FILE_NAME = 'Sandbox.sbc'
SECTOR_FILE_NAME = 'SANDBOX_0_0_0_.sbs'
LAST_LOADED_FILE_NAME = 'LastLoaded.sbl'
XML_NAMESPACES = {
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

for prefix, namespace in XML_NAMESPACES.items():
    Et.register_namespace(prefix, namespace)


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
        self.logger.info('Loading world from {0}'.format(world_dir))
        self.logger.info('trees init as {0}'.format(self.__trees__))
        self.load_trees()
        self.logger.info('Finished initializing world'.format(world_dir))


    def load_trees(self):
        for key in self.__trees__:
            self.logger.info('load tree {0}'.format(key))
            path = self.__world_file_paths__[key]

            if os.path.exists(path):
                self.__trees__[key] = Et.parse(path)
                self.logger.info('tree {0}'.format(self.__trees__[key].getroot()))
            else:
                if not key == 'last_loaded':
                    raise IOError('World file missing at {0}'.format(path))

    def tree(self, key):
        return self.__trees__[key]

    def trees(self):
        return self.__trees__

    def asteroids(self):
        return []
