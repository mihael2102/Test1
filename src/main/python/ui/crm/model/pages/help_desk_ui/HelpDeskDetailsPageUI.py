import re
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from _decimal import Decimal
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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
from selenium.webdriver.support.select import Select
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class HelpDeskDetailsPageUI(CRMBasePage):

    def get_title(self):
        sleep(0.1)
        title = super().wait_load_element(
            "//div[label='Title']//following-sibling::button/span[@class='btn-txt-wrapper']").text
        Logging().reportDebugStep(self, "Get Ticket title: " + title)
        return title

    def get_status(self):
        sleep(0.1)
        status = super().wait_load_element(
            "//div[label='Status']//following-sibling::button/span[@class='text-left btn-txt-wrapper']").text
        Logging().reportDebugStep(self, "Get Status: " + status)
        return status

    def get_source(self):
        sleep(0.1)
        source = super().wait_load_element(
            "//div[label='Ticket Source']//following-sibling::button/span[@class='text-left btn-txt-wrapper']").text
        Logging().reportDebugStep(self, "Get Status: " + source)
        return source

    def get_assigned_to(self):
        sleep(0.1)
        assigned_to = super().wait_load_element(
            "//div[label='Assigned To']//following-sibling::button/span[@class='text-left btn-txt-wrapper']").text
        Logging().reportDebugStep(self, "Get Assigned To: " + assigned_to)
        return assigned_to

    def get_category(self):
        sleep(0.1)
        category = super().wait_load_element(
            "//div[label='Category']//following-sibling::button/span[@class='text-left btn-txt-wrapper']").text
        Logging().reportDebugStep(self, "Get Assigned To: " + category)
        return category

    def get_priority(self):
        sleep(0.1)
        priority = super().wait_load_element(
            "//div[label='Priority']//following-sibling::button/span[@class='text-left btn-txt-wrapper']").text
        Logging().reportDebugStep(self, "Get Priority: " + priority)
        return priority

    def get_description(self):
        sleep(0.1)
        description = super().wait_load_element(
            "//div[label='Description']//following-sibling::button/span[@class='text-left btn-txt-wrapper']").text
        Logging().reportDebugStep(self, "Get Priority: " + description)
        return description

    def open_tab(self, title):
        tab = super().wait_load_element(
            "//mat-expansion-panel-header[@aria-disabled='false']//mat-panel-title[contains(text(),'%s')]" % title)
        self.driver.execute_script("arguments[0].click();", tab)
        Logging().reportDebugStep(self, "Open tab: " + title)
        return HelpDeskDetailsPageUI(self.driver)
