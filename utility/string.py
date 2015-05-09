"""
utility/string.py
"""

import random
import datetime
import time

def random_alphanumeric(length):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(length))


def timestamp():
    return datetime.datetime.fromtimestamp(time.time()).\
        strftime('%Y-%m-%d-%H-%M-%S')