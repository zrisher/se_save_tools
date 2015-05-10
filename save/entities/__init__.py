"""
save/entities
"""

XML_NAMESPACES = {
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

ENTITY_TREE_TYPE_ATTR = '{' + XML_NAMESPACES['xsi'] + '}type'

from .asteroid import Asteroid
from .character import Character
from .floating import FloatingObject
from .grid import Grid
from .meteor import Meteor

ENTITY_TYPES = {
    'asteroid': 'MyObjectBuilder_VoxelMap',
    'character': 'MyObjectBuilder_Character',
    'floating_object': 'MyObjectBuilder_FloatingObject',
    'grid': 'MyObjectBuilder_CubeGrid',
    'meteor': 'MyObjectBuilder_Meteor'
}


def load_entity_from_tree(tree, logger):
    logger.debug("loading entity from tree {0}".format(tree))
    tree_xsi = tree.attrib[ENTITY_TREE_TYPE_ATTR]

    for name, xsi in ENTITY_TYPES.items():
        if xsi == tree_xsi:
            if name == 'asteroid':
                return Asteroid(tree, logger=logger)
            if name == 'character':
                return Character(tree)
            if name == 'floating_object':
                return FloatingObject(tree)
            if name == 'grid':
                return Grid(tree)
            if name == 'meteor':
                return Meteor(tree)

    return None
