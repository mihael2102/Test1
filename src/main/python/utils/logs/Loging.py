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
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        self.ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(self.ch)
        with allure.step(message):
           self.logger.debug(class_name.__class__.__name__ + " - " + message)
        self.logger.removeHandler(self.ch)
