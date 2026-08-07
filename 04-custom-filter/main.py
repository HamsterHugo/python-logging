import logging
from firstChild import first_logs
from secondChild import second_logs

class WordFilter(logging.Filter):
    def __init__(self, word: str, reverse: bool=False):
        self.word = word
        self.reverse = reverse
    
    def filter(self, record: logging.LogRecord) -> bool:
        check: bool = self.word in record.msg
        if self.reverse: check = not check
        return check

filter1: WordFilter = WordFilter('WORD')
filter2: WordFilter = WordFilter('WORD', reverse=True)

console_handler: logging.StreamHandler = logging.StreamHandler()
file_handler: logging.FileHandler = logging.FileHandler('custom-filter.log')

console_handler.addFilter(filter1)
file_handler.addFilter(filter2)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    datefmt="[%d.%m.%Y %X]",
    handlers=[console_handler, file_handler]
)

logger: logging.Logger = logging.getLogger(__name__)

def log_messages():
    logger.debug('This is a simple DEBUG log: WORD')
    logger.info('This is a simple INFO log.')
    logger.warning('This is a simple WARNING log.')
    logger.error('This is a simple ERROR log.')
    logger.critical('This is a simple CRITICAL log: WORD')

if __name__ == '__main__':
    log_messages()
    first_logs()
    second_logs()