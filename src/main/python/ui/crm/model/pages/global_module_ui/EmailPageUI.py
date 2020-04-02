from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
import poplib
from email import parser
from src.main.python.utils.config import Config
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class EmailPageUI(CRMBasePage):

    def set_text_field(self, title, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set '" + text + "' to '" + title + "' field")
        field = super().wait_load_element(
            "//div[label[contains(text(),'%s')]]//following-sibling::mat-form-field//input" % title)
        field.clear()
        field.send_keys(text)
        return EmailPageUI(self.driver)

    def select_from_list(self, pick_list, item_title):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select '" + item_title + "' from pick list " + pick_list)
        item = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[text()='%s']" % (pick_list, item_title))
        self.driver.execute_script("arguments[0].click();", item)
        return EmailPageUI(self.driver)

    def set_body_mail(self, text):
        sleep(1)
        Logging().reportDebugStep(self, "Enter body mail: " + text)
        self.driver.switch_to_frame(super().wait_load_element("//*[@id='cke_1_contents']/iframe"))
        body_mail = super().wait_load_element("/html/body/p")
        body_mail.click()
        self.driver.execute_script("arguments[0].textContent = arguments[1];", body_mail, text)
        self.driver.switch_to.default_content()
        return EmailPageUI(self.driver)

    def click_send_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Send' button")
        btn = super().wait_load_element("//button[span=' Send ' and not(@disabled)]")
        btn.click()
        return EmailPageUI(self.driver)

    def check_email(self, subject):
        sleep(10)
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user(Config.email_address)
        pop_conn.pass_(Config.email_password)
        # Get messages from server:
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        # Concat message pieces:
        messages = ["\n".join(m.decode() for m in mssg[1]) for mssg in messages]
        # Parse message into an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        for message in messages:
            if str(message['subject']) == subject:
                Logging().reportDebugStep(self, str(message['subject']))
                return str(message['subject'])
        pop_conn.quit()
