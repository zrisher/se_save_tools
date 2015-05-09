"""
SEWT - Space Engineers WorldFile Tools

Does awesome stuff to world files
"""


import configparser #For config reading and writing
import xml.etree.ElementTree as ET #Used to read the SE save files
import argparse #Used for CLI arguments
import os #For file system checks & snapshot file working
import shutil #For copying files to backups
import datetime #For timestamps
import sys #for propper sys.exit()
import re #Regex, for determining generic names
import math #for distance calculations
import glob #for asteroid backups

#import tools.place_asteroids
import utility.logging
from save.world import World


INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LOG_DIR = 'logs'
RUN_TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def parse_cl_args():
    """
    Parse the command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("tool", help="which tool to run")
    parser.add_argument("-l", "--log_dir",
                        help="the directory path for logs")
    parser.add_argument('-w', '--world_dir', required=True,
                        help="the directory path for world files")
    parser.add_argument('-b', '--backup_dir',
                        help="the directory path to store and load backups")
    return parser.parse_args()


def main():
    """
    Run the tools
    """
    args = parse_cl_args()

    # init logger
    log_dir = args.log_dir or os.path.join(INSTALL_DIR, DEFAULT_LOG_DIR)
    log_file_name = "SEWT_{0}.txt".format(RUN_TIMESTAMP)
    log_path = os.path.join(log_dir, log_file_name)
    logger = utility.logging.logger('run', log_path)
    logger.info('initialized logger')

    # load files
    world_dir = args.world_dir
    backup_dir = args.backup_dir or os.path.join(world_dir, 'backup')
    logger.info('loading world')
    loaded_world = World(world_dir, backup_dir=backup_dir, logger=logger)
    logger.info('loaded world')

    # run tool
    tool = args.tool
    if tool == "distribute:asteroids":
        print('distribute:asteroids') #tools.place_asteroids.run(loaded_world, logger=logger)
    elif tool == 'restore:asteroids':
        print('restore:asteroids') #tools.restore_asteroids(loaded_world, backup_dir)
    elif tool == 'restore:grids':
        print('restore:grids') #tools.restore_grids(loaded_world, backup_dir)


# run the main method when this file is run
if __name__ == "__main__":
    main()

