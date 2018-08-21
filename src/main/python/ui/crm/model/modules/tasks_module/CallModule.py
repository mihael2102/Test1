from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.modules.client_modules.mass_sms.SendSMSClientsModule import SendSMSClientsModule
from src.main.python.ui.crm.model.modules.tasks_module.MassSMSModule import MassSMSModule
from src.main.python.ui.crm.model.modules.tasks_module.SendEmailModuleActions import SendEmailModuleActions
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class PhoneActionsModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_call_section(self, call_outcome, positive_outcome, negative_outcome, comments):
        self.set_call_outcome(call_outcome)
        self.set_positive_outcome(positive_outcome)
        self.set_negative_outcome(negative_outcome)
        self.set_comments(comments)
        return PhoneActionsModule()

    def open_send_sms_module(self):
        mass_sms_module = super().wait_element_to_be_clickable("//button[@title='Send SMS']")
        mass_sms_module.click()
        Logging().reportDebugStep(self, "The send sms module was opened")
        return MassSMSModule()

    def open_send_email_module(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//button[@title='Send Email']")
        first_check_box.click()
        Logging().reportDebugStep(self, "The call phone module was opened: ")
        return SendEmailModuleActions()

    def set_call_outcome(self, call_outcome):
        sleep(2)
        call_outcome_element = super().wait_element_to_be_clickable("//input[@value='%s']" % call_outcome)
        call_outcome_element.click()

        Logging().reportDebugStep(self, "The call outcome was set " + call_outcome)
        return PhoneActionsModule()

    def set_positive_outcome(self, positive_outcome):
        call_outcome_element = self.driver.find_element(By.XPATH, "//input[@value='%s']" % positive_outcome)
        call_outcome_element.click()

        Logging().reportDebugStep(self, "The call outcome was set " + positive_outcome)
        return PhoneActionsModule()

    def set_negative_outcome(self, negative_outcome):
        call_outcome_element = self.driver.find_element(By.XPATH, "//input[@value='%s']" % negative_outcome)
        call_outcome_element.click()

        Logging().reportDebugStep(self, "The call outcome was set " + negative_outcome)
        return PhoneActionsModule()

    def click_submit_button(self):
        send_button = self.driver.find_element(By.XPATH,
                                               "//div[@class='modal-body new-modal-body']//button[contains(text(),'Submit')]")
        send_button.click()
        Logging().reportDebugStep(self, "The submit button was clicked")
        return PhoneActionsModule()

    def set_comments(self, comments):
        comments_element = self.driver.find_element(By.XPATH, "//textarea[@name='interaction_comment']")
        comments_element.clear()
        comments_element.send_keys(comments)
        Logging().reportDebugStep(self, "The comments is set " + comments)
        return PhoneActionsModule()
