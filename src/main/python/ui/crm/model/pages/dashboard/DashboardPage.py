from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.client_modules.mass_sms.SendSMSClientsModule import SendSMSClientsModule
from src.main.python.ui.crm.model.modules.client_modules.send_email.SendEmailClientsModule import SendEmailClientsModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.client_modules.mass_assign.MassAssignClientsModule import \
    MassAssignClientsModule
from src.main.python.ui.crm.model.modules.client_modules.mass_edit.MassEditClientsModule import MassEditClientsModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config

class DashboardPage(CRMBasePage):

    def refresh(self):
        self.driver.refresh()
        Logging().reportDebugStep(self, "Perform the refresh ")
        return DashboardPage(self.driver)

    def check_total_portfolio(self):
        sleep(20)
        total_portfolio = self.driver.find_element(By.XPATH, "//*[@id='main-dashboard']/div[2]/div[1]/div/div[1]/div/div[1]/div/h4")
        Logging().reportDebugStep(self, "Check total portfolio")
        return total_portfolio.text

    def check_balance(self):
        sleep(3)
        check_balance = self.driver.find_element(By.XPATH,
            "//*[@id='main-dashboard']/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]")
        Logging().reportDebugStep(self, "Check balance")
        return check_balance.text

    def check_credit(self):
        sleep(3)
        check_credit = self.driver.find_element(By.XPATH,
            "//*[@id='main-dashboard']/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]")
        Logging().reportDebugStep(self, "Check credit")
        return check_credit.text

    def check_openpandl(self):
        sleep(3)
        check_openpandl = self.driver.find_element(By.XPATH,
            "//*[@id='main-dashboard']/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]")
        Logging().reportDebugStep(self, "Check open p and l")
        return check_openpandl.text

    def click_week_button(self):
        sleep(7)
        today_btn = super().wait_element_to_be_clickable("//a[contains(text(), 'Week')]")
        today_btn.click()
        Logging().reportDebugStep(self, "Click week btn")
        return DashboardPage(self.driver)