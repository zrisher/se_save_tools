"""
save/entities/base
"""


class Base:
    def __init__(self, tree, logger=None):
        self.tree = tree
        self.logger = logger
        self.e_id = self.tree.find("EntityId").text

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.e_id == other.e_id

    def __ne__(self, other):
        return not self.__eq__(other)

    def delete(self):
        print('remove not implemented')

    def position(self):
        self.logger.debug('finding position for {0}'.format(self))
        self.logger.debug('tree is {0}'.format(self.tree))
        for child in self.tree:
            self.logger.debug('tree child is {0}'.format(child))
        self.logger.debug('position 1 node is '.format(self.tree.findall('*')))
        self.tree.find('PositionAndOrientation/Position')
        node = self.tree.find('PositionAndOrientation/Position')
        self.logger.debug('position_node is '.format(node))
        if node:
            position = [node.attrib["x"], node.attrib["y"], node.attrib["z"]]
            self.logger.debug('position is {0}'.format(position))
            return position
        else:
            self.logger.error("Error: Can't find Position node!")