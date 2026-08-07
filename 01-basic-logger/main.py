import logging
import firstChild
import secondChild

console_handler: logging.StreamHandler = logging.StreamHandler()
file_handler: logging.FileHandler = logging.FileHandler('basics.log')

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[console_handler, file_handler]
)

logger: logging.Logger = logging.getLogger(__name__)

def log_messages():
    logger.debug('This is a simple DEBUG log.')
    logger.info('This is a simple INFO log.')
    logger.warning('This is a simple WARNING log.')
    logger.error('This is a simple ERROR log.')
    logger.critical('This is a simple CRITICAL log.')

if __name__ == '__main__':
    log_messages()
    firstChild.first_logs()
    secondChild.second_logs()
