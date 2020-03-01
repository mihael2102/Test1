from time import sleep
from datetime import *
import allure
from allure.constants import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.trading_ui.TradingDetailsPageUI import TradingDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.utils.logs.Loging import Logging


class TradingModulePageUI(CRMBasePage):

    def click_on_ta_number(self, ta_number):
        sleep(0.1)
        btn = super().wait_element_to_be_clickable("//span[text()=' %s ']" % ta_number)
        self.driver.execute_script("arguments[0].click();", btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Open details page of TA: " + ta_number)
        return GlobalDetailsPageUI(self.driver)
