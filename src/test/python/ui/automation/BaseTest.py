from datetime import *
import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from src.main.python.ui.brand.model.data.providers.DataProviders import DataProviders
from src.main.python.utils.config import Config


class BaseTest(unittest.TestCase):

    def setUp(self):
        global driver
        Config.data = DataProviders()
        allure.MASTER_HELPER.environment(BROWSER="CHROME", URL_BRAND=Config.url_client_area, URL_CRM=Config.url_crm)
        selenium_grid_url = "http://localhost:5578/wd/hub/"
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en")
        options.add_argument("--start-maximized")
        driver = webdriver.Remote(desired_capabilities=options.to_capabilities(),
                                  command_executor=selenium_grid_url)

    @property
    def get_driver(self):
        return driver

    def tearDown(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        if self._outcome.errors:
            for method, error in self._outcome.errors:
                if error:
                    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
                    file_name = 'C:/Users/Administrator/.jenkins/workspace/Regression New Forex Staging' \
                                '/allure/results/failed_screenshot %s.png' % now

                    driver.get_screenshot_as_file(file_name)
                    allure.MASTER_HELPER.attach('failed_screenshot', driver.get_screenshot_as_png(),
                                                type=AttachmentType.PNG)

                    self.browser.close()
                    self.browser.quit()

        else:
            # self.browser.close()
            # self.browser.quit()