"""
test/tools/restore_asteroids.py
"""

import os
import datetime
import pytest

DEFAULT_LOG_DIR = 'logs'

DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(DIR, '..', 'data')
TMP_DIR = os.path.join(DIR, '..', 'tmp')
LOG_DIR = os.path.join(DIR, '..', '..', DEFAULT_LOG_DIR)

DEFAULT_LOG_DIR = 'logs'
RUN_TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


from ...utility.files import create_dir, delete_dir, copy_dir
from ...utility.string import random_alphanumeric
from ...utility.logging import logger as simple_logger

from ...save.world import World
from ...tools import restore_asteroids


def test_restore_asteroids():
    """
    Describe restore_asteroids
    """

    #
    # before all
    #

    # init logger
    log_file_name = "SEWT_test_{0}.txt".format(RUN_TIMESTAMP)
    log_path = os.path.join(LOG_DIR, log_file_name)
    logger = simple_logger('run', log_path, level_str='debug')
    logger.debug('initialized logger')

    # create copy of test world to work with
    delete_dir(TMP_DIR)
    create_dir(TMP_DIR)
    world_path = os.path.join(TMP_DIR, random_alphanumeric(8))
    test_data_world_path = os.path.join(DATA_DIR, 'test_world')
    copy_dir(test_data_world_path, world_path)
    test_world = World(world_path, logger=logger)

    #
    # descriptions
    #
    restore_asteroids.run(test_world, test_world, logger)

    #
    # after all
    #

    # delete test world copy
    #delete_dir(random_world_path)