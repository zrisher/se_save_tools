"""
utility/files.py
"""

import os
import shutil
import distutils.dir_util
# import glob


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def delete_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def copy_dir(src, dst):
    distutils.dir_util.copy_tree(src, dst)


def create_file(path):
    with open(path, 'w+') as file:
        file.write('')


def delete_file(path):
    os.remove(path)


def copy_file(src, dst):
    shutil.copy(src, dst)