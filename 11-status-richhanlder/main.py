import logging
from typing import ClassVar

from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from rich.theme import Theme
from rich.terminal_theme import TerminalTheme

from firstChild import first_logs
from secondChild import second_logs

CUSTOM_TERMINAL_THEME = TerminalTheme(
    (12, 12, 12),
    (217, 217, 217),
    [
        (26, 26, 26),
        (244, 0, 95),
        (152, 224, 36),
        (255, 255, 0),
        (0, 128, 255),
        (244, 0, 95),
        (88, 209, 235),
        (196, 197, 181),
        (98, 94, 76),
    ],
    [
        (244, 0, 95),
        (152, 224, 36),
        (224, 213, 97),
        (0, 128, 255),
        (244, 0, 95),
        (88, 209, 235),
        (246, 246, 239),
    ],
)
STATUS_ICONS: dict = {
        "success": "✔",
        "complete": "★",
        "fail": "✗",
        "report": None
    }
CUSTOM_CONSOLE_THEME: Theme = Theme(
    {
        "logging.level.debug": "magenta",
        "status.success": "green",
        "status.complete": "bold green",
        "status.fail": "red",
        "status.report": "bold dark_orange"
    }
)
FORMAT: str = "%(asctime)s %(name)s %(levelname)s : %(message)s"
DATE_FORMAT: str = "[%d.%m.%y %X]"

class StatusAwareRichHandler(RichHandler):
    STATUS_ICONS: ClassVar[dict] = STATUS_ICONS

    def get_level_text(self, record: logging.LogRecord) -> Text:
        status: str = getattr(record, "status", None)
        if record.levelno == logging.INFO and status in self.STATUS_ICONS:
            label: str = status.upper().ljust(8)
            return Text.styled(f"{label}", f"status.{status}")
        return super().get_level_text(record)

    def render_message(self, record: logging.LogRecord, message: str) -> Text:
        status: str = getattr(record, "status", None)
        message_renderable = super().render_message(record, message)
        if record.levelno == logging.INFO and status in self.STATUS_ICONS:
            icon: str = self.STATUS_ICONS[status]
            if icon is not None:
                message_renderable.append(f" {icon}", style=f"status.{status}")
        return message_renderable

class StatusAwareFormatter(logging.Formatter):
    STATUS: ClassVar[dict] = STATUS_ICONS

    def format(self, record):
        original_levelname = record.levelname
        status = getattr(record, "status", None)
        if record.levelno == logging.INFO and status in self.STATUS:
            record.levelname = status.upper()
        formatted_message = super().format(record)
        record.levelname = original_levelname

        return formatted_message

console: Console = Console(record=True, theme=CUSTOM_CONSOLE_THEME)

def setup_logging(level: int = logging.DEBUG):
    console_handler: StatusAwareRichHandler = StatusAwareRichHandler(
        console=console,
        log_time_format=DATE_FORMAT
    )
    file_handler: logging.FileHandler = logging.FileHandler(
        filename='statusRichHandler.log',
        encoding='utf8'
    )
    formatter: StatusAwareFormatter = StatusAwareFormatter(
        fmt=FORMAT,
        datefmt=DATE_FORMAT
    )
    file_handler.setFormatter(formatter)

    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[console_handler, file_handler]
    )

def save_log_to_html(file_name: str) -> None:
    if not file_name.endswith('.html'): file_name += '.html'
    console.save_html(file_name, theme=CUSTOM_TERMINAL_THEME)

def log_messages():
    logger.debug('This is a simple DEBUG log.')
    logger.info('This is a simple INFO log.')
    logger.info('This is a simple INFO log with a SUCCESS-Label.', extra={"status": "success"})
    logger.info('This is a simple INFO log with a COMPLETE-Label.', extra={"status": "complete"})
    logger.info('This is a simple INFO log with a FAIL-Label.', extra={"status": "fail"})
    logger.info('This is a simple INFO log with a REPORT-Label.', extra={"status": "report"})
    logger.warning('This is a simple WARNING log.')
    logger.error('This is a simple ERROR log.')
    logger.critical('This is a simple CRITICAL log.')

if __name__ == '__main__':
    setup_logging()
    logger: logging.Logger = logging.getLogger(__name__)
    log_messages()
    first_logs()
    second_logs()
    save_log_to_html('statusRichHanlder.html')