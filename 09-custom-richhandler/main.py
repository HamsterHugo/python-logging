import logging
from firstChild import first_logs
from secondChild import second_logs

from rich.logging import RichHandler
from rich.console import Console
from rich.theme import Theme
from rich.terminal_theme import MONOKAI
from rich.style import Style

custom_theme: Theme = Theme({
    "logging.level.debug": Style(color='magenta', bold=True),
    "logging.level.info": Style(color='cyan'),
    "logging.level.warning": Style(color='dark_orange', bold=True),
    "logging.level.error": Style(color='red', bold=True),
    "logging.level.critical": Style(color='red', bold=True, reverse=True),
})

console: Console = Console(record=True, theme=custom_theme)

console_handler: RichHandler = RichHandler(console=console, rich_tracebacks=True)
file_handler: logging.FileHandler = logging.FileHandler('richLogging.log')

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
    console.save_html('richLogging.html', theme=MONOKAI)