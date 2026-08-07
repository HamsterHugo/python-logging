import logging
from firstChild import first_logs
from secondChild import second_logs

class StatusFormatter(logging.Formatter):
    def format(self, record):
        original_levelname = record.levelname
        status = getattr(record, "status", None)
        if status: record.levelname = status.upper()
        formatted_message = super().format(record)
        record.levelname = original_levelname

        return formatted_message

console_handler: logging.StreamHandler = logging.StreamHandler()
file_handler: logging.FileHandler = logging.FileHandler('custom-formmater.log')
formatter: StatusFormatter = StatusFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.DEBUG,
    format=logging.BASIC_FORMAT,
    handlers=[console_handler, file_handler]
)

logger: logging.Logger = logging.getLogger(__name__)

def log_messages():
    logger.debug('This is a simple DEBUG log.')
    logger.info('This is a simple INFO log.', extra={"status": "success"})
    logger.warning('This is a simple WARNING log.')
    logger.error('This is a simple ERROR log.')
    logger.critical('This is a simple CRITICAL log.')

if __name__ == '__main__':
    log_messages()
    first_logs()
    second_logs()