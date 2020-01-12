from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class AddDeleteEventPageUI(CRMBasePage):

    def click_add_event_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Add Event' button")
        add_event_btn = super().wait_element_to_be_clickable("//span[text()=' Add Event ']")
        add_event_btn.click()
        return AddDeleteEventPageUI(self.driver)

    def select_pick_list_item(self, pick_list, item):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select " + pick_list + ": " + item)
        title = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[text()='%s']" % (pick_list, item))
        self.driver.execute_script("arguments[0].click();", title)
        return AddDeleteEventPageUI(self.driver)

    def set_text_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set " + field + ": " + text)
        input_field = super().wait_load_element("//*[@id='%s']" % field)
        input_field.clear()
        input_field.send_keys(text)
        return AddDeleteEventPageUI(self.driver)

    def set_attached_to(self, name):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set Attached To: " + name)
        attached_to_field = super().wait_element_to_be_clickable(
            "//span[text()=' Attached To ']//following-sibling::div/span")
        attached_to_field.click()
        search_field = super().wait_load_element("//span[text()=' Attached To ']//following-sibling::div//input")
        search_field.clear()
        search_field.send_keys(name)
        item = super().wait_load_element("(//li/a/span[contains(text(),'%s')])[1]" % name)
        self.driver.execute_script("arguments[0].click();", item)
        return AddDeleteEventPageUI(self.driver)

    def click_save(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Save' button")
        save_btn = super().wait_element_to_be_clickable("//span[text()=' Save ']")
        save_btn.click()
        return AddDeleteEventPageUI(self.driver)
