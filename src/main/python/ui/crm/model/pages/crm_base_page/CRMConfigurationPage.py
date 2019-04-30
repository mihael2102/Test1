import re
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from _decimal import Decimal
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.pages.edit_ticket.BrandEditionTicketInfoPage import EditionTicketInfoPage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.client_modules.client_deposit.CRMClientDeposit import CRMClientDeposit
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.modules.tasks_module.SmsNotifier import SmsNotifierModule
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class CRMConfigurationPage(CRMBasePage):

    def check_common_configuration_loaded(self):
        sleep(2)
        self.driver.find_element_by_xpath("//h1[contains(text(),'Common Configuration')]")
        Logging().reportDebugStep(self, "Common configuration is loaded")
        return CRMConfigurationPage(self.driver)

    def check_brand_configuration_loaded(self):
        sleep(1)
        brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Brand Configuration')]")
        brand_configuration_btn.click()
        self.driver.find_element_by_xpath("//h1[contains(text(),'Brand Configuration')]")
        Logging().reportDebugStep(self, "Brand Configuration is loaded")
        return CRMConfigurationPage(self.driver)

    def check_sms_configuration_loaded(self):
        sleep(1)
        brand_configuration_btn = super().wait_load_element("//div[contains(text(),'SMS Configuration')]")
        brand_configuration_btn.click()
        self.driver.find_element_by_xpath("//h1[contains(text(),'SMS Configuration')]")
        Logging().reportDebugStep(self, "SMS Configuration is loaded")
        return CRMConfigurationPage(self.driver)

    def check_smtp_configuration_loaded(self):
        sleep(1)
        brand_configuration_btn = super().wait_load_element("//div[contains(text(),'SMTP Configuration')]")
        brand_configuration_btn.click()
        self.driver.find_element_by_xpath("//h1[contains(text(),'SMTP Configuration')]")
        Logging().reportDebugStep(self, "SMTP Configuration is loaded")
        return CRMConfigurationPage(self.driver)

    def check_minimum_deposit_loaded(self):
        sleep(1)
        brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Minimum Deposit')]")
        brand_configuration_btn.click()
        self.driver.find_element_by_xpath("//h1[contains(text(),'Minimum Deposit')]")
        Logging().reportDebugStep(self, "Minimum Deposit is loaded")
        return CRMConfigurationPage(self.driver)

    def check_cashier_loaded(self):
        sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'Cashier')]")
            brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Cashier')]")
            brand_configuration_btn.click()
            self.driver.find_element_by_xpath("//h1[contains(text(),'Cashier')]")
            Logging().reportDebugStep(self, "Cashier is loaded")
            return CRMConfigurationPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            pass
            Logging().reportDebugStep(self, "There is no Cashier module")
            return CRMConfigurationPage(self.driver)

    def check_manage_psp_loaded(self):
        sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'Manage PSP')]")
            brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Manage PSP')]")
            brand_configuration_btn.click()
            self.driver.find_element_by_xpath("//h1[contains(text(),'Manage PSP')]")
            Logging().reportDebugStep(self, "Manage PSP is loaded")
            return CRMConfigurationPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            pass
            Logging().reportDebugStep(self, "There is no Manage PSP module")
            return CRMConfigurationPage(self.driver)

    def check_click2call_loaded(self):
        sleep(1)
        brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Click2Call Configuration')]")
        brand_configuration_btn.click()
        self.driver.find_element_by_xpath("//h1[contains(text(),'Click2Call Configuration')]")
        Logging().reportDebugStep(self, "Click2Call Configuration is loaded")
        return CRMConfigurationPage(self.driver)

    def check_referral_configuration_loaded(self):
        sleep(1)
        brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Referral Configuration')]")
        brand_configuration_btn.click()
        self.driver.find_element_by_xpath("//h1[contains(text(),'Referral Configuration')]")
        Logging().reportDebugStep(self, "Referral Configuration is loaded")
        return CRMConfigurationPage(self.driver)

    def check_workflows_loaded(self):
        sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'Workflows')]")
            brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Workflows')]")
            brand_configuration_btn.click()
            self.driver.find_element_by_xpath("//h1[contains(text(),'Workflows')]")
            Logging().reportDebugStep(self, "Workflows is loaded")
            return CRMConfigurationPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            pass
            Logging().reportDebugStep(self, "Workflows module does not exist")
            return CRMConfigurationPage(self.driver)

    def check_sharing_access_loaded(self):
        sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'Sharing Access Rules')]")
            brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Sharing Access Rules')]")
            brand_configuration_btn.click()
            self.driver.find_element_by_xpath("//h1[contains(text(),'Sharing Access Rules')]")
            Logging().reportDebugStep(self, "Sharing Access Rules is loaded")
            return CRMConfigurationPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            pass
            Logging().reportDebugStep(self, "There is no Sharing Access module")
            return CRMConfigurationPage(self.driver)

    def check_email_templates_loaded(self):
        sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'Email Templates')]")
            brand_configuration_btn = super().wait_load_element("//div[contains(text(),'Email Templates')]")
            brand_configuration_btn.click()
            sleep(1)
            self.driver.find_element_by_xpath("//table[@id='emailmakerЗ']")
            Logging().reportDebugStep(self, "EMAIL Maker is loaded")
            return CRMConfigurationPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            pass
            self.driver.find_element_by_xpath("//span[contains(text(), \
                                        'Please note that you do not have sufficient priveleges to access this page')]")
            Logging().reportDebugStep(self, "There is no sufficient priveleges to access EMAIL Maker page")
            return CRMConfigurationPage(self.driver)