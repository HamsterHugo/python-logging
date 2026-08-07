import logging

logger: logging.Logger = logging.getLogger(__name__)

def first_logs():
    logger.debug('This is a simple DEBUG log from "firstChild.py".')
    logger.info('This is a simple INFO log from "firstChild.py".')
    logger.info('This is a simple INFO log with a SUCCESS-Label from "firstChild.py".', extra={"status": "success"})
    logger.info('This is a simple INFO log with a COMPLETE-Label from "firstChild.py".', extra={"status": "complete"})
    logger.info('This is a simple INFO log with a FAIL-Label from "firstChild.py".', extra={"status": "fail"})
    logger.info('This is a simple INFO log with a REPORT-Label from "firstChild.py".', extra={"status": "report"})
    logger.warning('This is a simple WARNING log from "firstChild.py".')
    logger.error('This is a simple ERROR log from "firstChild.py".')
    logger.critical('This is a simple CRITICAL log from "firstChild.py".')

if __name__ == '__main__':
    first_logs()