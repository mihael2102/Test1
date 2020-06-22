import re
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from _decimal import Decimal
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from selenium.webdriver.support.select import Select
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


class ClientsModulePageUI(CRMBasePage):

    def click_crm_id_ui(self, row='1'):
        sleep(0.1)
        crm_id = super().wait_element_to_be_clickable(
            "//tbody/tr[@role='row' and not(contains(@style,'hidden'))][%s]//span[contains(text(),'ACC')]" % row)
        self.driver.execute_script("arguments[0].click();", crm_id)
        sleep(1)
        self.wait_loading_to_finish_new_ui(15)
        Logging().reportDebugStep(self, "Open client's details")
        return ClientDetailsPageUI(self.driver)

    def select_filter_ui(self, test_filter):
        GlobalModulePageUI(self.driver)\
            .select_filter_new_ui(test_filter)
        return ClientsModulePageUI(self.driver)

    def set_data_column_field(self, column, data):
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column, data)
        return ClientsModulePageUI(self.driver)

    def get_data_from_list_view_ui(self, column, row):
        data = GlobalModulePageUI(self.driver)\
            .get_data_from_list_view_ui(column, row)
        return data
