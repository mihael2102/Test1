from datetime import *
import unittest

import sys
from selenium import webdriver
from src.main.python.ui.brand.model.data.providers.DataProviders import DataProviders
from src.main.python.utils.config import Config


class BaseTest(unittest.TestCase):

    def setUp(self):
        Config.data = DataProviders()
        selenium_grid_url = "http://localhost:5578/wd/hub/"
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=de")
        options.add_argument("--start-maximized")
        Config.browser = webdriver.Remote(desired_capabilities=options.to_capabilities(),
                                          command_executor=selenium_grid_url)

    def tearDown(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                fail_url = Config.browser.current_url
                print(fail_url)
                now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
                Config.browser.get_screenshot_as_file(
                    'D:/automation-newforexqa/%s.png' % now)  # my tests work in parallel, so I need uniqe file names
                fail_screenshot_url = 'http://debugtool/screenshots/%s.png' % now
                print(fail_screenshot_url)
                Config.browser.close()
                Config.browser.quit()
