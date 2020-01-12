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
        add_event_btn = super().wait_element_to_be_clickable("//span[text()=' Add Event ']")
        add_event_btn.click()
        Logging().reportDebugStep(self, "Click 'Add Event' button")
        return AddDeleteEventPageUI(self.driver)
