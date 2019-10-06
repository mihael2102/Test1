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
        self.driver.find_element_by_xpath("//tr[contains(@class,'tableRow')]")
        Logging().reportDebugStep(self, "Your Tasks section contain records")
        return MyDashboardPage(self.driver)

    def check_client_segmentation_contains_record(self):
        sleep(2)
        self.driver.find_element_by_xpath(
            "((//table[contains(@class,'segmentation-body')]/tbody/tr[@class='ng-star-inserted']))[1]")
        Logging().reportDebugStep(self, "Client Segmentation section contain records")
        return MyDashboardPage(self.driver)

    def sort_by_status(self):
        sleep(3)
        sort_by_type = super().wait_load_element(
            "//a[@data-column-label='Status']")
        sort_by_type.click()
        self.wait_crm_loading_to_finish_tasks(165)
        Logging().reportDebugStep(self, "Sort by status")
        return MyDashboardPage(self.driver)

    def sort_by_type(self):
        sleep(3)
        sort_by_type = super().wait_load_element(
            "//a[@data-column-label='Event Type']")
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
            "(//button[@class='dropdown-toggle btn-block filter-button'])[6]",
            timeout=70)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "//input[@class='form-control ng-pristine ng-valid ng-touched']",
            timeout=10)
        input_account_name.send_keys(assigned_to)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "//input[@class='ng-star-inserted']",
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
        local_time_field = self.driver.find_element_by_xpath(
            "//input[@name='date_time_start_local']")
        local_time_field.click()
        local_time_field.send_keys(local_time)
        sleep(1)
        apply_btn = super().wait_element_to_be_clickable(
            "(//button[@class='applyBtn btn btn-sm btn-success' and text()='Apply'])[2]")
        apply_btn.click()
        sleep(5)
        Logging().reportDebugStep(self, "Enter local time: " + local_time)
        return MyDashboardPage(self.driver)

    def enter_created_by(self, created_by):
        sleep(3)
        created_by_field = super().wait_element_to_be_clickable(
            "(//button[@class='dropdown-toggle btn-block filter-button'])[5]",
            timeout=30)
        try:
            created_by_field.click()
        except:
            self.driver.execute_script("arguments[0].click();", created_by_field)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "//div[@class='input-group input-group-sm']/input[@placeholder='Search']",
            timeout=10)
        input_account_name.send_keys(created_by)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "//input[@class='ng-star-inserted']",
            timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter created by")
        return MyDashboardPage(self.driver)

    def enter_assigned_to(self, assigned_to):
        sleep(3)
        assign_to_field = super().wait_element_to_be_clickable(
            "(//button[@class='dropdown-toggle btn-block filter-button'])[4]",
            timeout=30)
        try:
            assign_to_field.click()
        except:
            self.driver.execute_script("arguments[0].click();", assign_to_field)
        sleep(2)
        input_assign_to = super().wait_element_to_be_clickable(
            "//div[@class='input-group input-group-sm']/input[@placeholder='Search']",
            timeout=10)
        input_assign_to.send_keys(assigned_to)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "//input[@class='ng-star-inserted']",
            timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter assigned to: " + assigned_to)
        return MyDashboardPage(self.driver)

    def enter_country(self, country):
        sleep(3)
        country_field = super().wait_element_to_be_clickable(
            "//span[@class='pull-left ng-star-inserted']",
            timeout=30)
        try:
            country_field.click()
        except:
            self.driver.execute_script("arguments[0].click();", country_field)
        sleep(2)
        input_country = super().wait_element_to_be_clickable(
            "//span[@class='filter-search-container']/input[@placeholder='Search...']",
            timeout=10)
        country_new = country.replace(' ', '')
        input_country.send_keys(country_new)
        self.wait_crm_loading_to_finish_tasks(35)
        check_box = super().wait_element_to_be_clickable(
            "//span[contains(text(), '%s')]" % country_new)
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        sleep(2)
        Logging().reportDebugStep(self, "Enter country: " + country)
        return MyDashboardPage(self.driver)

    def enter_account_status(self, status):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "(//button[@class='dropdown-toggle btn-block filter-button'])[3]",
            timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_status = super().wait_element_to_be_clickable(
            "//input[@class='form-control ng-pristine ng-valid ng-touched']",
            timeout=10)
        input_account_status.send_keys(status)
        sleep(20)
        check_box = super().wait_element_to_be_clickable(
            "//input[@class='ng-star-inserted']",
            timeout=30)
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Enter account status: " + status)
        return MyDashboardPage(self.driver)

    def enter_status(self, status):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "(//button[@class='dropdown-toggle btn-block filter-button'])[2]",
            timeout=30)
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_status = super().wait_element_to_be_clickable(
            "//div[@class='input-group input-group-sm']/input[@placeholder='Search']",
            timeout=10)
        input_status.send_keys(status)
        self.wait_crm_loading_to_finish_tasks(55)
        check_box = super().wait_element_to_be_clickable(
            "//input[@class='ng-star-inserted']",
            timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView();", check_box)
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        sleep(2)
        Logging().reportDebugStep(self, "Enter status: " + status)
        return MyDashboardPage(self.driver)

    def enter_event_type(self, event_type):
        btn_type = super().wait_element_to_be_clickable(
            "(//button[@class='dropdown-toggle btn-block filter-button'])[1]",
            timeout=30)
        btn_type.click()
        sleep(2)
        input_account_name = self.driver.find_element_by_xpath(
            "//div[@class='input-group input-group-sm']/input[@placeholder='Search']")
        input_account_name.click()
        input_account_name.send_keys(event_type)
        sleep(2)
        check_box = super().wait_element_to_be_clickable(
            "//input[@class='ng-star-inserted']",
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
            "(//span[@class='link_field'])[10]").text
        Logging().reportDebugStep(self, "Get Local time: " + local_time)
        return local_time

    def get_created_by(self):
        sleep(1)
        created_by = self.driver.find_element_by_xpath(
            "(//span[@class='link_field'])[9]").text
        Logging().reportDebugStep(self, "Get created by: " + created_by)
        return created_by

    def get_assigned_to(self):
        sleep(1)
        assigned_to = self.driver.find_element_by_xpath(
            "(//span[@class='link_field'])[8]").text
        Logging().reportDebugStep(self, "Get assigned to: " + assigned_to)
        return assigned_to

    def get_country(self):
        sleep(1)
        country = self.driver.find_element_by_xpath(
            "(//span[@class='link_field'])[7]").text
        Logging().reportDebugStep(self, "Get country: " + country)
        return country

    def get_account_status(self):
        sleep(5)
        account_status = self.driver.find_element_by_xpath(
            "/html/body/app-root/sales-dashboard-module/div/div[2]/div/tasks-list-wrapper/div/tasks-list/div/div/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[7]/grid-cell/div/span[2]")
        Logging().reportDebugStep(self, "Get account status: " + account_status.text)
        return account_status.text

    def check_pop_up_send_sms(self):
        sleep(5)
        try:
            title = super().wait_load_element("//span[@class='title']/h4[contains(text(),'Send SMS to')]")
        except:
            title = super().wait_load_element("(//div/h3[text()='Server Not Configured?'])[2]")
        Logging().reportDebugStep(self, title.text)
        return title.text

    def click_sms_icon(self):
        sleep(3)
        first_check_box = super().wait_load_element(
            "(//span[contains(@class, 'glyphicon glyphicon-transfer cursor-pointer ng-star-inserted')])[1]")
        first_check_box.click()
        Logging().reportDebugStep(self, "Click SMS icon")
        return MyDashboardPage(self.driver)

    def open_email_actions_section(self):
        sleep(3)
        first_check_box = super().wait_load_element(
            "(//span[contains(@class, 'glyphicon glyphicon-envelope cursor-pointer ng-star-inserted')])[1]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The email module was opened")
        return MyDashboardPage(self.driver)

    def enter_subject_mail(self, subject):
        sleep(4)
        subject_mail = super().wait_load_element("//div[@class='modal-dialog modal-lg']//input[@id='subject']")
        subject_mail.send_keys(subject)
        Logging().reportDebugStep(self, "Enter subject mail: " + subject)
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
        sleep(3)
        click_send = super().wait_load_element("(//button[text()=' Send '])[2]")
        click_send.click()
        try:
            self.wait_element_to_be_disappear("(//button[text()=' Send '])[2]", timeout=35)
            Logging().reportDebugStep(self, "Click Send")
        except:
            Logging().reportDebugStep(self, "There is no Send mails function")
        return MyDashboardPage(self.driver)

    def select_show_all_tab(self):
        self.wait_crm_loading_to_finish_tasks(85)
        select_show_all_tab = self.driver.find_element_by_xpath(
            "//*[@id='main-tabs']/li[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", select_show_all_tab)
        try:
            select_show_all_tab.click()
        except:
            self.driver.execute_script("arguments[0].click();", select_show_all_tab)
        sleep(2)
        self.wait_crm_loading_to_finish_tasks(75)
        Logging().reportDebugStep(self, "Select Show All tab")
        return MyDashboardPage(self.driver)

    def enter_account_name(self, testqa):
        sleep(1)
        self.perform_scroll_down()
        sleep(0.5)
        input = super().wait_load_element("//*[@id='host-element']/input")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        sleep(1)
        input.send_keys(testqa)
        sleep(1)
        try:
            self.wait_load_element("//div[@class='spinner']", 55)
        except(NoSuchElementException, TimeoutException):
            pass
        self.wait_crm_loading_to_finish_tasks(75)
        sleep(1)
        Logging().reportDebugStep(self, "Enter account name: " + testqa)
        return MyDashboardPage(self.driver)

    def get_account_name(self):
        sleep(1)
        account_name = self.driver.find_element_by_xpath("(//a[contains(text(),'testqa')])[1]").text
        Logging().reportDebugStep(self, "Get account name: " + account_name)
        return account_name

    def click_pencil_icon(self):
        sleep(4)
        pencil_icon = self.driver.find_element_by_xpath("(//span[contains(@class, 'pencil')])[1]")
        pencil_icon.click()
        Logging().reportDebugStep(self, "Click pencil icon")
        return MyDashboardPage(self.driver)

    def get_status(self):
        sleep(1)
        get_status = self.driver.find_element_by_xpath("(//span[@class='link_field'])[4]").text
        Logging().reportDebugStep(self, "Get status: " + get_status)
        return get_status

    def get_event_type(self):
        sleep(1)
        get_type = self.driver.find_element_by_xpath("(//span[@class='link_field'])[2]").text
        Logging().reportDebugStep(self, "Get type: " + get_type)
        return get_type

    def get_time(self):
        sleep(5)
        get_time = self.driver.find_element_by_xpath("(//span[@class='link_field' and contains(text(),':')])[2]").text
        Logging().reportDebugStep(self, "Get Local Time: " + get_time)
        return get_time