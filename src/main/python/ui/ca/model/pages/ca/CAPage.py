from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import time

from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class CAPage(CRMBasePage):

    def verify_ticket_status_closed(self):
        status = super().wait_load_element("//*[@id='closedTickets']/tbody/tr/td[4]").text
        Logging().reportDebugStep(self, "Check status")
        return status

    def verify_ticket_status(self):
        status = super().wait_load_element("//*[@id='openTickets']/tbody/tr/td[4]").text
        Logging().reportDebugStep(self, "Check status")
        return status

    def get_ticket_number(self):
        ticket_number = super().wait_load_element("//*[@id='lblSuccessMessage']").text
        Logging().reportDebugStep(self, "Check ticket number")
        return ticket_number

    def click_submit_ticket(self):
        submit = super().wait_load_element("//*[@id='btnSubmit']")
        submit.click()
        Logging().reportDebugStep(self, "Click submit")
        return CAPage(self.driver)

    def close_popup_create(self):
        submit = super().wait_load_element("//*[@id='btnCloseSubmitWindow']")
        submit.click()
        Logging().reportDebugStep(self, "Click submit")
        return CAPage(self.driver)

    def enter_subject(self, subject):
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='iPopUp']"))
            subject_input = super().wait_load_element("//*[@id='txtSubject']")
            subject_input.send_keys(subject)
            Logging().reportDebugStep(self, "Enter subject")
            return CAPage(self.driver)
        except Exception as e:
            print("Error: ", e)
            return CAPage(self.driver)

    def enter_description(self, description):
        description_input = super().wait_load_element("//textarea[@class='new_ticket_text']")
        description_input.send_keys(description)
        Logging().reportDebugStep(self, "Enter description")
        return CAPage(self.driver)

    def select_category(self, category):
        select = super().wait_load_element("//*[@id='ddlCategory']")
        select.click()
        select_category = super().wait_load_element("//*[@id='ddlCategory']/option[contains(text(), '%s')]" % category)
        select_category.click()
        # self.driver.execute_script("arguments[0].click();", select_category)
        Logging().reportDebugStep(self, "Select category")
        return CAPage(self.driver)


    def open_new_ticket(self):
        sleep(2)
        service_desk = super().wait_load_element("//*[@id='btnTicketInfoNewTicket']")
        service_desk.click()
        Logging().reportDebugStep(self, "Click Open New Ticket")
        return CAPage(self.driver)

    def open_service_desk(self):
        sleep(2)
        service_desk = super().wait_load_element("//*[@id='mainmenu']/li[2]/a")
        service_desk.click()
        Logging().reportDebugStep(self, "Click Open Service Desk")
        return CAPage(self.driver)

    def open_live_account(self):
        sleep(2)
        button = super().wait_load_element("//*[@value='OPEN NEW ACCOUNT']")
        # button.click()
        self.driver.execute_script("arguments[0].click();", button)
        Logging().reportDebugStep(self, "Click Open Live Account")
        return CAPage(self.driver)

    def click_check_box_confirm(self):
        check_box = super().wait_load_element("//*[@id='cbRiskAck']")
        check_box.click()
        Logging().reportDebugStep(self, "Click I am over 18 years of age and I have read and accepted these")
        return CAPage(self.driver)

    def click_confirm(self):
        confirm = super().wait_load_element("//*[@id='btnCloseRiskPopup']")
        confirm.click()
        Logging().reportDebugStep(self, "Click confirm")
        return CAPage(self.driver)

    def verify_relevant_currency(self):
        my_account_button = super().wait_load_element("//*[@id='mainmenu']/li[1]/a")
        my_account_button.click()
        sleep(8)
        currency = super().wait_load_element("//*[@id='RealAccountListBody']/tr/td[3]").text
        Logging().reportDebugStep(self, "Click My Account and check currency")
        return currency

    def verify_correct_data(self):
        leverage = super().wait_load_element("//*[@id='RealAccountListBody']/tr/td[2]").text
        Logging().reportDebugStep(self, "Check leverage")
        return leverage

    def open_demo_account(self):
        confirm = super().wait_load_element("//*[@value='NEW PRACTICE ACCOUNT']")
        self.driver.execute_script("arguments[0].click();", confirm)
        # confirm.click()
        sleep(2)
        Logging().reportDebugStep(self, "Click add new demo account")
        return CAPage(self.driver)

    def select_currency(self):
        sleep(5)
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//select[@id='NewDemoAccountCurrency']")))
        # select = Select(self.dri_text(ver.find_element_by_css_selector("#NewDemoAccountCurrency"))
        # select.select_by_visible"EUR")
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='iPopUp']"))
            select = super().wait_load_element("//select[@id='NewDemoAccountCurrency']")
            select.click()
            select_currency = super().wait_load_element("//select[@id='NewDemoAccountCurrency']/option[contains(text(), 'EUR')]")
            select_currency.click()
            # self.driver.execute_script("arguments[0].click();", select_currency)
            Logging().reportDebugStep(self, "Select currency")
            return CAPage(self.driver)
        except Exception as e:
            print("Error: ", e)
            return CAPage(self.driver)


    def select_leverage(self):
        sleep(3)
        select = super().wait_load_element("//*[@id='SelLeverageP']")
        select.click()
        select_leverage = super().wait_load_element("//select[@id='SelLeverageP']/option[1]")
        self.driver.execute_script("arguments[0].click();", select_leverage)
        Logging().reportDebugStep(self, "Select USD currency")
        return CAPage(self.driver)

    def select_deposit(self):
        sleep(3)
        input = super().wait_load_element("//*[@id='TextInitialDepositP']")
        input.clear()
        input.send_keys("5000")
        Logging().reportDebugStep(self, "Select Deposit")
        return CAPage(self.driver)

    def click_submit(self):
        sleep(3)
        click_submit = super().wait_load_element("//button[@id='SubmitFinal']")
        self.driver.execute_script("arguments[0].click();", click_submit)
        # click_submit.click()
        Logging().reportDebugStep(self, "Click Submit")
        return CAPage(self.driver)

    def finish_button(self):
        sleep(3)
        click_submit = super().wait_load_element("//input[@class= 'green_btn popup_mod_btn centered']")
        click_submit.click()
        Logging().reportDebugStep(self, "Click Finish")
        return CAPage(self.driver)