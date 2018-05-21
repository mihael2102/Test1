import unittest
from selenium import webdriver
from src.main.python.ui.brand.model.data.providers.DataProviders import DataProviders
from src.main.python.utils.config import Config


class BaseTest(unittest.TestCase):

    def setUp(self):
        Config.data = DataProviders()
        selenium_grid_url = "http://10.0.0.94:4478/wd/hub"
        options = webdriver.ChromeOptions()

        options.add_argument("--lang=de")
        options.add_argument("--start-maximized")
        Config.browser = webdriver.Remote(desired_capabilities=options.to_capabilities(),
                                          command_executor=selenium_grid_url)

    def tearDown(self):
        Config.browser.close()
        Config.browser.quit()
