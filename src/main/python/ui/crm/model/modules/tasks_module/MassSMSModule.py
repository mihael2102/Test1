from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class MassSMSModule(CRMBasePage):

    def __init__(self) -> None:
        super().__init__()

    def perform_send_sms(self, phone, message):
        self.select_mobile(phone)
        self.enter_message(message)
        return MassSMSModule()

    def select_mobile(self, phone):
        phone_drop_down = super().wait_element_to_be_clickable(" //button[@id='dropdownMenu1']")
        phone_drop_down.click()
        #sleep(3)
        select_item = self.driver.find_element(By.XPATH,
                                               "//ul[@class='dropdown-menu']//a[contains(text(),'%s')]" % phone)
        select_item.click()
        Logging().reportDebugStep(self, "The mobile item was selected " + phone)
        return MassSMSModule()

    def enter_message(self, message):
        message_field = super().wait_element_to_be_clickable("//textarea[@id='sms-text']")
        message_field.clear()
        message_field.send_keys(message)
        Logging().reportDebugStep(self, "The message was entered " + message)
        return MassSMSModule()

    def click_send_button(self):
        send_button = self.driver.find_element(By.XPATH,
                                               "//div[@class='col-md-6 text-right']//button[contains(text(),'Send')]")
        send_button.click()
        Logging().reportDebugStep(self, "The save button was clicked")
        return MassSMSModule()
