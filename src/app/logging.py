import logging
import datetime


class Logs:
    def __int__(self):
        self.timestamp = datetime.datetime.now()

    def info(self, data: str):
        message = "{}: File loading {}".format(self.timestamp, data)
        logging.info(message)

    def error(self, error_data: str):
        message = "{}: Error data :{}".format(self.timestamp, error_data)
        logging.error(message)
