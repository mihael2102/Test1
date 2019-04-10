from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class WebTraderPage(CRMBasePage):

    def check_avaliable_funds(self):
        avaliable_funds = self.driver.find_element_by_xpath("//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[1]/div[1]").text
        Logging().reportDebugStep(self, "Check avaliable funds")
        return avaliable_funds

    def check_used_funds(self):
        used_funds = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[2]/div[1]").text
        Logging().reportDebugStep(self, "Check used funds")
        return used_funds

    def check_account_value(self):
        account_value = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[3]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return account_value

    def check_total_p_l(self):
        total_p_l = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[4]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return total_p_l

    def check_margin_level(self):
        margin_level = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[5]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return margin_level

    def get_avaliable_funds(self):
        avaliable_funds = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[1]/div[2]").text
        Logging().reportDebugStep(self, "Check account value")
        return avaliable_funds
