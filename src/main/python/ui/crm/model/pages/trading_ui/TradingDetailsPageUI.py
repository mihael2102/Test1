from time import sleep
from datetime import *
import allure
from allure.constants import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.utils.logs.Loging import Logging


class TradingDetailsPageUI(CRMBasePage):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

    def display_open_trades(self):
        sleep(0.1)
        btn = super().wait_element_to_be_clickable("//span[text()=' Display open trades ']")
        self.driver.execute_script("arguments[0].click();", btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Click 'Display open trades' button")
        return TradingDetailsPageUI(self.driver)

    def get_open_orders_data(self):
        sleep(0.2)
        open_orders_data = super().wait_load_element(
            "(//div[div='Open trades']//following-sibling::pnd-grid//tbody/tr[not(contains(@style,'hidden'))])[1]")\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get Open Orders data: " + open_orders_data)
        return open_orders_data

    def get_closed_orders_data_ui(self):
        sleep(0.2)
        open_orders_data = super().wait_load_element(
            "//mat-expansion-panel[@id='closed-transactions']//tbody[@role='rowgroup']")\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get Open Orders data: " + open_orders_data)
        return open_orders_data
