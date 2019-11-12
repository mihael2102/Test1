from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from time import sleep


class TradingAccountsInformationPage(CRMBasePage):

    ''' 
        Returns the account text   
    '''

    def get_account_text(self):
        super().wait_load_element("//span[@id='dtlview_Trading Account Login']")
        count_id_field = self.driver.find_element(By.XPATH,
                                            "//td[contains(text(),'Trading Account Login')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the account from crm: " + count_id_field.text)
        return count_id_field.text

    ''' 
        Returns the currency text   
    '''

    def get_currency_text(self):
        super().wait_load_element("//span[@id='dtlview_Trading Account Login']")
        currency_field = self.driver.find_element(By.XPATH,
                                                  "//td[contains(text(),'Currency')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the currency from crm: " + currency_field.text)
        return currency_field.text

    ''' 
        Returns the balance text   
    '''

    def get_balance_text(self):
        sleep(0.1)
        balance_text = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                 ["balance_text"]).get_attribute("innerText")
        Logging().reportDebugStep(self, "Returns the balance from crm: " + balance_text)
        return balance_text

    def get_equity_text(self):
        equity_text = self.driver.find_element(By.XPATH, "//td[contains(text(),'Equity')]//following-sibling::td[1]")
        parser_equity_text = equity_text.text.split(".")[0]
        Logging().reportDebugStep(self, "Returns the equity from crm: " + parser_equity_text)
        return parser_equity_text

    def get_assigned_to_text(self):
        assigned_text = self.driver.find_element(By.XPATH,
                                                 "//td[contains(text(),'Assigned To')]//following-sibling::td[1]").text
        parse_assigned_text = assigned_text.strip()
        Logging().reportDebugStep(self, "Returns the  assigned  from crm: " + parse_assigned_text)
        return parse_assigned_text

    def get_server_to_text(self):
        server_text = self.driver.find_element(By.XPATH, "//td[contains(text(),'Server')]//following-sibling::td[1]")
        parser_assigned_text = server_text.text.split(".")[0]
        Logging().reportDebugStep(self, "Returns the  server  from crm: " + parser_assigned_text)
        return parser_assigned_text

    def get_brand_text(self):
        brand_text = self.driver.find_element(By.XPATH, "//td[contains(text(),'Brand')]//following-sibling::td[1]")
        parser_brand_text = brand_text.text.split(".")[0]
        Logging().reportDebugStep(self, "Returns the brand from crm: " + parser_brand_text)
        return parser_brand_text
