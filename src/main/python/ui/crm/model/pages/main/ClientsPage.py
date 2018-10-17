from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.client_modules.mass_sms.SendSMSClientsModule import SendSMSClientsModule
from src.main.python.ui.crm.model.modules.client_modules.send_email.SendEmailClientsModule import SendEmailClientsModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.client_modules.mass_assign.MassAssignClientsModule import \
    MassAssignClientsModule
from src.main.python.ui.crm.model.modules.client_modules.mass_edit.MassEditClientsModule import MassEditClientsModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config


class ClientsPage(CRMBasePage):

    def perform_searching(self, client_status, email, country):
        if client_status:
            self.select_client_status(client_status)
        if email:
            self.enter_email(email)
        # if name:
        #     self.enter_client_name(name)
        if country:
            self.enter_country(country)

        # if brand:
        #     self.select_brand(brand)
        self.click_search_button()
        return ClientsPage(self.driver)

    def perform_searching_by_email(self, email):
        self.enter_email(email)
        return ClientsPage(self.driver)

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
        select_test_filter = self.driver.find_element(By.XPATH, "//span[contains(text(),'%s')]" % test_filter)
        select_test_filter.click()
        Logging().reportDebugStep(self, "Click the selected filter")
        self.wait_crm_loading_to_finish()
        return ClientsPage(self.driver)

    def clear_filter(self):
        filter_lear = super().wait_element_to_be_clickable("//a[@id='clearFilter']")
        filter_lear.click()
        return ClientsPage(self.driver)

    def open_client_module_clients_module(self):
        home_page_element = super().wait_element_to_be_clickable("//span[@class='glyphicon glyphicon-Clients']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The client module was opened")
        return ClientsPage(self.driver)

    def open_all_tab_clients_module(self):
        all_tab = super().wait_element_to_be_clickable("//li[contains(text(),'All')]")
        all_tab.click()
        Logging().reportDebugStep(self, "The client module was opened")
        return ClientsPage(self.driver)

    ''' 
         Select the filter in drop-down   
         :parameter email the email of exist user
         :parameter password the password of exist user
         :return Client Profile Page instance
    '''

    def find_client_by_email(self, email):
        sleep(2)
        email_field = super().wait_load_element("//input[@id='tks_email1']")
        email_field.send_keys(email)
        Logging().reportDebugStep(self, "Setting  the user's email in the email field  is : " + email)
        search_button = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        search_button.click()
        Logging().reportDebugStep(self, "Click the search button ")
        sleep(2)
        # client_id = super().wait_element_to_be_clickable("//tr[@class='lvtColData']//div[@class='link_field']")
        # client_id.click()
        client_id = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["id_client"])
        self.driver.execute_script("arguments[0].click();", client_id)
        Logging().reportDebugStep(self, "Click user email: " + email)
        return ClientProfilePage(self.driver)

    '''
         Select the crm page again
         return  Home Page instance 
    '''

    def switch_second_tab_page(self):
        super().switch_second_tab_page()
        Logging().reportDebugStep(self, "switch the second tab ")
        return ClientsPage(self.driver)

    ''' 
        Open the help desk module 
        return Help Desk instance  
    '''

    def open_help_desk_module(self):
        help_desc_module = super().wait_load_element("//a[contains(text(), 'Help Desk')]")
        help_desc_module.click()
        Logging().reportDebugStep(self, "Open  the help desk module ")
        return HelpDeskPage(self.driver)

    def refresh(self):
        self.driver.refresh()
        Logging().reportDebugStep(self, "Perform the refresh ")
        return ClientsPage(self.driver)

    def enter_email(self, email):
        sleep(2)
        email_field = super().wait_load_element("//input[@id='tks_email1']")
        email_field.clear()
        email_field.send_keys(email)
        Logging().reportDebugStep(self, "Email was entered : " + email)
        return ClientsPage(self.driver)

    def enter_client_name(self, name):
        client_name = self.driver.find_element(By.XPATH, "//input[@name='tks_accountname']")
        client_name.send_keys(name)
        Logging().reportDebugStep(self, "The client name was entered : " + name)
        return ClientsPage(self.driver)

    def enter_country(self, country):
        country_drop_down = self.driver.find_element(By.XPATH,
                                                     "//*[@id='customAdvanceSearch']/td[6]/div/div[1]/button")
        # for_old_forex

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//*[@id='customAdvanceSearch']/td[6]/div/div[1]/ul/li[1]/div/input")
        # for_old_forex
        search_field.clear()
        search_field.send_keys(country)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % country)
        # country_choice.click()
        self.driver.execute_script("arguments[0].click();", country_choice)
        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The country was entered : " + country)

        return ClientsPage(self.driver)

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(By.XPATH, "//input[@name='tks_firstname']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "The first name  was entered : " + first_name)
        return ClientsPage(self.driver)

    def enter_last_name(self, last_name):
        first_name_field = self.driver.find_element(By.XPATH, "//input[@name='tks_lastname']")
        first_name_field.clear()
        first_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The last name  was entered : " + last_name)
        return ClientsPage(self.driver)

    def enter_city(self, city):
        city_field = self.driver.find_element(By.XPATH, "//input[@name='tks_city']")
        city_field.clear()
        city_field.send_keys(city)
        Logging().reportDebugStep(self, "The city  was entered : " + city)
        return ClientsPage(self.driver)

    def select_brand(self, brand):
        country_drop_down = self.driver.find_element(By.XPATH,
                                                     "//tr[@id='customAdvanceSearch']//td[12]//span[@class='multiselect-selected-text']")

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[12]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(brand)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % brand)
        country_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The brand  was selected : " + brand)
        return ClientsPage(self.driver)

    def select_client_status(self, client_status):
        sleep(3)
        # for_old_forex
        country_drop_down = super().wait_load_element(
            "//*[@id='customAdvanceSearch']/td[4]/div/div[1]/button")

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//*[@id='customAdvanceSearch']/td[4]/div/div[1]/ul/li[1]/div/input")
        # for_old_forex
        search_field.clear()
        search_field.send_keys(client_status)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % client_status)
        # for_old_forex
        # country_choice.click()
        self.driver.execute_script("arguments[0].click();", country_choice)

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The client status was selected : " + client_status)
        return ClientsPage(self.driver)

    def click_search_button(self):
        # Need to scroll to 'Filters' button to make 'Search' button visible
        # drop_down_filter = super().wait_load_element("//span[@class='filter-option pull-left']")
        # super().scroll_into_view(drop_down_filter)
        # Click on 'Search'
        search_button_xpath = "//td[@class='txt_al_c']/input"
        search_button = super().wait_element_to_be_clickable(search_button_xpath)
        # search_button.click()
        self.driver.execute_script("arguments[0].click();", search_button)
        Logging().reportDebugStep(self, "The search button was clicked ")
        return ClientsPage(self.driver)

    def open_client_id(self):
        self.wait_crm_loading_to_finish()
        client_id = self.driver.find_element(By.XPATH, "//tr[@class='lvtColData']//div[@class='link_field']")
        self.driver.execute_script("arguments[0].scrollIntoView();", client_id)
        self.perform_scroll_up()
        sleep(1)
        client_id.click()
        Logging().reportDebugStep(self, "Click user name by email : ")
        return ClientProfilePage(self.driver)

    def open_create_filter_pop_up(self):
        filter_button = super().wait_element_to_be_clickable("//a[contains(text(), 'Create Filter')]")
        filter_button.click()
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterPage(self.driver)

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
        Logging().reportDebugStep(self, "Eighth column name : " + name_eighth_column.text)
        return name_eighth_column.text

    def get_ninth_name_column(self):
        name_ninth_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[10]")
        Logging().reportDebugStep(self, "Ninth  column name : " + name_ninth_column.text)
        return name_ninth_column.text

    def get_tenth_name_column(self):
        name_tenth_column = super().wait_element_to_be_clickable(
            "//table[@id='resizeble_cols']//td[11]")
        Logging().reportDebugStep(self, "Tenth  column name : " + name_tenth_column.text)
        return name_tenth_column.text

    def get_eleventh_name_column(self):
        name_eleventh_column = self.driver.find_element(By.XPATH,
                                                        "//table[@id='resizeble_cols']//td[12]")
        Logging().reportDebugStep(self, "Eleventh  column name : " + name_eleventh_column.text)
        return name_eleventh_column.text

    def delete_filter(self):
        delete_filter_button = super().wait_element_to_be_clickable("//a[@title='Delete']")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "The delete button was clicked")
        return ClientsPage(self.driver)

    def confirm_delete(self):
        delete_filter_button = super().wait_element_to_be_clickable("//button[contains(text(),'OK')]")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "Filter was deleted")
        return ClientsPage(self.driver)

    def select_three_records_clients_module(self):
        sleep(2)
        first_check_box = super().wait_element_to_be_clickable("//tbody[@id='listBody']//tr[1]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[2]//td[1]")
        second_check_box.click()
        third_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[3]//td[1]")
        third_check_box.click()
        Logging().reportDebugStep(self, "The three records were selected")
        return ClientsPage(self.driver)

    def select_record(self):
        sleep(2)
        first_check_box = super().wait_element_to_be_clickable("//tbody[@id='listBody']//tr[1]//td[1]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The record was selected")
        return ClientsPage(self.driver)

    def click_send_email_module(self):
        send_email_module = super().wait_element_to_be_clickable("//input[@value='Send Mail']")
        send_email_module.click()
        Logging().reportDebugStep(self, "The mass edit module was opened")
        return SendEmailClientsModule(self.driver)

    def open_mass_edit_module(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass Edit']")
        mass_edit_module.click()
        Logging().reportDebugStep(self, "The mass edit module was opened")
        return MassEditClientsModule(self.driver)

    '''
        Returns a confirmation  message if the user entered a valid password
     '''

    def get_confirm_message(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns the message confirmation : " + confirm_message.text)
        return confirm_message.text

    def open_mass_assign_module(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass assign']")
        mass_edit_module.click()
        Logging().reportDebugStep(self, "The mass assign module was opened")
        return MassAssignClientsModule(self.driver)

    def get_first_client_email(self):
        client_email = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'Email')]//following-sibling::td[1]")))
        Logging().reportDebugStep(self, "Returns the first client: " + client_email.text)
        return client_email.text

    def get_second_client_email(self):
        sleep(3)
        second_client_id = super().wait_element_to_be_clickable(
            "//tbody[@id='listBody']//tr[2]//td[2]")
        second_client_id.click()

        client_email = super().wait_load_element("//td[contains(text(),'Email')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the first client: " + client_email.text)
        return client_email.text

    def get_third_client_email(self):
        sleep(3)
        third_client_id = super().wait_element_to_be_clickable(
            "//tbody[@id='listBody']//tr[3]//td[2]")
        third_client_id.click()

        client_email = super().wait_load_element("//td[contains(text(),'Email')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the first client: " + client_email.text)
        return client_email.text

    def came_back_on_previous_page(self):
        super().came_back_on_previous_page()
        Logging().reportDebugStep(self, "Come back on previous page was successfully")
        return ClientsPage(self.driver)

    def open_send_sms_module(self):
        mass_sms_module = super().wait_element_to_be_clickable("//input[@value='Send SMS']")
        mass_sms_module.click()
        Logging().reportDebugStep(self, "The send sms module was opened")
        return SendSMSClientsModule(self.driver)
