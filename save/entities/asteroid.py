"""
save/entities/asteroid
"""

FILE_EXTENSION = '.vx2'
VOXEL_BACKUP_FOLDER = 'voxel backups'
REMOVAL_GRID_CAUTION_RANGE = 2000

from .base import Base


class Asteroid(Base):
    def __init__(self, tree, logger=None):
        super().__init__(tree, logger)
        self.type = 'asteroid'

    def name(self):
        return self.tree.find('StorageName').text




# l.info("===Processing asteroid / voxel map: %s / %s==="%(object.find("EntityId").text, voxelname))

"""
def VoxelHasBackup(voxelname):
    voxelname = voxelname + FILE_EXTENSION
    backupdir = args.save_path + cget(config, "voxel_backup_folder")

if (os.path.exists(backupdir)):
    l.debug("Backup exists for voxel")
    lolwut = os.listdir(backupdir)
    r = (voxelname in os.listdir(backupdir))
    return r #Return True or False
else:
    l.debug("No backup exists for voxel")
    return False





##############################################
# Restore a backed up asteroid
##############################################
def RestoreVoxel(voxelname):
voxelname = voxelname + "." + cget(config, "asteroid_file_suffix")
l.debug("Restoring voxel from backup: " + voxelname)
backupdir = args.save_path + cget(config, "voxel_backup_folder")

if os.path.exists(backupdir) == False:
    l.error("Attempted to restore voxel from backup, backup dir doesn't exist!")
    return False

if os.path.isfile(backupdir + "/" + voxelname):
    #Backup exists
    if args.whatif == True:
        l.info("Whatif enabled, skipped restoring voxel")
    else:
        shutil.copyfile(backupdir + "/" + voxelname, args.save_path + voxelname)
else:
    l.error("Attempted to restore a voxel from backup, failed to find backup file!")
    return False



#############################################
# Function to remove an asteroid from the save, as well
#   as removing the asteroid voxel file
#############################################
def RemoveAsteroid(object, sectorobjects, savepath, whatif):
roidname = object.find("StorageName").text
l.info("Removing asteroid: " + roidname)

fname = "%s%s.%s"%(savepath, roidname, cget(config, "asteroid_file_suffix"))
l.debug("Asteroid file: " + fname)

if whatif == True:
    l.info("WhatIf used, not actually removing asteroid file")
else:
    if os.path.isfile(fname):
        os.remove(fname)
    else:
        l.warning("Warning: unable to locate asteroid file: " + roidname)


sectorobjects.remove(object)

"""