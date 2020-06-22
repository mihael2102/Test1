from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.ca.model.pages.ca_pages_ui.MainPage import MainPage
from src.main.python.ui.ca.model.pages.ca_global_ui.GlobalClientAreaPage import GlobalClientAreaPage
from time import sleep


class PersonalDetailsPage(CRMBasePage):

    def update_personal_information(self, list1=None, day=None, list2=None, month=None, list3=None, year=None,
                                    list4=None, country=None, list5=None, citizenship=None, field1=None, city=None,
                                    field2=None, zip_code=None, field3=None, address=None, field4=None, f_name=None,
                                    field5=None, l_name=None):
        if list1 and day:
            self.select_item_from_list(list1, day)
        if list2 and month:
            self.select_item_from_list(list2, month)
        if list3 and year:
            self.select_item_from_list(list3, year)
        if list4 and country:
            self.select_item_from_list(list4, country)
        if list5 and citizenship:
            self.select_item_from_list(list5, citizenship)
        if field1 and city:
            self.set_text_field(field1, city)
        if field2 and zip_code:
            self.set_text_field(field2, zip_code)
        if field3 and address:
            self.set_text_field(field3, address)
        if field4 and f_name:
            self.set_text_field(field4, f_name)
        if field5 and l_name:
            self.set_text_field(field5, l_name)
        self.click_final_btn()
        self.close_client_area()

    def select_item_from_list(self, pick_list, item):
        GlobalClientAreaPage(self.driver)\
            .select_item_from_list(pick_list, item)
        return PersonalDetailsPage(self.driver)

    def set_text_field(self, field, text):
        GlobalClientAreaPage(self.driver) \
            .set_text_field(field, text)
        return PersonalDetailsPage(self.driver)

    def click_final_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click final button")
        btn = super().wait_load_element(
            "//button[contains(text(),'Next')]|//button[contains(text(), 'Save Changes')]")
        btn.click()
        Logging().reportDebugStep(self, "Click 'Next/Save Changes' button")
        return PersonalDetailsPage(self.driver)

    def close_client_area(self):
        GlobalClientAreaPage(self.driver) \
            .close_client_area()
        return MainPage(self.driver)

    def get_data_from_text_field(self, field):
        sleep(0.1)
        Logging().reportDebugStep(self, "Get data from field: " + field)
        data = super().wait_load_element("//label[text()='%s']//following-sibling::input" % field)
        data = data.get_attribute('value')
        Logging().reportDebugStep(self, "Get data from field '" + field + "': " + data)
        return data

    def get_data_from_list(self, pick_list):
        sleep(0.1)
        Logging().reportDebugStep(self, "Get data from list: " + pick_list)
        data = super().wait_load_element("//custom-select[@name='%s']//span[contains(@class,'currentvalue')]"
                                         % pick_list).get_attribute('innerText')
        Logging().reportDebugStep(self, "Get data from list '" + pick_list + "': " + data)
        return data
