from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.ca.model.pages.ca_pages_ui.MainPage import MainPage
from time import sleep


class GlobalClientAreaPage(CRMBasePage):

    def select_item_from_list(self, pick_list, item):
        sleep(0.5)
        try:
            Logging().reportDebugStep(self, "Select " + pick_list + ": " + item)
            data = super().wait_load_element("//custom-select[@name='%s']//span[text()='%s']" % (pick_list, item))
            self.driver.execute_script("arguments[0].click();", data)
        except:
            Logging().reportDebugStep(self, "The " + pick_list + " list is read only or is not existing")
        return GlobalClientAreaPage(self.driver)

    def set_text_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set " + field + ": " + text)
        input_field = super().wait_load_element("//label[text()='%s']//following-sibling::input" % field)
        try:
            sleep(0.1)
            input_field.clear()
            input_field.send_keys(text)
        except:
            Logging().reportDebugStep(self, "The " + field + " field is read only")
        return GlobalClientAreaPage(self.driver)

    def click_btn(self, button):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click '" + button + "' button")
        btn = super().wait_load_element("//button[contains(text(),'%s')]" % button)
        btn.click()
        return GlobalClientAreaPage(self.driver)

    def close_client_area(self):
        sleep(1)
        try:
            Logging().reportDebugStep(self, "Close Client Area pop up")
            close_btn = super().wait_element_to_be_clickable("//a[@class='close-popup-pandats']", timeout=35)
            self.driver.execute_script("arguments[0].click();", close_btn)
        except:
            Logging().reportDebugStep(self, "Client Area pop up already closed")
        return GlobalClientAreaPage(self.driver)
