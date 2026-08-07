import logging
from typing import ClassVar

from rich.logging import RichHandler
from rich.text import Text

from firstChild import first_logs
from secondChild import second_logs

ICONS = {
    "DEBUG": "🐛",
    "INFO": "ℹ️",
    "WARNING": "⚠️",
    "ERROR": "❌",
    "CRITICAL": "🔥",
}

class IconRichHandler(RichHandler):
    LEVEL_ICONS: ClassVar[dict] = ICONS

    def get_level_text(self, record: logging.LogRecord) -> Text:
        level_name = record.levelname
        level_icon = self.LEVEL_ICONS[level_name]
        space: int = 4 if level_name in ["INFO", "WARNING"] else 2
        return level_icon.ljust(space)

console_handler: IconRichHandler = IconRichHandler()
file_handler: logging.FileHandler = logging.FileHandler('icons.log')

formatter: logging.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%d.%m.%Y - %X]",
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