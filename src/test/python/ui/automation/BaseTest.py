from datetime import *
import unittest
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
                file_name = 'D:/automation-newforexqa/src/screen_shots/failed_screenshots/failed_screenshot %s.png' % now
                Config.browser.get_screenshot_as_file(file_name)
                Config.browser.close()
                Config.browser.quit()
            else:
                Config.browser.close()
                Config.browser.quit()
