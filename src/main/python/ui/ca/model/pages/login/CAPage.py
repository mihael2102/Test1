from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class CAPage(CRMBasePage):

    def open_manage_accounts(self):
        manage_accounts_button = super().wait_element_to_be_clickable \
                    ("//li[@class='ng-star-inserted'][contains(text(), 'Manage Accounts')]")
        sleep(1)
        manage_accounts_button.click()
        Logging().reportDebugStep(self, "Click Manage Accounts button")
        return CAPage(self.driver)