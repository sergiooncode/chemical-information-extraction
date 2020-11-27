import logging

from config.constants import DEFAULT_LOG_LEVEL
from src.common.logging.base.logging_interface import LoggerInterface

logging.basicConfig(level=DEFAULT_LOG_LEVEL)


class LoggingAdapter(LoggerInterface):
    def critical(
        self,
        message: str,
    ):
        logging.critical(message)

    def error(
        self,
        message: str,
    ):
        logging.error(message)

    def warning(
        self,
        message: str,
    ):
        logging.warning(message)

    def info(
        self,
        message: str,
    ):
        logging.info(message)

    def debug(
        self,
        message: str,
    ):
        logging.debug(message)
