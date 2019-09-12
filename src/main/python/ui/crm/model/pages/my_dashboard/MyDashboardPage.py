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

    def sort_by_status(self):
        sleep(3)
        sort_by_type = super().wait_load_element("//a[@data-column-label='Status']")
        sort_by_type.click()
        self.wait_crm_loading_to_finish_tasks(75)
        Logging().reportDebugStep(self, "Sort by Status")
        return MyDashboardPage(self.driver)

    def sort_by_type(self):
        sleep(3)
        sort_by_type = super().wait_load_element("//a[@data-column-label='Event Type']")
        sort_by_type.click()
        self.wait_crm_loading_to_finish_tasks(75)
        Logging().reportDebugStep(self, "Sort by Event Type")
        return MyDashboardPage(self.driver)

    def enter_priority(self, priority):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[15]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button", timeout=70)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[15]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(priority)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[15]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input", timeout=70)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter Priority: " + priority)
        return MyDashboardPage(self.driver)

    def enter_subject(self, subject):
        sleep(5)
        input = self.driver.find_element_by_xpath("//td[16]//input[@class='ng-untouched ng-pristine ng-valid']")
        input.send_keys(subject)
        self.wait_crm_loading_to_finish_tasks(75)
        Logging().reportDebugStep(self, "Enter Subject: " + subject)
        return MyDashboardPage(self.driver)

    def enter_total_p_l(self, pnl):
        sleep(5)
        input = self.driver.find_element_by_xpath("//td[13]//input")
        input.send_keys(pnl)
        self.wait_crm_loading_to_finish_tasks(55)
        Logging().reportDebugStep(self, "Enter Total P&L: " + pnl)
        return MyDashboardPage(self.driver)

    def enter_balance(self, balance):
        sleep(5)
        input = self.driver.find_element_by_xpath("//td[12]//input")
        input.send_keys(balance)
        self.wait_crm_loading_to_finish_tasks(35)
        Logging().reportDebugStep(self, "Enter Balance: " + balance)
        return MyDashboardPage(self.driver)

    def enter_local_time(self, local_time):
        sleep(3)
        input = self.driver.find_element_by_xpath("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[11]/filters-factory/time-range-filter/input")
        input.send_keys(local_time)
        self.wait_crm_loading_to_finish_tasks(35)
        Logging().reportDebugStep(self, "Enter Local Time: " + local_time)
        return MyDashboardPage(self.driver)

    def enter_created_by(self, created_by):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[10]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button", timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[10]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(created_by)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[10]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input", timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter Created by: " + created_by)
        return MyDashboardPage(self.driver)

    def enter_assigned_to(self, assigned_to):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[9]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button", timeout=30)
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
        check_box = super().wait_element_to_be_clickable("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[9]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input", timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter Assigned to: " + assigned_to)
        return MyDashboardPage(self.driver)

    def enter_country(self, country):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[8]/filters-factory/select-search-filter/select-search/div/div[1]", timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[8]/filters-factory/select-search-filter/select-search/div/div[2]/span[1]/input",
            timeout=10)
        country_new = country.replace(' ','')
        input_account_name.send_keys(country_new)
        sleep(5)
        check_box = super().wait_element_to_be_clickable("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[8]/filters-factory/select-search-filter/select-search/div/div[2]//span")
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        sleep(2)
        Logging().reportDebugStep(self, "Enter Country: " + country)
        return MyDashboardPage(self.driver)

    def enter_account_status(self, status):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[7]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button", timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[7]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(status)
        sleep(1)
        self.wait_crm_loading_to_finish_tasks(35)
        check_box = super().wait_element_to_be_clickable("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[7]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input", timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter Account status: " + status)
        return MyDashboardPage(self.driver)

    def enter_status(self, status):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button", timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_status.send_keys(status)
        sleep(3)
        check_box = super().wait_element_to_be_clickable("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input", timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView();", check_box)
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        self.wait_crm_loading_to_finish_tasks(35)
        Logging().reportDebugStep(self, "Enter Status: " + status)
        return MyDashboardPage(self.driver)

    def enter_event_type(self, type):
        btn_type = super().wait_load_element(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button" , timeout=30)
        self.perform_scroll_down()
        btn_type.click()
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(type)
        self.wait_crm_loading_to_finish_tasks(55)
        check_box = super().wait_element_to_be_clickable("/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input", timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView();", check_box)
        check_box.click()
        self.wait_crm_loading_to_finish_tasks(35)
        Logging().reportDebugStep(self, "Enter Event Type: " + type)
        return MyDashboardPage(self.driver)

    def get_subject(self):
        sleep(1)
        subject = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[16]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get Subject: " + subject.text)
        return subject.text

    def get_priority(self):
        sleep(1)
        priority = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[15]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get Priority: " + priority.text)
        return priority.text

    def get_total_p_l(self):
        sleep(1)
        total_p_l = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[13]/grid-cell/div/span[2]/div/i/span[2]")
        Logging().reportDebugStep(self, "Get Total P&L: " + total_p_l.text)
        return total_p_l.text

    def get_balance(self):
        sleep(1)
        balance = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[12]/grid-cell/div/span[2]/div/i/span[2]")
        Logging().reportDebugStep(self, "Get Balance: " + balance.text)
        return balance.text

    def get_local_time(self):
        sleep(1)
        local_time = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[11]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get Local Time: " + local_time.text)
        return local_time.text

    def get_created_by(self):
        sleep(1)
        created_by = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[10]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get Created By: " + created_by.text)
        return created_by.text

    def get_assigned_to(self):
        sleep(1)
        assigned_to = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[9]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get Assigned to: " + assigned_to.text)
        return assigned_to.text

    def get_country(self):
        sleep(1)
        country = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[8]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get Country: " + country.text)
        return country.text

    def get_account_status(self):
        sleep(1)
        account_status = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[7]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get Account Status: " + account_status.text)
        return account_status.text

    def check_pop_up_send_sms(self):
        sleep(1)
        try:
            title = super().wait_load_element("//span/h4")
        except:
            title = super().wait_load_element("(//div[@class='modal-body new-modal-body']/h3)[2]")
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
        Logging().reportDebugStep(self, "The Email module was opened")
        return MyDashboardPage(self.driver)

    def enter_subject_mail(self, subject):
        sleep(4)
        subject_mail = super().wait_load_element("//div[@class='modal-dialog modal-lg']//input[@id='subject']")
        subject_mail.send_keys(subject)
        Logging().reportDebugStep(self, "Enter Subject mail: " + subject)
        return MyDashboardPage(self.driver)

    def enter_body_mail(self, body):
        sleep(4)
        self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//iframe[@title='Rich Text Editor, editor2']"))
        enter_body_mail = self.driver.find_element(By.XPATH, "/html/body/p")
        enter_body_mail.click()
        self.driver.execute_script("arguments[0].textContent = arguments[1];", enter_body_mail, body)
        # enter_body_mail.send_keys(body)
        Logging().reportDebugStep(self, "Enter body mail: " + body)
        return MyDashboardPage(self.driver)

    def enter_cc_mail(self, cc_mail):
        self.driver.switch_to.default_content()
        sleep(3)
        subject_mail = super().wait_load_element("//div[@class = 'modal-dialog modal-lg']//input[@id='email_cc']")
        subject_mail.send_keys(cc_mail)
        Logging().reportDebugStep(self, "Enter cc mail: " + cc_mail)
        return MyDashboardPage(self.driver)

    def click_send(self):
        self.driver.switch_to.default_content()
        sleep(10)
        click_send = super().wait_load_element("(//button[text()=' Send '])[2]")
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
        select_show_all_tab = super().wait_load_element("//li[contains(text(), 'Show all')]", timeout=35)
        self.driver.execute_script("arguments[0].scrollIntoView();", select_show_all_tab)
        select_show_all_tab.click()
        self.wait_crm_loading_to_finish_tasks(75)
        Logging().reportDebugStep(self, "Select Show All tab")
        return MyDashboardPage(self.driver)

    def enter_account_name(self, testqa):
        sleep(3)
        input = super().wait_load_element("(//*[@id='host-element']/input)[1]", timeout=35)
        input.send_keys(testqa)
        self.wait_load_element("//div[@class='spinner']")
        self.wait_crm_loading_to_finish_tasks(95)
        Logging().reportDebugStep(self, "Enter account name: " + testqa)
        return MyDashboardPage(self.driver)

    def get_account_name(self):
        sleep(1)
        account_name = self.driver.find_element_by_xpath("//tr[2]/td[6]/grid-cell/div/span[2]/a")
        Logging().reportDebugStep(self, "Get account name: " + account_name.text)
        return account_name.text

    def click_pencil_icon(self):
        sleep(4)
        pencil_icon = self.driver.find_element_by_xpath("//tbody/tr[2]/td[18]/div[5]/div/span")
        pencil_icon.click()
        Logging().reportDebugStep(self, "Click pencil icon")
        return MyDashboardPage(self.driver)

    def get_status(self):
        sleep(1)
        get_status = self.driver.find_element_by_xpath(
            "//tbody/tr[2]/td[5]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get status: " + get_status.text)
        return get_status.text

    def get_type(self):
        sleep(1)
        get_type = self.driver.find_element_by_xpath(
            "//tbody/tr[2]/td[3]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get type: " + get_type.text)
        return get_type.text

    def get_time(self):
        sleep(1)
        get_time = self.driver.find_element_by_xpath(
            "//tbody/tr[2]/td[4]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get time: " + get_time.text)
        return get_time.text