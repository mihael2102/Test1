from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage

from src.main.python.utils.logs.Loging import Logging


class FilterPage(CRMBasePage):

    def perform_create_filter_client_module(self, filter_name, first_column_name, second_column_name, third_column_name,
                                            fourth_column_name, fifth_column_name, sixth_column_name,
                                            seventh_column_name, eighth_column_name, ninth_column_name,
                                            tenth_column_name, eleventh_column_name):
        self.set_name_filter(filter_name)
        self.perform_choice_first_column(first_column_name)
        self.perform_choice_second_column(second_column_name)
        self.perform_choice_third_column(third_column_name)
        self.perform_choice_fourth_column(fourth_column_name)
        self.perform_choice_fifth_column(fifth_column_name)
        self.perform_choice_sixth_column(sixth_column_name)
        self.perform_choice_seventh_column(seventh_column_name)
        self.perform_choice_eighth_column(eighth_column_name)
        self.perform_choice_ninth_column(ninth_column_name)
        self.perform_choice_tenth_column(tenth_column_name)
        self.perform_choice_eleventh_column(eleventh_column_name)
        return FilterPage(self.driver)

    def perform_create_filter_lead_module(self, filter_name, first_column_name, second_column_name, third_column_name,
                                          fourth_column_name, fifth_column_name, sixth_column_name, seventh_column_name,
                                          eighth_column_name):
        self.set_name_filter(filter_name)
        self.perform_choice_first_column(first_column_name)
        self.perform_choice_second_column(second_column_name)
        self.perform_choice_third_column(third_column_name)
        self.perform_choice_fourth_column(fourth_column_name)
        self.perform_choice_fifth_column(fifth_column_name)
        self.perform_choice_sixth_column(sixth_column_name)
        self.perform_choice_seventh_column(seventh_column_name)
        self.perform_choice_eighth_column(eighth_column_name)
        return FilterPage(self.driver)

    def perform_create_filter_lead_module_new(self, filter_name, first_column_name, second_column_name, third_column_name,
                                          fourth_column_name, fifth_column_name, sixth_column_name, seventh_column_name):
        self.set_name_filter(filter_name)
        self.perform_choice_first_column(first_column_name)
        self.perform_choice_second_column(second_column_name)
        self.perform_choice_third_column(third_column_name)
        self.perform_choice_fourth_column(fourth_column_name)
        self.perform_choice_fifth_column(fifth_column_name)
        self.perform_choice_sixth_column(sixth_column_name)
        self.perform_choice_seventh_column(seventh_column_name)
        return FilterPage(self.driver)

    def perform_create_filter_help_desk_module(self, filter_name, first_column_name, second_column_name,
                                               third_column_name, fourth_column_name, fifth_column_name,
                                               sixth_column_name, seventh_column_name, eightn_column_name,
                                               tenth_column_name, eleventh_column_name):
        self.set_name_filter(filter_name)
        self.perform_choice_first_column(first_column_name)
        self.perform_choice_second_column(second_column_name)
        self.perform_choice_third_column(third_column_name)
        self.perform_choice_fourth_column(fourth_column_name)
        self.perform_choice_fifth_column(fifth_column_name)
        self.perform_choice_sixth_column(sixth_column_name)
        self.perform_choice_seventh_column(seventh_column_name)
        self.perform_choice_eighth_column(eightn_column_name)
        self.perform_choice_tenth_column(tenth_column_name)
        self.perform_choice_eleventh_column(eleventh_column_name)
        return FilterPage(self.driver)

    def perform_create_filter_documents_module(self, filter_name, first_column_name, second_column_name,
                                               third_column_name, fourth_column_name):
        self.set_name_filter(filter_name)
        self.perform_choice_first_column(first_column_name)
        self.perform_choice_second_column(second_column_name)
        self.perform_choice_third_column(third_column_name)
        self.perform_choice_fourth_column(fourth_column_name)
        return FilterPage(self.driver)

    def perform_create_filter_trading_accounts_module(self, filter_name, first_column_name, second_column_name,
                                                      third_column_name, fourth_column_name, fifth_column_name,
                                                      sixth_column_name, seventh_column_name, eightn_column_name):
        self.set_name_filter(filter_name)
        self.perform_choice_first_column(first_column_name)
        self.perform_choice_second_column(second_column_name)
        self.perform_choice_third_column(third_column_name)
        self.perform_choice_fourth_column(fourth_column_name)
        self.perform_choice_fifth_column(fifth_column_name)
        self.perform_choice_sixth_column(sixth_column_name)
        self.perform_choice_seventh_column(seventh_column_name)
        self.perform_choice_eighth_column(eightn_column_name)
        return FilterPage(self.driver)

    def set_name_filter(self, name_filter):
        name_filter_field = super().wait_load_element("//input[@name='viewName']")
        name_filter_field.clear()
        name_filter_field.send_keys(name_filter)
        Logging().reportDebugStep(self, "Tha name filter was set")
        return FilterPage(self.driver)

    def perform_choice_first_column(self, name_first_column):
        super().wait_element_to_be_clickable("//select[@name='column1']")
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column1']"))
        select.select_by_visible_text(name_first_column)
        Logging().reportDebugStep(self, "The first column was selected")
        return FilterPage(self.driver)

    def perform_choice_second_column(self, name_second_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column2']"))
        select.select_by_visible_text(name_second_column)
        Logging().reportDebugStep(self, "The second column was selected")
        return FilterPage(self.driver)

    def perform_choice_third_column(self, name_third_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column3']"))
        select.select_by_visible_text(name_third_column)
        Logging().reportDebugStep(self, "The third column was selected")
        return FilterPage(self.driver)

    def perform_choice_fourth_column(self, name_fourth_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column4']"))
        select.select_by_visible_text(name_fourth_column)
        Logging().reportDebugStep(self, "The fourth column was selected")
        return FilterPage(self.driver)

    def perform_choice_fifth_column(self, name_fifth_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column5']"))
        select.select_by_visible_text(name_fifth_column)
        Logging().reportDebugStep(self, "The fifth column was selected")
        return FilterPage(self.driver)

    def perform_choice_sixth_column(self, name_sixth_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column6']"))
        select.select_by_visible_text(name_sixth_column)
        Logging().reportDebugStep(self, "The sixth column was selected")
        return FilterPage(self.driver)

    def perform_choice_seventh_column(self, name_seventh_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column7']"))
        select.select_by_visible_text(name_seventh_column)
        Logging().reportDebugStep(self, "The seventh column was selected")
        return FilterPage(self.driver)

    def perform_choice_eighth_column(self, name_eighth_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column8']"))
        select.select_by_visible_text(name_eighth_column)
        Logging().reportDebugStep(self, "The eight column was selected")
        return FilterPage(self.driver)

    def perform_choice_ninth_column(self, name_ninth_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column9']"))
        select.select_by_visible_text(name_ninth_column)
        Logging().reportDebugStep(self, "The ninth column was selected")
        return FilterPage(self.driver)

    def perform_choice_tenth_column(self, name_tenth_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column10']"))
        select.select_by_visible_text(name_tenth_column)
        Logging().reportDebugStep(self, "The eleventh column was selected")
        return FilterPage(self.driver)

    def perform_choice_eleventh_column(self, name_eleventh_column):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='column11']"))
        select.select_by_visible_text(name_eleventh_column)
        Logging().reportDebugStep(self, "The eleventh column was selected")
        return FilterPage(self.driver)

    def click_save_button(self):
        save_button = self.driver.find_element(By.XPATH, "//input[@id='saveCustomView']")
        save_button.click()
        Logging().reportDebugStep(self, "The filter was crated: ")
        return FilterPage(self.driver)
