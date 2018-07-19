from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CallTaskModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_call_section(self, call_outcome, positive_outcome, negative_outcome, comments):
        self.set_call_outcome(call_outcome)
        self.set_positive_outcome(positive_outcome)
        self.set_negative_outcome(negative_outcome)
        self.set_comments(comments)
        return CallTaskModule()

    def set_call_outcome(self, call_outcome):
        sleep(2)
        call_outcome_element = super().wait_element_to_be_clickable("//input[@value='%s']" % call_outcome)
        call_outcome_element.click()

        Logging().reportDebugStep(self, "The call outcome was set " + call_outcome)
        return CallTaskModule()

    def set_positive_outcome(self, positive_outcome):
        call_outcome_element = self.driver.find_element(By.XPATH, "//input[@value='%s']" % positive_outcome)
        call_outcome_element.click()

        Logging().reportDebugStep(self, "The call outcome was set " + positive_outcome)
        return CallTaskModule()

    def set_negative_outcome(self, negative_outcome):
        call_outcome_element = self.driver.find_element(By.XPATH, "//input[@value='%s']" % negative_outcome)
        call_outcome_element.click()

        Logging().reportDebugStep(self, "The call outcome was set " + negative_outcome)
        return CallTaskModule()

    def click_submit_button(self):
        send_button = self.driver.find_element(By.XPATH,
                                               "//div[@class='modal-body new-modal-body']//button[contains(text(),'Submit')]")
        send_button.click()
        Logging().reportDebugStep(self, "The submit button was clicked")
        return CallTaskModule()

    def set_comments(self, comments):
        comments_element = self.driver.find_element(By.XPATH, "//textarea[@name='interaction_comment']")
        comments_element.clear()
        comments_element.send_keys(comments)
        Logging().reportDebugStep(self, "The comments is set " + comments)
        return CallTaskModule()
