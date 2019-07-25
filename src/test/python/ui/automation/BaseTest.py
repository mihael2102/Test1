import unittest
from datetime import *
#import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.main.python.utils.config import Config
from src.main.python.utils.data.providers.ConfigProvider import ConfigProvider
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver_type = None
        self.config = None
        self.driver = None

    def setUp(self):
        if not self.config:
            self.config = ConfigProvider()
        #allure.MASTER_HELPER.environment(BROWSER="CHROME", URL_BRAND=Config.url_client_area, URL_CRM=Config.url_crm)
        if self.driver_type is None or self.driver_type == 'Chrome':

            ' For hidden browser: '
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(Config.user_agent)
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            self.driver = webdriver.Chrome(Config.chrome_driver, chrome_options=chrome_options)

            ' For opened chrome: '
            # opts = Options()
            # opts.add_argument(Config.user_agent)
            # self.driver = webdriver.Chrome(chrome_options=opts, executable_path=Config.chrome_driver)
            # self.driver.maximize_window()
        elif self.driver_type == 'Remote':
            selenium_grid_url = "http://localhost:5578/wd/hub/"
            options = webdriver.ChromeOptions()
            options.add_argument("--lang=en")
            options.add_argument("--start-maximized")
            self.driver = webdriver.Remote(desired_capabilities=options.to_capabilities(),
                                      command_executor=selenium_grid_url)
            # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", webdriver.DesiredCapabilities.CHROME)
        else:
            raise TypeError("Invalid web driver")

    def tearDown(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        if self._outcome.errors:
            for method, error in self._outcome.errors:
                if error:
                    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
                    print("%s %s" % (now, error))
                    # file_name = 'C:/Users/Administrator/.jenkins/workspace/Regression New Forex Staging' \
                    #             '/allure/results/failed_screenshot %s.png' % now
                    #
                    # driver.get_screenshot_as_file(file_name)
                    # allure.MASTER_HELPER.attach('failed_screenshot', driver.get_screenshot_as_png(),
                    #                             type=AttachmentType.PNG)
        sleep(3)
        self.driver.close()
        self.driver.quit()
