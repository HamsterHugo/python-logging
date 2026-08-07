import logging

logger: logging.Logger = logging.getLogger(__name__)

def second_logs():
    logger.debug('This is a simple DEBUG log from "secondChild.py".')
    logger.info('This is a simple INFO log from "secondChild.py".')
    logger.info('This is a simple INFO log with a SUCCESS-Label from "secondChild.py".', extra={"status": "success"})
    logger.info('This is a simple INFO log with a COMPLETE-Label from "secondChild.py".', extra={"status": "complete"})
    logger.info('This is a simple INFO log with a FAIL-Label from "secondChild.py".', extra={"status": "fail"})
    logger.info('This is a simple INFO log with a REPORT-Label from "secondChild.py".', extra={"status": "report"})
    logger.warning('This is a simple WARNING log from "secondChild.py".')
    logger.error('This is a simple ERROR log from "secondChild.py".')
    logger.critical('This is a simple CRITICAL log from "secondChild.py".')

if __name__ == '__main__':
    second_logs()