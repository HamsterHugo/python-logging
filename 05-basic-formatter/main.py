import logging
from firstChild import first_logs
from secondChild import second_logs

console_handler = logging.StreamHandler()
file_handler: logging.FileHandler = logging.FileHandler("basic-formatter.log")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.DEBUG,
    format=logging.BASIC_FORMAT,
    handlers=[console_handler, file_handler]
)

logger = logging.getLogger(__name__)

def log_messages():
    logger.debug('This is a simple DEBUG log.')
    logger.info('This is a simple INFO log.')
    logger.warning('This is a simple WARNING log.')
    logger.error('This is a simple ERROR log.')
    logger.critical('This is a simple CRITICAL log.')

if __name__ == '__main__':
    log_messages()
    first_logs()
    second_logs()