"""
save/entities/grid
"""
from .base import Base


class Grid(Base):
    def __init__(self, tree):
        super().__init__(tree)
        self.type = 'grid'


"""
    Check for nearby grids attached to you and store
    has_grid_receptor_a
    has_grid_receptor_b
    attached_grids = {}

            if entity.find("CubeBlocks"):
                entity_id = entity.e_id
                for block in entity.blocks:
                    if block.find("EntityId"):
                        blockId = block.find("EntityId").text
                        attrib = FindAttrib(block)
                        #A Type joins
                        if attrib == "MyObjectBuilder_MotorAdvancedStator" or attrib == "MyObjectBuilder_MotorStator":
                            if block.find("RotorEntityId"): #If it's missing
                                if block.find("RotorEntityId").text != "0": #If it's 0, no rotor joined
                                    joinEndsA.append(JoinEnd(entity, blockId, entityId, block.find("RotorEntityId").text))

                        if attrib == "MyObjectBuilder_ExtendedPistonBase":
                            joinEndsA.append(JoinEnd(entity, blockId, entityId, block.find("TopBlockId").text))

                        #B type joins, just record them. They'll be matched up later
                        if attrib == "MyObjectBuilder_MotorAdvancedRotor" or attrib == "MyObjectBuilder_PistonTop" or attrib == "MyObjectBuilder_MotorRotor":
                            joinEndsB.append(JoinEnd(entity, blockId, entityId, None))

    #Table assembled, lets match them
    joins = []
    for JoinA in joinEndsA:
        match = None
        for j in joinEndsB:
            if j.BlockId == JoinA.OtherEnd:
                match = j
                break
        #match = next(j for j in joinEndsB if j.EntityId == JoinA.OtherEnd)

        if match != None:
            #Match found
            joins.append(JoinEntry(JoinA.EntityId, JoinA.ParentNode, match.EntityId, match.ParentNode))

    #Return the join table
    return joins
"""