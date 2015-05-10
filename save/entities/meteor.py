"""
save/entities/meteor
"""

from .base import Base


class Meteor(Base):
    def __init__(self, tree):
        super().__init__(tree)
        self.type = 'meteor'