from time import sleep
import poplib
from email import parser
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.modules.tasks_module.SendEmailModuleActions import SendEmailModuleActions
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.tasks_module.AddEventModule import AddEventModule
from src.main.python.ui.crm.model.modules.tasks_module.CalendarViewModule import CalendarViewModule
from src.main.python.ui.crm.model.modules.tasks_module.CallModule import PhoneActionsModule
from src.main.python.ui.crm.model.modules.tasks_module.EditEventModule import EditEventModule
from src.main.python.ui.crm.model.modules.tasks_module.MassEditTaskModule import MassEditTaskModule
from src.main.python.ui.crm.model.modules.tasks_module.MassEmailModule import MassEmailModule
from src.main.python.ui.crm.model.modules.tasks_module.MassSMSModule import MassSMSModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from datetime import *
import allure
from src.main.python.utils.config import Config
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class TasksPage(CRMBasePage):

    '''
        Open the second tabs of crm page
        :parameter url crm page url  
    '''

    def open_second_tab_page(self, url):
        super().open_second_tab_page(url)
        Logging().reportDebugStep(self, "Open second tabs page: " + url + '\n')
        return TasksPage()

    ''' 
          Open the task module 
          return Help Desk instance
      '''


    def get_third_column_frow_text(self):
        column_text = super().wait_load_element("//tr[2]/td[6]/grid-cell/div/span/a")
        Logging().reportDebugStep(self, "Returns first column text: " + column_text.text)
        return column_text.text

    def get_third_column_srow_text(self):
        column_text = super().wait_load_element("//tr[2]/td[14]/span")
        Logging().reportDebugStep(self, "Returns second column text: " + column_text.text)
        return column_text.text

    def click_column_title(self, column):
        sleep(1)
        task_module = super().wait_load_element("//a[contains(text(), '%s')]" % column)
        task_module.click()
        self.wait_crm_loading_to_finish_tasks(155)
        Logging().reportDebugStep(self, "Click " + column + " column title")
        return TasksPage(self.driver)

    def get_second_column_frow_text(self):
        sleep(10)
        column_text = super().wait_load_element("//tr[2]/td[5]/grid-cell/div/span[@class='link_field']")
        Logging().reportDebugStep(self, "Returns first column text: " + column_text.text)
        return column_text.text

    def get_second_column_srow_text(self):
        column_text = super().wait_load_element("//tr[2]/td[3]/div/a")
        Logging().reportDebugStep(self, "Returns second column text: " + column_text.text)
        return column_text.text

    def get_first_column_frow_text(self):
        sleep(10)
        column_text = super().wait_load_element("//tr[2]/td[3]/grid-cell/div/span[@class='link_field']")
        Logging().reportDebugStep(self, "Returns first column text: " + column_text.text)
        return column_text.text

    def get_first_column_srow_text(self):
        column_text = super().wait_load_element("//tr[2]/td[2]/div/a")
        Logging().reportDebugStep(self, "Returns second column text: " + column_text.text)
        return column_text.text

    def open_task_module(self):
        task_module = super().wait_load_element("//span[@class='glyphicon glyphicon-Tasks']")
        task_module.click()
        Logging().reportDebugStep(self, "Task module is opened")
        return TasksPage(self.driver)

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return TasksPage(self.driver)

    def get_show_all_tab_text(self):
        super().wait_load_element("//ul[@id='main-tabs']//li[1]")
        tab = self.driver.find_element(By.XPATH, "//ul[@id='main-tabs']//li[1]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[1]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_show_mine_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[2]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[2]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_today_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[3]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[3]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_this_week_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[4]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[4]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def open_show_mine_tab(self):
        sleep(2)
        tab = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[2]")
        tab.click()
        self.wait_crm_loading_to_finish()
        Logging().reportDebugStep(self, "The mine tab was opened ")
        return TasksPage(self.driver)

    def open_show_all_tab(self):
        sleep(2)
        tab = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[1]")
        tab.click()
        self.wait_crm_loading_to_finish()
        sleep(2)
        Logging().reportDebugStep(self, "The all tab was opened ")
        return TasksPage(self.driver)

    def open_sms_actions_section(self):
        sleep(6)
        try:
            first_check_box = super().wait_element_to_be_clickable(
                "//tr[@class='tableRow ng-star-inserted'][1]/td[@class='grid-actions-cell ng-star-inserted last-col col-pinned-right']/div[2]")
        except:
            first_check_box = super().wait_element_to_be_clickable(
                "/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[18]/div[2]/div/span/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[18]/div[2]/div/span")
        first_check_box.click()
        Logging().reportDebugStep(self, "The sms module was opened")
        return TasksPage(self.driver)

    def check_pop_up_send_sms(self):
        sleep(5)
        try:
            title = super().wait_load_element("/html/body/bs-modal[12]/div/div/div/div[2]/div[1]/div/span/h4")

        except:
            title = super().wait_load_element("/html/body/bs-modal[12]/div/div/div/div[2]/h3")
        Logging().reportDebugStep(self, title.text)
        return title.text

    def enter_body_mail(self, body):
        sleep(4)
        self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//*[@id='cke_1_contents']/iframe"))
        enter_body_mail = self.driver.find_element(By.XPATH, "/html/body/p")
        enter_body_mail.click()
        self.driver.execute_script("arguments[0].textContent = arguments[1];", enter_body_mail, body)
        # enter_body_mail.send_keys(body)
        Logging().reportDebugStep(self, "Enter body mail")
        return TasksPage(self.driver)

    def open_email_actions_section(self):
        sleep(3)

        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow ng-star-inserted'][1]/td[@class='grid-actions-cell ng-star-inserted last-col col-pinned-right']/div[1]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The email module was opened")
        return TasksPage(self.driver)

    def open_mass_edit_task(self):
        mass_edit_module = super().wait_element_to_be_clickable("//button[contains(text(),'Mass Edit')]")
        mass_edit_module.click()
        Logging().reportDebugStep(self, "The mass edit module was opened")
        return MassEditTaskModule(self.driver)

    def open_mass_email_task_module(self):
        mass_email_module = super().wait_element_to_be_clickable("//button[contains(text(),'Mass Email')]")
        mass_email_module.click()
        Logging().reportDebugStep(self, "The mass email module was opened")
        return MassEmailModule(self.driver)

    def get_history_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[5]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[5]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def open_add_event_module(self):
        sleep(3)
        event_button = self.driver.find_element(By.XPATH,"//button[contains(text(),'Add Event')]")
        self.driver.execute_script("arguments[0].click();", event_button)
        # event_button.click()
        Logging().reportDebugStep(self, "The event  module was opened")
        return AddEventModule(self.driver)

    def open_calendar_view_module(self):
        self.wait_element_to_be_clickable("//button[contains(text(),'Calendar View')]")
        calendar_view_button = self.driver.find_element(By.XPATH,
                                                        "//button[contains(text(),'Calendar View')]")
        self.driver.execute_script("arguments[0].click();", calendar_view_button)
        # calendar_view_button.click()
        Logging().reportDebugStep(self, "The calendar view module was opened")
        return CalendarViewModule(self.driver)

    def select_three_records_task_module(self):
        sleep(1)
        first_check_box = super().wait_element_to_be_clickable("//tr[@class='tableRow'][1]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//tr[@class='tableRow'][2]//td[1]")
        second_check_box.click()
        third_check_box = self.driver.find_element(By.XPATH, "//tr[@class='tableRow'][3]//td[1]")
        third_check_box.click()
        Logging().reportDebugStep(self, "The records were selected")
        return TasksPage(self.driver)

    def select_two_records_task_module(self):
        first_check_box = super().wait_element_to_be_clickable("//tr[@class='tableRow'][1]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//tr[@class='tableRow'][2]//td[1]")
        second_check_box.click()
        return TasksPage(self.driver)

    def perform_mass_delete(self):
        sleep(3)
        delete_button = super().wait_element_to_be_clickable("//button[contains(text(),'Mass Delete')]")
        delete_button.click()
        delete_button = super().wait_element_to_be_clickable(
            "//div[@class='modal-footer new-modal-footer']//button[contains(text(),'OK')]")
        delete_button.click()
        Logging().reportDebugStep(self, "The mass delete was performed")
        return TasksPage(self.driver)

    def open_mass_sms_module(self):
        event_button = self.driver.find_element(By.XPATH,
                                                "//button[contains(text(),'Mass SMS')]")
        event_button.click()
        Logging().reportDebugStep(self, "The event  module was opened ")
        return MassSMSModule(self.driver)

    '''
           Returns a task was_updated  message if the user entered a valid password
    '''

    def get_confirm_message_task_module(self):
        sleep(2)
        task_was_created_text = super().wait_load_element("//div[contains(text(),'Task was created')]").text
        # confirm_message = super().wait_load_element("//div[@class='toast-message']")
        Logging().reportDebugStep(self, "Returns the message task  : " + task_was_created_text)
        return task_was_created_text

    def get_task_subject(self, subject):
        sleep(3)
        task_subject = self.driver.find_element(By.XPATH, "//a//div[contains(text(),'%s')]" % subject)
        task_subject.click()
        Logging().reportDebugStep(self, "Returns the subject task  : " + task_subject.text)
        return task_subject.text

    def click_pencil_button(self):
        sleep(3)
        pencil_button = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow'][1]//span[@class='glyphicon glyphicon-pencil cursor-pointer']")
        pencil_button.click()
        Logging().reportDebugStep(self, "Click the record by pencil button")
        return EditEventModule(self.driver)

    def click_ok(self):
        super().click_ok()
        Logging().reportDebugStep(self, "Message sent successfully")
        return MassSMSModule(self.driver)

    def open_first_client_profile(self):
        sleep(3)
        client_link = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow']//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The first client profile is opened")
        return ClientProfilePage(self.driver)

    def open_second_client_profile(self):
        sleep(3)
        client_link = super().wait_element_to_be_clickable(
            "//div[@class='table-grid-container']//tr[4]//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The second client profile was opened ")
        return ClientProfilePage(self.driver)

    def open_third_client_profile(self):
        sleep(3)
        client_link = super().wait_element_to_be_clickable(
            "//div[@class='table-grid-container']//tr[5]//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The third client profile was opened ")
        return ClientProfilePage(self.driver)

    def perform_screen_shot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/tasks_module/tasks_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('passed_screenshot', self.driver.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return CalendarViewModule(self.driver)

    def find_event_by_subject(self, subject):
        sleep(2)
        # for_old_forex
        self.driver.execute_script("window.scrollTo(0, document.body.scrollWeight);")
        subject_button = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["subject_button"])
        subject_button.click()
        subject_field = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["subject_field"])
        subject_field.clear()
        sleep(5)
        subject_field.send_keys(subject)
        Logging().reportDebugStep(self, "The subject was set: " + subject)
        sleep(3)
        Logging().reportDebugStep(self, "The subject was set: " + subject)
        event_type = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["event_type"])
        event_type.click()
        title = super().wait_element_to_be_clickable("/html/body/app-root/tasks-list/div/div[1]/div/button-block/div[1]/h3")
        # title.click()
        self.driver.execute_script("arguments[0].click();", title)

        return TasksPage(self.driver)

    def open_phone_actions(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow'][1]//div[3]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The call phone module was opened: ")
        return PhoneActionsModule(self.driver)

    def perform_searching(self, first_name, last_name):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_first_name(first_name)
        self.enter_first_name(first_name)
        self.enter_first_name(first_name)
        self.enter_first_name(first_name)
        return TasksPage(self.driver)

    def clear_filter(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableHeader']//td[1]//input")
        Logging().reportDebugStep(self, "Clear filter was performed")
        first_check_box.click()
        return TasksPage(self.driver)

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_firstname']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "The first name was entered : " + first_name)
        return TasksPage(self.driver)

    def enter_last_name(self, last_name):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_firstname']")
        first_name_field.clear()
        first_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The first name was entered : " + last_name)
        return TasksPage(self.driver)

    def get_results_count(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        refresh_icon = self.driver.find_element(By.XPATH, "//a[@class='fa fa-refresh']")
        self.driver.execute_script("arguments[0].click();", refresh_icon)
        # refresh_icon.click()
        sleep(8)
        result_count_xpath = "//*[contains(text(), 'Showing Records')]"
        self.wait_visible_of_element(result_count_xpath)
        results_count_text = self.driver.find_elements(By.XPATH, result_count_xpath)[0].text
        Logging().reportDebugStep(self, "Results found text: %s" % results_count_text)
        results_split = results_count_text.split(" ")
        result_count = int(results_split[len(results_split) - 1])
        Logging().reportDebugStep(self, "Got %d search results" % result_count)
        return result_count


    def enter_subject_mail(self, subject):
        sleep(4)
        subject_mail = super().wait_load_element("//input[@id='subject']")
        subject_mail.send_keys(subject)
        Logging().reportDebugStep(self, "Enter subject mail" + subject)
        return TasksPage(self.driver)

    def enter_cc_mail(self, cc_mail):
        self.driver.switch_to.default_content()
        sleep(3)
        subject_mail = super().wait_load_element("//*[@id='email_cc']")
        subject_mail.send_keys(cc_mail)
        Logging().reportDebugStep(self, "Enter cc mail" + cc_mail)
        return TasksPage(self.driver)

    def click_send(self):
        self.driver.switch_to.default_content()
        sleep(10)
        click_send = super().wait_load_element("/html/body/bs-modal[7]/div/div/div/div[3]/span/button[4]")
        click_send.click()
        Logging().reportDebugStep(self, "Click Send")
        return TasksPage(self.driver)

    def check_email(self, subject):
        sleep(10)
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user('jonathan.albalak@pandats.com')
        pop_conn.pass_('xUQ7hrr9VF')
        # Get messages from server:
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        # Concat message pieces:
        messages = ["\n".join(m.decode() for m in mssg[1]) for mssg in messages]
        # Parse message intom an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        for message in messages:
            if str(message['subject']) == subject:
                Logging().reportDebugStep(self, str(message['subject']))
                return str(message['subject'])
        pop_conn.quit()

    def get_first_account_name(self):
        sleep(10)
        account_name = super().wait_load_element("/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[6]/grid-cell/div/span[2]/a").text
        Logging().reportDebugStep(self, "Check Account name" + account_name)
        return account_name

    def search_account_name(self, first_name):
        input_account_name = super().wait_element_to_be_clickable("//*[@id='host-element']/input", timeout=10)
        input_account_name.send_keys(first_name)
        sleep(5)
        self.wait_crm_loading_to_finish_tasks(85)
        Logging().reportDebugStep(self, "Search Account name")
        return TasksPage(self.driver)

    def search_by_type(self, type):
        btn_type = super().wait_element_to_be_clickable("//td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button")
        btn_type.click()
        sleep(30)
        input_account_name = super().wait_element_to_be_clickable("/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input", timeout=10)
        input_account_name.send_keys(type)
        sleep(2)
        check_box = super().wait_element_to_be_clickable("//ss-multiselect-dropdown/div/ul/li[5]/a/input")
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Search by Type")
        return TasksPage(self.driver)

    def search_by_status(self, status):
        sleep(3)
        btn_status = super().wait_element_to_be_clickable(
            "/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/button")
        try:
            btn_status.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_status)
        sleep(2)
        input_account_name = super().wait_element_to_be_clickable(
            "/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[1]/div/input",
            timeout=10)
        input_account_name.send_keys(status)
        sleep(2)
        check_box = super().wait_element_to_be_clickable("/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/filters-factory/multiple-select-bs-filter/filter-multiple-select-bs/div/ss-multiselect-dropdown/div/ul/li[5]/a/input")
        check_box.click()
        sleep(2)
        Logging().reportDebugStep(self, "Search by status")
        return TasksPage(self.driver)


    def get_first_type(self):
        sleep(3)
        first_type = super().wait_load_element(
            "/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[3]/grid-cell/div/span[2]").text
        Logging().reportDebugStep(self, "Check Type" + first_type)
        return first_type

    def get_first_status(self):
        sleep(3)
        first_status = super().wait_load_element(
            "/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/tbody/tr[2]/td[5]/grid-cell/div/span[2]").text
        Logging().reportDebugStep(self, "Check status" + first_status)
        return first_status

    def select_all_event(self):
        check_box = super().wait_load_element("/html/body/app-root/tasks-list/div/div[2]/div/grid/div[2]/div/div[1]/table/thead/tr/th[1]/input")
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        Logging().reportDebugStep(self, "Select all event")
        return TasksPage(self.driver)


    def get_account_name(self, first_name):
        sleep(2)
        search_account_name_text = super().wait_load_element("//a[contains(text(),'%s')]" % first_name).text
        return search_account_name_text

    def open_edit_event(self):
        pencil_button = self.driver.find_element(By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["edit_event"])
        self.driver.execute_script("arguments[0].click();", pencil_button)
        Logging().reportDebugStep(self, "Edit popup was opened")
        return EditEventModule(self.driver)

    def task_was_updated(self):
        sleep(0.5)
        task_was_updated_text = super().wait_load_element("//div[contains(text(),'Task was updated')]").text
        Logging().reportDebugStep(self, "Text from 'Update' popup has been got: " + task_was_updated_text)
        return task_was_updated_text

    def Sign_Out(self):
        CRMBasePage(self.driver).refresh_page()
        sleep(2)
        user = super().wait_element_to_be_clickable("//*[@id='bs-example-navbar-collapse-1']/ul[2]/li[3]/a/img")
        # self.driver.execute_script("arguments[0].click();", user)
        user.click()
        sleep(2)
        sign_out = super().wait_element_to_be_clickable("//a[contains(text(), 'Sign Out')]")
        self.driver.execute_script("arguments[0].click();", sign_out)
        Logging().reportDebugStep(self, "Sign Out")
        return TasksPage(self.driver)


