######################################
# Function to get clust of objects,
#   if they're joined by pistons, rotors, etc
# Updated to use the indexed sector objects dictionary
######################################
def GetObjectCluster(objectnode, joins):
    i = 0
    clustervar = [objectnode]

    #Keep adding to the clustervar
    #while i < len(clustervar):
    #    for object in clustervar:
    #        for block in list(object.find("CubeBlocks")):
    #            result = GetOtherJoinEnd(block, sectorobjectsindexed)
    #            if result != None:
    #                if result not in clustervar:    #Only add if the clustervar doesn't contain it already
    #                    clustervar.append(result)   #Tricky multi joins!
    #    i = i + 1 #Next in cluster
    #End clustervar loop

    toProcess = [objectnode]
    haveSeen = [objectnode.find("EntityId").text]
    while i < len(clustervar):
        object = clustervar[i]
        entityId = object.find("EntityId").text
        for j in joins:
            if j.EntityAId == entityId and j.EntityBNode not in clustervar:
                clustervar.append(j.EntityBNode)
            if j.EntityBId == entityId and j.EntityANode not in clustervar:
                clustervar.append(j.EntityANode)

        i = i + 1

    return clustervar


#####################################
# Function to get the name(s) of the entity cluster
# Custom names are placed at the front
#####################################
def ObjectClusterName(objectcluster):
    #Prep the name object
    nobject = ClusterName()
    namingBlocks = cget(config, "type_custom_names").split(";")
    blockNamesToIgnore = cget(config, "block_names_to_ignore").split(";")

    for object in objectcluster:
        nobject.objectNames.append((object.find("EntityId").text , object.find("DisplayName").text)) #Save as tuple
        l.debug("ID: '%s'"%object.find("EntityId").text)
        l.debug("Name: " + object.find("DisplayName").text)

        for block in object.find("CubeBlocks"):
            attrib = FindAttrib(block)
            if attrib in namingBlocks:
                #Is a block that we can use for name finding
                if block.find("CustomName") != None: #Custom name property exists
                    if block.find("CustomName").text != "": #Ignore it if it's blank
                        nobject.AddBlockName(block.find("CustomName").text)


        #End of block loop
    #End of object loop

    #Calculate the primary name
    nobject.CalcPrimaryName()

    return nobject

class ClusterName:
    objectNames = [] #Tuples of (Object ID, Object Name) of the object cluster
    blockNames = [] #List of custom block names like beacon and antenna
    primaryName = "" #If only a single name can be used, use this one. Primarily used with export save names

    def __init__(self):
        self.objectNames = []
        self.blockNames = []
        self.primaryName = ""

    def __str__(self):
        names = []
        for key, value in self.objectNames:
            names.append("'%s' (%s)"%(value, key))

        names.extend(self.blockNames)

        return " / ".join(names)

    def AddBlockName(self, blockName):
        if blockName == None:
            return
        if str.strip(blockName) == "":
            return

        l.debug("Testing block name: " + blockName)
        regexString = r"^(%s)(\W(\d)+)*$"%("|".join(cget(config, "block_names_to_ignore").split(";")))
        p = re.compile(regexString, re.IGNORECASE) #Regex used to chekc if it's generic or not
        #e.g. Antenna 1234

        if p.match(blockName) == None and blockName != "":
        #if p.match(blockName) == None:
            self.blockNames.append(blockName)


    def CalcPrimaryName(self):
        if len(self.blockNames) > 0:
            self.primaryName = self.blockNames[0]
        else:
            p = re.compile(r"^(Platform|Large Ship|Small Ship) (\d)+$", re.IGNORECASE) #Regex used to determine if the object name is unique or not
            for k, v in self.objectNames: #Just loop the names, not the ID's
                if p.match(v) == None: #No match, must be custom
                    self.primaryName = v
                    break #Already got one, don't go any further
        #End if

        if self.primaryName == "": #If STILL no primary name
            self.primaryName = self.objectNames[0][1] #Just use the first tuple

        l.debug("Primary name: " + self.primaryName)


#################################
# Function to get the playerID's of
# players that own blocks in this cluster
#################################

def GetClusterOwners(objectcluster, currentownerlist):
    for object in objectcluster:
        for block in object.find("CubeBlocks"):
            if block.find("Owner") != None:
                blockowner = block.find("Owner").text
                if blockowner not in currentownerlist:
                    currentownerlist.append(blockowner)

    return currentownerlist


############################################
# Function to stop object cluster movement
############################################
def StopMovement(objectcluster):
    l.info("Stopping movement")
    for object in objectcluster:
        if object.find('LinearVelocity') != None:
            object.find('LinearVelocity').attrib["x"] = "0"
            object.find('LinearVelocity').attrib["z"] = "0"
            object.find('LinearVelocity').attrib["y"] = "0"
        else:
            l.error("Error: Unable to find LinearVelocity node!")

        if object.find('AngularVelocity') != None:
            object.find('AngularVelocity').attrib["x"] = "0"
            object.find('AngularVelocity').attrib["y"] = "0"
            object.find('AngularVelocity').attrib["z"] = "0"
        else:
            l.error("Error: Unable to find AngularVelocity node!")

class JoinEnd:
    EntityId = "" #EntityId of the parent entity
    BlockId = "" #EntityId of this block
    ParentNode = None #SectorObject node
    OtherEnd = "" #EntityId of the other block (if it's a JoinEndA

    def __init__(self, ParentNode, BlockId, EntityId, OtherEnd):
        self.ParentNode = ParentNode
        self.BlockId = BlockId
        self.EntityId = EntityId
        self.OtherEnd = OtherEnd

class JoinEntry:
    EntityAId = ""
    EntityANode = None
    EntityBId = ""
    EntityBNode = None

    def __init__(self, EntityAId, EntityANode, EntityBId, EntityBNode):
        self.EntityAId = EntityAId
        self.EntityANode = EntityANode
        self.EntityBId = EntityBId
        self.EntityBNode = EntityBNode