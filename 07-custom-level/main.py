import logging
from firstChild import first_logs
from secondChild import second_logs

SUCCESS: int = 21
COMPLETE: int = 22
FAIL: int = 23

logging.addLevelName(SUCCESS, 'SUCCESS')
logging.addLevelName(COMPLETE, 'COMPLETE')
logging.addLevelName(FAIL, 'FAIL')

def success(self, message, *args, **kwargs):
    if self.isEnabledFor(SUCCESS):
        self._log(SUCCESS, message, args, **kwargs)

def complete(self, message, *args, **kwargs):
    if self.isEnabledFor(COMPLETE):
        self._log(COMPLETE, message, args, **kwargs)

def fail(self, message, *args, **kwargs):
    if self.isEnabledFor(FAIL):
        self._log(FAIL, message, args, **kwargs)

logging.Logger.success = success
logging.Logger.complete = complete
logging.Logger.fail = fail

console_handler: logging.StreamHandler = logging.StreamHandler()
file_handler: logging.FileHandler = logging.FileHandler('custom-level.log')

logging.basicConfig(
    level=logging.DEBUG,
    format=logging.BASIC_FORMAT,
    handlers=[console_handler, file_handler]
)

logger: logging.Logger = logging.getLogger(__name__)

def log_messages():
    logger.debug('This is a simple DEBUG log.')
    logger.info('This is a simple INFO log.')
    logger.success('This is a simple SUCCESS log.')
    logger.complete('This is a simple COMPLETE log.')
    logger.fail('This is a simple FAIL log.')
    logger.warning('This is a simple WARNING log.')
    logger.error('This is a simple ERROR log.')
    logger.critical('This is a simple CRITICAL log.')

if __name__ == '__main__':
    log_messages()
    first_logs()
    second_logs()