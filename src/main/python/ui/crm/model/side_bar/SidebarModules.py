from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.side_bar.create_event.CreateEvent import CreateEvent
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep


class SidebarModules(CRMBasePage):

    def open_sidebar_if_exists(self):
        open_sidebar = None
        try:
            open_sidebar = self.wait_element_to_be_clickable("//a[@id='slide-button']", 2)
        except TimeoutException:
            Logging().reportDebugStep(self, "Side bar is not present")
        if open_sidebar:
            try:
                self.driver.find_element(By.XPATH, "//a[@id='slide-button' and @title='Open']")
                open_sidebar.click()
                sleep(2)
                self.wait_element_to_be_clickable("//a[@id='slide-button' and @title='Close']")
                Logging().reportDebugStep(self, "Open the side bar")
            except NoSuchElementException:
                Logging().reportDebugStep(self, "Side bar is already open")

    def open_create_event_module(self, module):
        self.open_sidebar_if_exists()
        selected_module = super().wait_element_to_be_clickable("//div[@id='sidebar']//a[contains(., '%s')]" % module)
        selected_module.click()
        sleep(2)
        super().wait_element_to_be_clickable("//a[@id='additional_actions_button']")
        Logging().reportDebugStep(self, "The event module was opened")
        return CreateEvent(self.driver)
