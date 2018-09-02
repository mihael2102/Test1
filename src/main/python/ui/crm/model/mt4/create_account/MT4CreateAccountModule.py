from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging


class MT4CreateAccountModule(CRMBasePage):

    def create_account(self, server, currency, group, leverage):
        """
        create a trading account
        :param server:
        :param currency:
        :param group:
        :param leverage:
        :return:
        """
        if server:
            self.select_server(server)
        if currency:
            self.select_currency(currency)
        if group:
            self.select_group(group)
        if leverage:
            self.select_leverage(leverage)
        self.click_create()
        return ClientProfilePage(self.driver)

    def select_server(self, server):
        drop_down = self.wait_element_to_be_clickable("//select[@name='server']")
        drop_down.click()
        server_selection = self.driver.find_element(By.XPATH, "//select[@name='server']//"
                                                              "following-sibling::*[contains(.,'%s')]" % server)
        server_selection.click()
        Logging().reportDebugStep(self, "Trading account server was selected: %s" + server_selection.text)
        return self

    def select_currency(self, currency):
        drop_down = self.wait_element_to_be_clickable("//select[@name='currency']")
        drop_down.click()
        currency_selection = self.driver.find_element(By.XPATH, "//select[@name='currency']//"
                                                                "following-sibling::*[contains(.,'%s')]" % currency)
        currency_selection.click()
        Logging().reportDebugStep(self, "Trading account currency was selected: %s" + currency_selection.text)
        return self

    def select_group(self, group):
        drop_down = self.wait_element_to_be_clickable("//select[@name='group']")
        drop_down.click()
        group_selection = self.driver.find_element(By.XPATH, "//select[@name='group']//"
                                                             "following-sibling::*[contains(.,'%s')]" % group)
        group_selection.click()
        Logging().reportDebugStep(self, "Trading account group was selected: %s" + group_selection.text)
        return self

    def select_leverage(self, leverage):
        drop_down = self.wait_element_to_be_clickable("//select[@name='leverage']")
        drop_down.click()
        leverage_selection = self.driver.find_element(By.XPATH, "//select[@name='leverage']//"
                                                                "following-sibling::*[contains(.,'%s')]" % leverage)
        leverage_selection.click()
        Logging().reportDebugStep(self, "Trading account leverage was selected: %s" + leverage_selection.text)
        return self

    def click_create(self):
        button = self.wait_load_element("//button[contains(., 'Create')]")
        button.click()
        Logging().reportDebugStep(self, "The Create button was clicked")
