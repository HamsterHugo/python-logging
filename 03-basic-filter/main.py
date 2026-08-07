import logging
from firstChild import first_logs
from secondChild import second_logs

console_handler: logging.StreamHandler = logging.StreamHandler()
file_handler: logging.FileHandler = logging.FileHandler('basic-filter.log')

first_filter: logging.Filter = logging.Filter('firstChild')
second_filter: logging.Filter = logging.Filter('secondChild')

file_handler.addFilter(first_filter)
console_handler.addFilter(second_filter)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    datefmt="[%d.%m.%Y %X]",
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