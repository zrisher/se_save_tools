"""
tools/distribute_asteroids.py

This tool
  generates asteroid locations according to a strategy
  finds all the asteroids in the world that are far away from grids
  places those asteroids into a pool and fills it to the num required
  randomly picks asteroids from the pool and places at the new locations

"""

STRATEGIES = {
    'gardens_of_sajuuk': {
        'description': '''
big asteroid cloud from 0 to 50km
3 5km CP's at 100km at 0deg
6 rings at 150km at 90deg
~30 randomly placed asteroids between 200-500km -
maybe a couple together and one along a 500km border or even in a corner
http://media.moddb.com/images/downloads/1/11/10830/ARmed2.1.JPG
        ''',
        'shapes': [
            {
                'type': 'sphere',
                'asteroids': 50,
                'center': [0, 0, 0],
                'inner_r': 0,
                'outer_r': 50,
            },
            {
                'type': 'clustered_ring',
                'asteroids': 60,
                'clusters': 6,
                'coverage': .5,
                'center': [0, 0, 0],
                'inner_r': 144,
                'outer_r': 146,
                'start_degrees': 90,
            },
            {
                'type': 'sphere',
                'asteroids': 27,
                'center': [0, 0, 0],
                'inner_r': 200,
                'outer_r': 500,
            },
            {
                'type': 'sphere',
                'asteroids': 2,
                'cluster_size': 2,
                'center': [0, 0, 0],
                'inner_r': 200,
                'outer_r': 500,
            },
            {
                'type': 'corners',
                'asteroids': 1,
                'distance': 1
            },
        ]
    }
}


def run(world, logger=None, strategy='gardens_of_sajuuk'):
    return True


def asteroid_group(num, center, inner_r, outer_r, space=500):
    """
     randomly places NUM around CENTER at least SPACE apart
    """
    return [[]]








