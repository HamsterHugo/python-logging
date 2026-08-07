import logging

logger: logging.Logger = logging.getLogger(__name__)

def second_logs():
    logger.debug('This is a simple DEBUG log from "second.py".')
    logger.info('This is a simple INFO log from "second.py".')
    logger.warning('This is a simple WARNING log from "second.py".')
    logger.error('This is a simple ERROR log from "second.py".')
    logger.critical('This is a simple CRITICAL log from "second.py".')

if __name__ == '__main__':
    second_logs()