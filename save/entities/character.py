"""
save/entities/character
"""

from .base import Base


class Character(Base):
    def __init__(self, tree):
        super().__init__(tree)
        self.type = 'character'
