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
import autoit
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class CAPage(CRMBasePage):

    def fill_questionarie_triomarket(self,amount, purpose,anticipated, expirience, level, gloss, employment, worth, source, work, relate):
        self.enter_amount(amount)
        self.enter_purpose(purpose)
        self.enter_anticipated(anticipated)
        self.enter_expirience(expirience)
        self.enter_level(level)
        self.enter_gloss(gloss)
        self.enter_employment(employment)
        self.enter_worth(worth)
        self.enter_source(source)
        self.enter_work(work)
        self.enter_relate(relate)
        self.continue_click()
        Logging().reportDebugStep(self, "Finished fill questionarie")
        return CAPage(self.driver)

    def fill_questionarie(self, knowledge, source, funds, citizen, country, tin, pep):
        self.enter_knowledge(knowledge)
        self.enter_source(source)
        self.enter_funds(funds)
        self.enter_citizen(citizen)
        self.enter_country(country)
        self.enter_tin(tin)
        self.enter_pep(pep)
        self.next_questionarie()
        self.continue_click()
        Logging().reportDebugStep(self, "Finished fill questionarie")
        return CAPage(self.driver)

    def continue_click(self):
        sleep(5)
        submit = super().wait_load_element("//*[@id='welcome_continue']")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click Continue")
        return CAPage(self.driver)

    def next_questionarie(self):
        sleep(3)
        submit = super().wait_load_element("//*[@id='Next']")
        submit.click()
        Logging().reportDebugStep(self, "Click Next")
        return CAPage(self.driver)

    def enter_knowledge(self, knowledge):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlRelevantExperience']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlRelevantExperience']"))
        select.select_by_visible_text(knowledge)
        Logging().reportDebugStep(self, "Enter knowledge")
        return CAPage(self.driver)

    def enter_source(self, source):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlSourceOfFunds']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlSourceOfFunds']"))
        select.select_by_visible_text(source)
        Logging().reportDebugStep(self, "Enter source")
        return CAPage(self.driver)

    def enter_funds(self, funds):
        sleep(3)
        funds_input = self.driver.find_element(By.XPATH, "//*[@id='txtSourceOfFundsOther']")
        funds_input.send_keys(funds)
        Logging().reportDebugStep(self, "Enter funds")
        return CAPage(self.driver)

    def enter_citizen(self, citizen):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlUsCitizenTax']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlUsCitizenTax']"))
        select.select_by_visible_text(citizen)
        Logging().reportDebugStep(self, "Enter citizen")
        return CAPage(self.driver)

    def enter_country(self, country):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlTaxResidenceCountry_1']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlTaxResidenceCountry_1']"))
        select.select_by_visible_text(country)
        Logging().reportDebugStep(self, "Enter country")
        return CAPage(self.driver)

    def enter_tin(self, tin):
        sleep(3)
        tin_input = self.driver.find_element(By.XPATH, "//*[@id='dnn_ctr608_View_txtTaxTinNumber_1']")
        tin_input.send_keys(tin)
        Logging().reportDebugStep(self, "Enter knowledge")
        return CAPage(self.driver)

    def enter_pep(self, pep):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlPoliticallyPerson']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlPoliticallyPerson']"))
        select.select_by_visible_text(pep)
        Logging().reportDebugStep(self, "Enter knowledge")
        return CAPage(self.driver)

    def verify_status_documents(self):
        status = super().wait_load_element("//*[@id='trIdentityFront']/td[3]/span").text
        Logging().reportDebugStep(self, "Verify status documents")
        return status

    def browse_documents(self):
        button = super().wait_load_element("//*[@id='fileUploadItentity']")
        button.click()
        autoit.win_wait_active("Open")
        autoit.send("Bear.jpg")
        autoit.send("{ENTER}")
        Logging().reportDebugStep(self, "Click browse Documents")
        return CAPage(self.driver)

    def open_upload_document_module(self):
        sleep(5)
        button = super().wait_load_element("//a[contains(text(), 'Upload Documents')]")
        button.click()
        Logging().reportDebugStep(self, "Click Upload Documents")
        return CAPage(self.driver)

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