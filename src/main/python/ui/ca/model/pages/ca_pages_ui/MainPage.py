from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MainPage(CRMBasePage):

    def open_first_tab(self, url):
        self.open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return MainPage(self.driver)

    def switch_second_tab(self):
        self.switch_second_tab_page()
        Logging().reportDebugStep(self, "Switch to second page")
        return MainPage(self.driver)

    def refresh_page_ca(self):
        self.refresh_page()
        return MainPage(self.driver)

    def click_hi_user(self):
        sleep(0.5)
        click_hi_user = super().wait_load_element("//*[contains(text(),'Hi,')]", timeout=75)
        sleep(0.7)
        self.driver.execute_script("arguments[0].click();", click_hi_user)
        Logging().reportDebugStep(self, "Click 'Hi, User' button")
        return MainPage(self.driver)

    """ Click item from list under 'Hi, user' button """
    def click_main_menu_item(self, item):
        sleep(0.1)
        try:
            Logging().reportDebugStep(self, "Click '" + item + "' button in menu list")
            menu_item = super().wait_load_element("//ul/li[text()=' %s ']" % item)
            self.driver.execute_script("arguments[0].click();", menu_item)
        except:
            Logging().reportDebugStep(self, "'" + item + "' button doesn't exist in menu list")
        return MainPage(self.driver)

    def get_client(self):
        sleep(1)
        client = super().wait_load_element("//*[contains(text(),'Hi,')]").get_attribute('innerText')
        client = client.split(' ')[1]
        Logging().reportDebugStep(self, "Get name of client: " + client)
        return client
