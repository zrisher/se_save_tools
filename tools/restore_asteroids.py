"""
tools/restore_asteroids.py

This tool
  deletes all asteroids in World not near a player/grid
  imports all asteroids from Backup World besides those that remain in World
"""


def run(world, backup_world, logger):
    logger.info('running restore_asteroids {0}'.format(True))

    sector = world.tree('sector').getroot()

    asteroids = sector.findall("SectorObjects/MyObjectBuilder_EntityBase")

    logger.info('---asteroids----')

    logger.info('asteroids {0}'.format(asteroids))
    for child in asteroids:
        logger.info('child {0}'.format(child))

    logger.info('-----------------\n')




