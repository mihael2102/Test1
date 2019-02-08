from time import sleep
from datetime import *
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.modules.leads_module.MassAssignLeadModule import MassAssignLeadModule
from src.main.python.ui.crm.model.modules.leads_module.MassEditLeadModule import MassEditLeadModule
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.ui.crm.model.pages.leads.ImportLeadPage import ImportLeadPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.waitting_utils.WaitingUtils import WaitingUtils


class LeadsModule(CRMBasePage):

    def perform_searching_lead_module(self, first_name, last_name, email, assigned_to, tittle, lead_source, lead_status,
                                      language):
        self.wait_element_to_be_clickable("//td[@class='txt_al_c']")
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        # self.enter_assigned_to(assigned_to)
        # self.enter_tittle(tittle)
        # self.enter_lead_source(lead_source)
        # self.enter_lead_status(lead_status)
        # self.enter_language(language)
        self.click_search_button_leads_module()
        self.wait_crm_loading_to_finish()
        return LeadsModule()

    def open_create_lead_module(self):
        task_module = super().wait_load_element("//td[@class='moduleName']//button[1]")
        task_module.click()
        Logging().reportDebugStep(self, "Create leads module is opened")
        return CreateLeadsProfilePage(self.driver)

    def open_create_filter_pop_up(self):
        filter_button = super().wait_element_to_be_clickable("//a[@title='Create Filter']")
        filter_button.click()
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterPage(self.driver)

    def open_import_page(self):
        import_page = super().wait_element_to_be_clickable("//button[@title='Import Leads']")
        import_page.click()
        Logging().reportDebugStep(self, "The import_page was opened")
        return ImportLeadPage(self.driver)

    def open_today_lead_tab(self):
        today_lead_tab = super().wait_element_to_be_clickable("//li[contains(text(),'Today Leads')]")
        today_lead_tab.click()
        Logging().reportDebugStep(self, "The today tab was opened")
        return LeadsModule(self.driver)

    def get_import_lead(self, last_name_lead):
        WaitingUtils().wait_util_element_is_displayed(last_name_lead, self.driver)
        return LeadsModule(self.driver)

    '''
         Returns a confirmation  message if the user entered a valid password
    '''

    def get_confirm_message_lead_module(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns a confirmation message: " + confirm_message.text)
        return confirm_message.text

    def select_three_records_task_module(self):
        sleep(1)
        first_check_box = super().wait_element_to_be_clickable("//tbody[@id='listBody']//tr[1]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[2]//td[1]")
        second_check_box.click()
        third_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[3]//td[1]")
        third_check_box.click()
        Logging().reportDebugStep(self, "The records were selected")
        return LeadsModule(self.driver)

    ''' 
           Select the filter in drop-down   
          :parameter test_filter the filter that is created in the filters drop down
          :return Home Page instance
       '''

    def select_filter(self, test_filter):
        drop_down_filter = super().wait_load_element("//span[@class='filter-option pull-left']")
        drop_down_filter.click()
        Logging().reportDebugStep(self, "Click the  drop down filter ")
        field_found = self.driver.find_element(By.XPATH, "//input[@class='input-block-level form-control']")
        field_found.clear()
        field_found.send_keys(test_filter)
        Logging().reportDebugStep(self, "The field found is : " + test_filter)
        select_test_filter = self.driver.find_element(By.XPATH, "//a/span[contains(., '%s')]" % test_filter)
        select_test_filter.click()
        sleep(10)
        sleep(10)
        Logging().reportDebugStep(self, "Click the selected filter")
        self.wait_crm_loading_to_finish()
        return LeadsModule(self.driver)

    def open_mass_edit_task(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass Edit']")
        mass_edit_module.click()
        return MassEditLeadModule(self.driver)

    def open_mass_assign_lead_module(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass assign']")
        mass_edit_module.click()
        return MassAssignLeadModule(self.driver)

    '''
            Returns a task was_updated  message if the user entered a valid password
     '''

    def get_message_lead_module(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns the message task  : " + confirm_message.text)
        return confirm_message.text

    def click_ok(self):
        super().click_ok()
        return LeadsModule(self.driver)

    def perform_screen_shot_lead_module(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/leads_module/leads_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return LeadsModule(self.driver)

    def perform_screen_shot_import_lead_module(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/leads_module/leads_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed,the grid with leads is empty ")
        return LeadsModule(self.driver)

    def perform_screen_shot_confirm_import_lead_module(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/leads_module/leads_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed,the lead is displayed")
        return LeadsModule(self.driver)

    def select_leads(self):
        select_lead_check_box = super().wait_element_to_be_clickable("//td[@class='lvtCol']//input")
        select_lead_check_box.click()
        Logging().reportDebugStep(self, "All imported leads were selected")
        return LeadsModule(self.driver)

    def click_delete_button(self):
        delete_lead_check_box = super().wait_element_to_be_clickable("//input[@value='Delete']")
        delete_lead_check_box.click()
        allert = self.driver.switch_to_alert()
        allert.accept()
        Logging().reportDebugStep(self, "All imported leads were deleted")
        return LeadsModule(self.driver)

    def delete_filter_lead_module(self):
        delete_filter_button = super().wait_element_to_be_clickable("//a[@title='Delete']")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "The delete button was clicked")
        return LeadsModule(self.driver)

    def confirm_delete_lead_module(self):
        delete_filter_button = super().wait_element_to_be_clickable("//button[contains(text(),'OK')]")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "Three lead were deleted")
        return LeadsModule(self.driver)

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_firstname']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "The first name was entered : " + first_name)
        return LeadsModule(self.driver)

    def enter_last_name(self, last_name):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_lastname']")
        first_name_field.clear()
        first_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The last name was entered : " + last_name)
        return LeadsModule(self.driver)

    def enter_email(self, email):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_email']")
        first_name_field.clear()
        first_name_field.send_keys(email)
        Logging().reportDebugStep(self, "The email was entered : " + email)
        return LeadsModule(self.driver)

    def enter_assigned_to(self, assigned_to):
        country_drop_down = self.driver.find_element(By.XPATH,
                                                     "//tr[@id='customAdvanceSearch']//td[5]//span[@class='multiselect-selected-text']")

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[5]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(assigned_to)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % assigned_to)
        country_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The brand  was selected : " + assigned_to)
        return LeadsModule(self.driver)

    def enter_tittle(self, tittle):
        tittle_name_field = self.driver.find_element(By.XPATH,
                                                     "//tr[@name='customAdvanceSearch']//input[@id='tks_designation']")
        tittle_name_field.clear()
        tittle_name_field.send_keys(tittle)
        Logging().reportDebugStep(self, "The assigned_to was entered : " + tittle)
        return LeadsModule(self.driver)

    def enter_lead_source(self, lead_source):
        lead_source_drop_down = self.driver.find_element(By.XPATH,
                                                         "//tr[@id='customAdvanceSearch']//td[7]//span[@class='multiselect-selected-text']")

        lead_source_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[7]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(lead_source)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % lead_source)
        country_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The brand  was selected : " + lead_source)
        return LeadsModule(self.driver)

    def enter_lead_status(self, lead_status):
        lead_source_drop_down = self.driver.find_element(By.XPATH,
                                                         "//tr[@id='customAdvanceSearch']//td[8]//span[@class='multiselect-selected-text']")

        lead_source_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[8]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(lead_status)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % lead_status)
        country_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The lead_status  was selected : " + lead_status)
        return LeadsModule(self.driver)

    def enter_language(self, language):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_cf_1092']")
        first_name_field.clear()
        first_name_field.send_keys(language)
        Logging().reportDebugStep(self, "The language was entered : " + language)
        return LeadsModule(self.driver)

    def click_search_button_leads_module(self):
        search_button = super().wait_element_to_be_clickable("//td[@class='txt_al_c']")
        search_button.click()
        Logging().reportDebugStep(self, "The search button was clicked ")
        return LeadsModule(self.driver)

    def get_results_count(self):
        refresh_icon = self.driver.find_elements(By.XPATH, "//span[@class='fa fa-refresh']")[0]
        refresh_icon.click()
        result_count_xpath = "//*[contains(text(), 'Showing Records')]"
        self.wait_visible_of_element(result_count_xpath)
        results_count_text = self.driver.find_elements(By.XPATH, result_count_xpath)[0].text
        results_split = results_count_text.split(" ")
        result_count = int(results_split[len(results_split) - 1])
        return result_count

    def get_first_name_column(self):
        name_first_column = super().wait_element_to_be_clickable(
            "//table[@id='resizeble_cols']//td[2]")
        Logging().reportDebugStep(self, "First column name  : " + name_first_column.text)
        return name_first_column.text

    def get_second_name_column(self):
        name_second_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[3]")
        Logging().reportDebugStep(self, "Second column name: " + name_second_column.text)
        return name_second_column.text

    def get_third_name_column(self):
        name_third_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[4]")
        Logging().reportDebugStep(self, "Third column name: " + name_third_column.text)
        return name_third_column.text

    def get_fourth_name_column(self):
        name_fourth_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[5]")
        Logging().reportDebugStep(self, "Fourth column name : " + name_fourth_column.text)
        return name_fourth_column.text

    def get_fifth_name_column(self):
        name_fifth_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[6]")
        Logging().reportDebugStep(self, "Fifth column name : " + name_fifth_column.text)
        return name_fifth_column.text

    def get_sixth_name_column(self):
        name_sixth_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[7]")
        Logging().reportDebugStep(self, "Sixth column name : " + name_sixth_column.text)
        return name_sixth_column.text

    def get_seventh_name_column(self):
        name_seventh_column = self.driver.find_element(By.XPATH,
                                                       "//table[@id='resizeble_cols']//td[8]")
        Logging().reportDebugStep(self, "Seventh column name : " + name_seventh_column.text)
        return name_seventh_column.text

    def get_eighth_name_column(self):
        name_eighth_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[9]")
        Logging().reportDebugStep(self, "Seventh column name : " + name_eighth_column.text)
        return name_eighth_column.text