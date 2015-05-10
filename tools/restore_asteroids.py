"""
tools/restore_asteroids.py

This tool
  deletes all asteroids in World not near a player/grid
  imports all asteroids from Backup World besides those that remain in World
"""


def run(world, backup_world, logger):
    logger.info('running restore_asteroids')

    asteroids = world.asteroids()
    logger.debug('asteroids {0}'.format(asteroids))
    for asteroid_id, asteroid in asteroids.items():
        logger.debug('looping asteroid {0}'.format(asteroid))
        logger.debug('grids within 2km {0}'.format(world.grids_within(2000, asteroid)))
        if not world.grids_within(2000, asteroid):
            logger.debug('removing asteroid')
            asteroid.delete()



