"""
save/coords
"""

import math

def distance_between(position, other_position):
    try:
        distance = math.sqrt(
          math.pow(position[0] - other_position[0], 2) +
          math.pow(position[1] - other_position[1], 2) +
          math.pow(position[2] - other_position[2], 2)
        )
    except:
        distance = -1.0

    return distance