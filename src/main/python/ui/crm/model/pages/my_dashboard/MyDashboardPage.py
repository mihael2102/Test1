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
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[1]/div[2]/ \
                                                sales-dashboard-segmentation/div/table[2]/tbody/tr[1]")
        Logging().reportDebugStep(self, "Client Segmentation section contain records")
        return MyDashboardPage(self.driver)

    def sort_by_status(self):
        sleep(3)
        sort_by_type = super().wait_load_element(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/thead/tr/th[5]/a")
        sort_by_type.click()
        self.wait_crm_loading_to_finish_tasks(165)
        Logging().reportDebugStep(self, "Sort by status")
        return MyDashboardPage(self.driver)

    def sort_by_type(self):
        sleep(3)
        sort_by_type = super().wait_load_element(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/thead/tr/th[3]/a")
        try:
            sort_by_type.click()
        except:
            self.driver.execute_script("arguments[0].click();", sort_by_type)
        self.wait_crm_loading_to_finish_tasks(180)
        Logging().reportDebugStep(self, "Sort by type")
        return MyDashboardPage(self.driver)

    def enter_priority(self, assigned_to):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[15]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button",
            timeout=70)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[15]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(assigned_to)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[15]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input",
            timeout=70)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter priority")
        return MyDashboardPage(self.driver)

    def enter_subject(self, balance):
        sleep(15)
        input = self.driver.find_element_by_xpath("//td[16]//input[@class='ng-untouched ng-pristine ng-valid']")
        input.send_keys(balance)
        sleep(50)
        Logging().reportDebugStep(self, "Enter subject")
        return MyDashboardPage(self.driver)

    def enter_total_p_l(self, balance):
        sleep(15)
        input = self.driver.find_element_by_xpath("//td[13]//input")
        input.send_keys(balance)
        sleep(50)
        Logging().reportDebugStep(self, "Enter total_p_l")
        return MyDashboardPage(self.driver)

    def enter_balance(self, balance):
        sleep(15)
        input = self.driver.find_element_by_xpath("//td[12]//input")
        input.send_keys(balance)
        sleep(50)
        Logging().reportDebugStep(self, "Enter balance")
        return MyDashboardPage(self.driver)

    def enter_local_time(self, local_time):
        sleep(15)
        input = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[11]/filters-factory/time-range-filter/input")
        input.send_keys(local_time)
        sleep(5)
        Logging().reportDebugStep(self, "Enter local time")
        return MyDashboardPage(self.driver)

    def enter_created_by(self, assigned_to):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[10]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button",
            timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[10]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(assigned_to)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[10]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input",
            timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter created by")
        return MyDashboardPage(self.driver)

    def enter_assigned_to(self, assigned_to):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[9]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button",
            timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[9]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(assigned_to)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[9]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input",
            timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter assigned to")
        return MyDashboardPage(self.driver)

    def enter_country(self, country):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[8]/filters-factory/select-search-filter/select-search/div/div[1]",
            timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[8]/filters-factory/select-search-filter/select-search/div/div[2]/span[1]/input",
            timeout=10)
        country_new = country.replace(' ', '')
        input_account_name.send_keys(country_new)
        sleep(10)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[8]/filters-factory/select-search-filter/select-search/div/div[2]//span[contains(text(), 'Germany')]")
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        sleep(2)
        Logging().reportDebugStep(self, "Enter country")
        return MyDashboardPage(self.driver)

    def enter_account_status(self, status):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[7]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button",
            timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[7]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(status)
        sleep(20)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[7]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input",
            timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter account status")
        return MyDashboardPage(self.driver)

    def enter_status(self, status):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button",
            timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(status)
        sleep(20)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input",
            timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView();", check_box)
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        sleep(2)
        Logging().reportDebugStep(self, "Enter status")
        return MyDashboardPage(self.driver)

    def enter_event_type(self, type):
        btn_type = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button",
            timeout=30)
        btn_type.click()
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(type)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input",
            timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView();", check_box)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter event type")
        return MyDashboardPage(self.driver)

    def get_subject(self):
        sleep(5)
        subject = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[16]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get subject")
        return subject.text

    def get_priority(self):
        sleep(5)
        priority = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[15]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get priority")
        return priority.text

    def get_total_p_l(self):
        sleep(5)
        total_p_l = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[13]/grid-cell/div/span[2]/div/i/span[2]")
        Logging().reportDebugStep(self, "Get total_p_l")
        return total_p_l.text

    def get_balance(self):
        sleep(5)
        balance = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[12]/grid-cell/div/span[2]/div/i/span[2]")
        Logging().reportDebugStep(self, "Get balance")
        return balance.text

    def get_local_time(self):
        sleep(5)
        local_time = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[11]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get local time")
        return local_time.text

    def get_created_by(self):
        sleep(5)
        created_by = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[10]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get created by")
        return created_by.text

    def get_assigned_to(self):
        sleep(5)
        assigned_to = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[9]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get assigned to")
        return assigned_to.text

    def get_country(self):
        sleep(5)
        country = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[8]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get country")
        return country.text

    def get_account_status(self):
        sleep(5)
        account_status = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[7]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get account status")
        return account_status.text

    def check_pop_up_send_sms(self):
        sleep(5)
        try:
            title = super().wait_load_element("/html/body/bs-modal[17]/div/div/div/div[2]/div[1]/div/span/h4")

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
        first_check_box = super().wait_load_element(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[18]/div[1]/div")
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
        sleep(3)
        click_send = super().wait_load_element("/html/body/bs-modal[12]/div/div/div/div[3]/span/button[4]")
        click_send.click()
        Logging().reportDebugStep(self, "Click Send")
        return MyDashboardPage(self.driver)

    # def check_latest_sales_loaded(self):
    #     sleep(2)
    #     self.driver.find_element_by_xpath("//h3[contains(text(),'Latest Sales Insights')]")
    #     Logging().reportDebugStep(self, "Latest Sales Insights is loaded")
    #     return MyDashboardPage(self.driver)
    #
    # def check_task_section_contains_record(self):
    #     sleep(1)
    #     self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[2]/div/ \
    #                             tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]")
    #     Logging().reportDebugStep(self, "Your Tasks section contain records")
    #     return MyDashboardPage(self.driver)
    #
    # def check_client_segmentation_contains_record(self):
    #     sleep(1)
    #     self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[1]/div[2]/ \
    #                                             sales-dashboard-segmentation/div/table[2]/tbody/tr[1]")
    #     Logging().reportDebugStep(self, "Client Segmentation section contain records")
    #     return MyDashboardPage(self.driver)

    def select_show_all_tab(self):
        # sleep(10)
        self.wait_crm_loading_to_finish_tasks(85)
        select_show_all_tab = self.driver.find_element_by_xpath(
            "//*[@id='main-tabs']/li[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", select_show_all_tab)
        try:
            select_show_all_tab.click()
        except:
            self.driver.execute_script("arguments[0].click();", select_show_all_tab)
        sleep(2)
        self.wait_crm_loading_to_finish_tasks(65)
        Logging().reportDebugStep(self, "Select show all tab")
        return MyDashboardPage(self.driver)

    def enter_account_name(self, testqa):
        sleep(5)
        input = self.driver.find_element_by_xpath("//*[@id='host-element']/input")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        sleep(1)
        input.send_keys(testqa)
        sleep(1)
        self.wait_crm_loading_to_finish_tasks(55)
        sleep(3)
        Logging().reportDebugStep(self, "Enter account name: " + testqa)
        return MyDashboardPage(self.driver)

    def get_account_name(self):
        sleep(4)
        account_name = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[6]/grid-cell/div/span[2]/a").text
        Logging().reportDebugStep(self, "Get account name: " + account_name)
        return account_name

    def click_pencil_icon(self):
        sleep(4)
        pencil_icon = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[18]/div[5]/div/span")
        pencil_icon.click()
        Logging().reportDebugStep(self, "Click pencil icon")
        return MyDashboardPage(self.driver)

    def get_status(self):
        sleep(5)
        get_status = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[5]/grid-cell/div/span[2]")\
            .text
        Logging().reportDebugStep(self, "Get status: " + get_status)
        return get_status

    def get_type(self):
        sleep(5)
        get_type = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[3]/grid-cell/div/span[2]")\
                .text
        Logging().reportDebugStep(self, "Get type: " + get_type)
        return get_type

    def get_time(self):
        sleep(5)
        get_time = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[4]/grid-cell/div/span[2]")\
            .text
        Logging().reportDebugStep(self, "Get type: " + get_time)
        return get_time