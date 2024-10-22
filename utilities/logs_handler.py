import logging


class LogHandler():

    @staticmethod
    def create_logger():
        """
        Create a logger to capture important events

        Returns
        -------
        logger: Logger
        """
        logger = logging.getLogger("test_logger")

        # Set logging level
        logger.setLevel(logging.INFO)

        # Create a log file handler and a logging format to display logs
        handler = logging.FileHandler(filename="test_logs.log", mode="w")
        formatter = logging.Formatter(
            "%(asctime)s - Sauce Demo App - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
