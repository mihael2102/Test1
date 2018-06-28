from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class SendSMSClientsModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_send_sms(self, message):
        self.enter_message(message)
        return SendSMSClientsModule()

    def enter_message(self, message):
        message_field = super().wait_element_to_be_clickable("//textarea[@id='sms_message']")
        message_field.clear()
        message_field.send_keys(message)
        Logging().reportDebugStep(self, "The message was entered " + message)
        return SendSMSClientsModule()

    def click_send_button(self):
        send_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Send')]")
        send_button.click()
        Logging().reportDebugStep(self, "The send button was clicked")
        return SendSMSClientsModule()

    def click_ok(self):
        super().click_ok()
        Logging().reportDebugStep(self, "Message sent successfully")
        return SendSMSClientsModule()
