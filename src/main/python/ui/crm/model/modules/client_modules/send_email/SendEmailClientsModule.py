from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class SendEmailClientsModule(CRMBasePage):

    def perform_send_email(self, subject, comment):
        self.set_subject(subject)
        self.set_comment(comment)
        self.click_send_button_clients_module()

    def set_subject(self, subject):
        subject_field = super().wait_element_to_be_clickable("//input[@name='subject']")
        subject_field.clear()
        subject_field.send_keys(subject)
        Logging().reportDebugStep(self, "The subject was set: " + subject)
        return SendEmailClientsModule()

    def set_comment(self, comments):
        self.driver.switch_to_frame(super().wait_element_to_be_clickable("//div[@id='cke_description']//iframe"))
        comment_tag = self.driver.find_element(By.XPATH, "//html[@dir='ltr']/body")
        comment_tag.send_keys(comments)
        self.driver.switch_to_default_content()
        Logging().reportDebugStep(self, "The comment was set: " + comments)
        return SendEmailClientsModule()

    def click_send_button_clients_module(self):
        send_button = super().wait_element_to_be_clickable("//input[@name='Send']")
        send_button.click()
        Logging().reportDebugStep(self, "The send button was clicked")
        return SendEmailClientsModule()
