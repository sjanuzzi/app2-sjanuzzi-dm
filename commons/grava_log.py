import logging
import logging.config

logging.config.fileConfig(fname='commons/log.config', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def log_debug(message):
    logging.debug(message)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_critial(message):
    logging.critical(message)


