"""
save/entities/floating
"""
from .base import Base


class FloatingObject(Base):
    def __init__(self, tree):
        super().__init__(tree)
        self.type = 'floating_object'



"""
def GetFloatingItemName(objnode):
		return "%s : %s"%(
		FindAttrib(objnode.find('Item').find('PhysicalContent')).
			replace("MyObjectBuilder_", ""),
		objnode.find('Item').find('PhysicalContent')
			.find('SubtypeName').text)
			#type : name e.g. Ore : Iron
"""