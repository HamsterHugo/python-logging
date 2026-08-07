import logging
from firstChild import first_logs
from secondChild import second_logs

from rich.logging import RichHandler

console_handler: RichHandler = RichHandler()
file_handler: logging.FileHandler = logging.FileHandler('richLogging.log')

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
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
    first_logs()
    second_logs()