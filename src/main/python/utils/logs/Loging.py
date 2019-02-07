# create logger
import logging

import allure


class Logging(object):
    logger = None

    def reportDebugStep(self, class_name, message):
        self.logger = logging.getLogger("Logger")
        self.logger.setLevel(logging.DEBUG)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(message)s')

        # add formatter to ch
        self.ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(self.ch)
        with allure.step(message):
           self.logger.debug(message)
        self.logger.removeHandler(self.ch)