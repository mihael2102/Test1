from datetime import *
import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from src.main.python.utils.data.providers.DataProviders import DataProviders
from src.main.python.utils.data.providers.ConfigProvider import ConfigProvider
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging


class BaseTest(unittest.TestCase):

    data_provider = None
    driver_type = None
    data = None

    def setUp(self):
        global driver
        if self.data_provider is None:
            self.data = DataProviders()
        else:
            self.data = self.data_provider
        allure.MASTER_HELPER.environment(BROWSER="CHROME", URL_BRAND=Config.url_client_area, URL_CRM=Config.url_crm)
        if self.driver_type is None:
            selenium_grid_url = "http://localhost:5578/wd/hub/"
            options = webdriver.ChromeOptions()
            options.add_argument("--lang=en")
            options.add_argument("--start-maximized")
            driver = webdriver.Remote(desired_capabilities=options.to_capabilities(),
                                      command_executor=selenium_grid_url)
        elif self.driver_type == 'Chrome':
            driver = webdriver.Chrome(Config.chrome_driver)
            driver.maximize_window()

    @property
    def get_driver(self):
        return driver

    def tearDown(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        if self._outcome.errors:
            for method, error in self._outcome.errors:
                if error:
                    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
                    # file_name = 'C:/Users/Administrator/.jenkins/workspace/Regression New Forex Staging' \
                    #             '/allure/results/failed_screenshot %s.png' % now
                    #
                    # driver.get_screenshot_as_file(file_name)
                    # allure.MASTER_HELPER.attach('failed_screenshot', driver.get_screenshot_as_png(),
                    #                             type=AttachmentType.PNG)
        driver.close()
        driver.quit()
