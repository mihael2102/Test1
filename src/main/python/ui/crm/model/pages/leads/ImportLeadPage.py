from time import sleep
# import autoit
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.config import Config


class ImportLeadPage(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_first_step_upload_lead(self):
        browser_element = super().wait_element_to_be_clickable("//a[contains(text(),'Browse')]")
        browser_element.click()
        #sleep(2)
        # autoit.control_set_text("Open", "Edit1",
        #                         r"C:\Users\Administrator\.jenkins\workspace\%s\src\main\python\utils\documents\Leads_import.csv" % Config.test)
        # autoit.control_send("Open", "Edit1", "{ENTER}")
        Logging().reportDebugStep(self, "The  document was uploaded ")
        return ImportLeadPage()

    def get_confirm_message_upload_lead(self):
        confirm_message = super().wait_element_to_be_clickable("//div[@class='steps']//h1")
        Logging().reportDebugStep(self, "The confirm message is: " + confirm_message.text)
        return confirm_message.text

    def click_next_button(self):
        next_button = super().wait_element_to_be_clickable("//input[@value='Next Step']")
        next_button.click()
        Logging().reportDebugStep(self, "The next button was clicked ")
        return ImportLeadPage()

    def perform_scroll_down(self):
        super().perform_scroll_down()
        return ImportLeadPage()

    def select_source_lead(self, source):
        source_element = super().wait_element_to_be_clickable("//button[@data-id='lead_source']")
        source_element.click()
        #sleep(1)
        source_element_drop_down = super().wait_element_to_be_clickable(
                                                            "//div[@class='dropdown-menu open']//span[contains(text(),'%s')]" % source)

        self.driver.execute_script("arguments[0].scrollIntoView();", source_element_drop_down)
        source_element_drop_down.click()
        Logging().reportDebugStep(self, "The source was selected: " + source)
        return ImportLeadPage()

    def set_source_name(self, source_name):
        source_element = super().wait_element_to_be_clickable("//input[@id='source_name']")
        source_element.clear()
        source_element.send_keys(source_name)
        Logging().reportDebugStep(self, "The source name was set: " + source_name)
        return ImportLeadPage()

    def select_status(self, status):
        status_element = super().wait_element_to_be_clickable("//button[@data-id='lead_status']")
        status_element.click()
        #sleep(1)
        status_element_drop_down = super().wait_element_to_be_clickable(
                                                            "//div[@class='dropdown-menu open']//span[contains(text(),'%s')]" % status)

        self.driver.execute_script("arguments[0].scrollIntoView();", status_element_drop_down)
        status_element_drop_down.click()
        Logging().reportDebugStep(self, "The source was selected: " + status)
        return ImportLeadPage()

    def select_assigned_to(self, assigned_to):
        assigned_to_element = super().wait_element_to_be_clickable("//button[@data-id='lead_owner']")
        assigned_to_element.click()
        #sleep(2)
        assigned_to_element_drop_down = super().wait_element_to_be_clickable(
                                                                 "//div[@class='dropdown-menu open']//span[contains(text(),'%s')]" % assigned_to)

        self.driver.execute_script("arguments[0].scrollIntoView();", assigned_to_element_drop_down)
        assigned_to_element_drop_down.click()
        Logging().reportDebugStep(self, "The source was selected: " + assigned_to)
        return ImportLeadPage()
