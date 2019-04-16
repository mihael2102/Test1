from selenium.webdriver.common.by import By
from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class SendEmailClientsModule(CRMBasePage):

    def perform_send_email(self, subject, comment):
        self.set_subject(subject)
        self.set_comment(comment)
        self.click_send_button_clients_module()

    def set_subject(self, subject):
        sleep(2)
        subject_field = super().wait_element_to_be_clickable("//input[@name='subject']")
        subject_field.clear()
        subject_field.send_keys(subject)
        Logging().reportDebugStep(self, "The subject was set: " + subject)
        return SendEmailClientsModule()

    def set_comment(self, comments):
        try:
            sleep(5)
            self.driver.switch_to_frame(super().wait_element_to_be_clickable("//div[@id='cke_description']//iframe"))
            comment_tag = self.driver.find_element(By.XPATH, "/html/body/p")
            comment_tag.send_keys(comments)
            self.driver.switch_to_default_content()
        except:
            self.refresh_page()
            sleep(2)
            self.click_send_mail_btn()
            sleep(1)
            self.driver.switch_to_frame(super().wait_element_to_be_clickable("//div[@id='cke_description']//iframe"))
            comment_tag = self.driver.find_element(By.XPATH, "//html[@dir='ltr']/body")
            comment_tag.send_keys(comments)
            self.driver.switch_to_default_content()
        Logging().reportDebugStep(self, "The comment was set: " + comments)
        return SendEmailClientsModule(self.driver)

    def click_send_button_clients_module(self):
        send_button = super().wait_element_to_be_clickable("//input[@name='Send']")
        send_button.click()
        Logging().reportDebugStep(self, "The send button was clicked")
        return SendEmailClientsModule()

    def click_save_btn(self):
        save_btn = super().wait_element_to_be_clickable("//*[@id='mailcomposeform']//input[@value='Save']")
        save_btn.click()
        Logging().reportDebugStep(self, "The Save button was clicked")
        return SendEmailClientsModule(self.driver)

    def get_email_subject(self):
        sleep(1)
        email_subject = self.driver.find_element_by_xpath("//*[@id='rld_table_content']/tbody/tr[2]/td[1]/a").text
        Logging().reportDebugStep(self, "Email subject is: " + email_subject)
        return email_subject

    def click_edit_email_btn(self):
        edit_email_btn = super().wait_element_to_be_clickable("//*[@id='rld_table_content']//a[@title='Edit']")
        self.driver.execute_script("arguments[0].click();", edit_email_btn)
        Logging().reportDebugStep(self, "The Edit Mail button was clicked")
        return SendEmailClientsModule(self.driver)

    def click_send_mail_btn(self):
        send_mail_btn = self.driver.find_element_by_xpath("//*[@id='sidebar']//a[contains(text(),'Send Mail')]")
        send_mail_btn.click()
        Logging().reportDebugStep(self, "Click Send Mail button")
        return SendEmailClientsModule(self.driver)
