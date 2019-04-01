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
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MyDashboardPage(CRMBasePage):

    def check_latest_sales_loaded(self):
        sleep(2)
        self.driver.find_element_by_xpath("//h3[contains(text(),'Latest Sales Insights')]")
        Logging().reportDebugStep(self, "Latest Sales Insights is loaded")
        return MyDashboardPage(self.driver)

    def check_task_section_contains_record(self):
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[2]/div/ \
                                tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]")
        Logging().reportDebugStep(self, "Your Tasks section contain records")
        return MyDashboardPage(self.driver)

    def check_client_segmentation_contains_record(self):
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[1]/div[2]/ \
                                                sales-dashboard-segmentation/div/table[2]/tbody/tr[1]")
        Logging().reportDebugStep(self, "Client Segmentation section contain records")
        return MyDashboardPage(self.driver)

    def enter_account_name(self, testqa):
        sleep(1)
        input = self.driver.find_element_by_xpath("//*[@id='host-element']/input")
        input.send_keys(testqa)
        sleep(5)
        Logging().reportDebugStep(self, "Enter account name")
        return MyDashboardPage(self.driver)

    def get_account_name(self):
        sleep(3)
        account_name = self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[6]/grid-cell/div/span[2]/a")
        Logging().reportDebugStep(self, "Get account name")
        return account_name.text


    def click_pencil_icon(self):
        sleep(4)
        pencil_icon = self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[18]/div[5]/div/span")
        pencil_icon.click()
        Logging().reportDebugStep(self, "Click pencil icon")
        return MyDashboardPage(self.driver)

    def get_status(self):
        sleep(3)
        get_status = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[5]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get status")
        return get_status.text


    def get_type(self):
        sleep(3)
        get_type = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[3]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get type")
        return get_type.text


    def get_time(self):
        sleep(3)
        get_time = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[4]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get type")
        return get_time.text