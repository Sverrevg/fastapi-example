import logging.config
from logging import Logger


class LoggerBuilder:
    def __init__(self, path_to_config: str, logging_dir: str):
        self.config_path = path_to_config
        self.logging_dir = logging_dir

    def create_logger(self) -> Logger:
        """Setup logging"""
        logging.config.fileConfig(self.config_path)
        logging.FileHandler(self.logging_dir)
        return logging.getLogger("root")
