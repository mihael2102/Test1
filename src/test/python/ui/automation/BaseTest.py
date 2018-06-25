from datetime import *
import unittest
import allure
from allure.constants import AttachmentType
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

        report_started = datetime.now().strftime("%d-%m-%Y") + " " + datetime.now().strftime("%H:%M:%S")

        allure.MASTER_HELPER.environment(BROWSER="CHROME", REPORT_STARTED_AT=report_started,
                                         URL_BRAND=Config.url_client_area, URL_CRM=Config.url_crm)

    def tearDown(self):
        report_finished = datetime.now().strftime("%d-%m-%Y") + " " + datetime.now().strftime("%H:%M:%S")
        allure.MASTER_HELPER.environment(REPORT_FINISHED_AT=report_finished)

        """Take a Screen-shot of the drive homepage, when it Failed."""
        if self._outcome.errors:
            for method, error in self._outcome.errors:
                if error:
                    fail_url = Config.browser.current_url
                    print(fail_url)
                    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
                    file_name = 'C:/Users/Administrator/.jenkins/workspace/Smoke New Forex Staging/src/screen_shots/failed_screenshots/failed_screenshot %s.png' % now
                    Config.browser.get_screenshot_as_file(file_name)
                    allure.MASTER_HELPER.attach('failed_screenshot', Config.browser.get_screenshot_as_png(),
                                                type=AttachmentType.PNG)

                    allure.MASTER_HELPER.environment(REPORT_FINISHED=datetime.now())

                    Config.browser.close()
                    Config.browser.quit()
        else:
            Config.browser.close()
            Config.browser.quit()
