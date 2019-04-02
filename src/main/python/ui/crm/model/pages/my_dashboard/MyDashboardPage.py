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

    def check_pop_up_send_sms(self):
        sleep(5)
        try:
            title = super().wait_load_element("/html/body/bs-modal[12]/div/div/div/div[2]/div[1]/div/span/h4")

        except:
            title = super().wait_load_element("/html/body/bs-modal[17]/div/div/div/div[2]/h3")
        Logging().reportDebugStep(self, title.text)
        return title.text

    def click_sms_icon(self):
        sleep(3)
        first_check_box = super().wait_load_element(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[18]/div[2]/div")
        first_check_box.click()
        Logging().reportDebugStep(self, "Click SMS icon")
        return MyDashboardPage(self.driver)

    def open_email_actions_section(self):
        sleep(3)
        first_check_box = super().wait_load_element("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[18]/div[1]/div")
        first_check_box.click()
        Logging().reportDebugStep(self, "The email module was opened")
        return MyDashboardPage(self.driver)


    def enter_subject_mail(self, subject):
        sleep(4)
        subject_mail = super().wait_load_element("//div[@class='modal-dialog modal-lg']//input[@id='subject']")
        subject_mail.send_keys(subject)
        Logging().reportDebugStep(self, "Enter subject mail" + subject)
        return MyDashboardPage(self.driver)

    def enter_body_mail(self, body):
        sleep(4)
        self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//iframe[@title='Rich Text Editor, editor2']"))
        enter_body_mail = self.driver.find_element(By.XPATH, "/html/body/p")
        enter_body_mail.click()
        self.driver.execute_script("arguments[0].textContent = arguments[1];", enter_body_mail, body)
        # enter_body_mail.send_keys(body)
        Logging().reportDebugStep(self, "Enter body mail")
        return MyDashboardPage(self.driver)


    def enter_cc_mail(self, cc_mail):
        self.driver.switch_to.default_content()
        sleep(3)
        subject_mail = super().wait_load_element("//div[@class = 'modal-dialog modal-lg']//input[@id='email_cc']")
        subject_mail.send_keys(cc_mail)
        Logging().reportDebugStep(self, "Enter cc mail" + cc_mail)
        return MyDashboardPage(self.driver)

    def click_send(self):
        self.driver.switch_to.default_content()
        sleep(10)
        click_send = super().wait_load_element("/html/body/bs-modal[12]/div/div/div/div[3]/span/button[4]")
        click_send.click()
        Logging().reportDebugStep(self, "Click Send")
        return MyDashboardPage(self.driver)


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

    def select_show_all_tab(self):
        sleep(4)
        select_show_all_tab = self.driver.find_element_by_xpath(
            "//*[@id='main-tabs']/li[1]")
        select_show_all_tab.click()
        Logging().reportDebugStep(self, "Select show all tab")
        return MyDashboardPage(self.driver)

    def enter_account_name(self, testqa):
        sleep(15)
        input = self.driver.find_element_by_xpath("//*[@id='host-element']/input")
        input.send_keys(testqa)
        sleep(50)
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
        sleep(5)
        get_status = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[5]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get status")
        return get_status.text


    def get_type(self):
        sleep(5)
        get_type = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[3]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get type")
        return get_type.text


    def get_time(self):
        sleep(5)
        get_time = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[4]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get type")
        return get_time.text