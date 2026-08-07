import logging

logger: logging.Logger = logging.getLogger(__name__)

def first_logs():
    logger.debug('This is a simple DEBUG log from "first.py".')
    logger.info('This is a simple INFO log from "first.py".')
    logger.warning('This is a simple WARNING log from "first.py".')
    logger.error('This is a simple ERROR log from "first.py".')
    logger.critical('This is a simple CRITICAL log from "first.py".')

if __name__ == '__main__':
    first_logs()