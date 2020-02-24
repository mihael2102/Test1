import re
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support.select import Select


class QuestionnaireCRMPage(CRMBasePage):

    def select_item_pick_list(self, question, answer):
        sleep(0.1)
        pick_list = Select(super().wait_load_element(
            "//label[contains(text(),'%s')]//following-sibling::div[@class='form-group']/select" % question))
        pick_list.select_by_visible_text(answer)
        Logging().reportDebugStep(self, question + ": " + answer)
        return QuestionnaireCRMPage(self.driver)

    def set_text_field(self, title, text):
        sleep(0.1)
        field = super().wait_load_element("//label[contains(text(),'%s')]//following-sibling::input" % title)
        field.clear()
        field.send_keys(text)
        Logging().reportDebugStep(self, title + ": " + text)
        return QuestionnaireCRMPage(self.driver)

    def open_section(self, title):
        sleep(0.1)
        section = super().wait_load_element("//h4[contains(text(),'%s')]" % title)
        self.driver.execute_script("arguments[0].click();", section)
        Logging().reportDebugStep(self, "Open section: " + title)
        return QuestionnaireCRMPage(self.driver)

    def click_save_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Save' button")
        save_btn = super().wait_load_element("//*[@id='Questionnaire_save_button']")
        self.driver.execute_script("arguments[0].click();", save_btn)
        return QuestionnaireCRMPage(self.driver)

    def click_ok(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'OK' button")
        ok_btn = super().wait_load_element("//button[text()='OK']")
        ok_btn.click()
        return QuestionnaireCRMPage(self.driver)

    def get_success_message(self):
        sleep(0.1)
        message = super().wait_load_element("//div[@class='bootstrap-dialog-message']").text
        Logging().reportDebugStep(self, "Get message: " + message)
        return QuestionnaireCRMPage(self.driver)
