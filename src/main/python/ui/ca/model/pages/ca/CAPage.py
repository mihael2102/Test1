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

    def click_actions_launch_by_account(self, account_number):
        sleep(3)
        actions_launch_by_account = self.driver.find_element_by_xpath("//button[@id='btnLaunch" + account_number + "']")
        actions_launch_by_account.click()
        Logging().reportDebugStep(self, "Click LAUNCH")
        return CAPage(self.driver)

    def get_account_number(self):
        sleep(3)
        account_number = self.driver.find_element_by_xpath("//*[@id='OpenAccontTbl']/tbody/tr[1]/td[2]").text
        Logging().reportDebugStep(self, "Check account_number " + account_number)
        return account_number

    def get_balance(self):
        sleep(10)
        avaliable_funds = self.driver.find_element_by_xpath(
            "//*[@id='PracticeAccountListBody']/tr/td[4]").text
        Logging().reportDebugStep(self, "Check Balance " + avaliable_funds)
        return avaliable_funds

    def click_actions_launch(self):
        sleep(5)
        try:
            button = super().wait_element_to_be_clickable("//button[contains(text(), 'LAUNCH')]")
        except:
            button = self.driver.find_element(By.XPATH,
                                              "//tbody[@id='PracticeAccountListBody']//button[contains(text(), 'FOREX')]")
        button.click()
        Logging().reportDebugStep(self, "Click LAUNCH")
        return CAPage(self.driver)

    def open_finmarket(self):
        sleep(3)
        check_box = self.driver.find_element(By.XPATH, "//*[@id='chbChangePersonalDetails']")
        check_box.click()
        sleep(3)
        check_box = self.driver.find_element(By.XPATH, "//*[@id='chbConfirm']")
        check_box.click()
        sleep(3)
        button = self.driver.find_element(By.XPATH, "//*[@id='btnSubmit']")
        button.click()
        Logging().reportDebugStep(self, "OPEN AN ADDITIONAL ACCOUNT")
        return CAPage(self.driver)

    def close_popup_itrader(self):
        sleep(7)
        continue_btn = super().wait_element_to_be_clickable("//input[@value='Continue']")
        continue_btn.click()
        # check_box = self.driver.find_element(By.XPATH, "//*[@id='chbAgreeNegative']")
        # check_box.click()
        # sleep(3)
        # button = self.driver.find_element(By.XPATH, "//*[@id='btnRiskNextNeg']")
        # button.click()
        Logging().reportDebugStep(self, "Close Success pop up")
        return CAPage(self.driver)

    def fill_questionarie_itrader(self, status, industry, yes, source, estimate_income, estimate_worth, purpose, amount,
                                  incoming_fund, level, time_investing, time_last_trade, instrument, time_experience,
                                  trade_size, applies, price, fb_price, inital_deposit, result_of_trading,
                                  investment_obj, no, tin):
        self.select_employment_status(status)
        self.select_industry(industry)
        self.question_financial_instrument(yes)
        self.check_box_source(source)
        self.check_box_source_total(source)
        self.select_estimate_income(estimate_income)
        self.select_estimate_worth(estimate_worth)
        self.select_purpose(purpose)
        self.select_estimate_amount(amount)
        self.select_incoming_funds(incoming_fund)
        self.select_level(level)
        self.select_time_investing(time_investing)
        self.select_time_last_trade(time_last_trade)
        self.select_instrument(instrument)
        self.select_time_experience(time_experience)
        self.select_trade_size(trade_size)
        self.select_applies(applies)
        self.select_price(price)
        self.select_fb_price(fb_price)
        self.select_inital_deposit(inital_deposit)
        self.select_result_of_trading(result_of_trading)
        self.select_investment_obj(investment_obj)
        self.select_us(no)
        self.enter_tin_itrader(tin)
        # self.select_leverage_itrader(leverage)
        self.select_pep(no)
        self.click_next()

    def select_pep(self, no):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlPep']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlPep']"))
        select.select_by_visible_text(no)
        Logging().reportDebugStep(self, "Select pep No")
        return CAPage(self.driver)

    def click_next(self):
        sleep(3)
        click_next = self.driver.find_element(By.XPATH, "//*[@id='Next']")
        click_next.click()
        Logging().reportDebugStep(self, "Click next")
        return CAPage(self.driver)

    def select_leverage_itrader(self, leverage):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlLeverages']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlLeverages']"))
        select.select_by_visible_text(leverage)
        Logging().reportDebugStep(self, "Select leverage itrader")
        return CAPage(self.driver)

    def enter_tin_itrader(self, tin):
        sleep(3)
        select = self.driver.find_element(By.XPATH, "//*[@id='dnn_ctr608_View_txtTaxTinNumber_1']")
        select.send_keys(tin)
        Logging().reportDebugStep(self, "Enter tin")
        return CAPage(self.driver)

    def select_us(self, no):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlUsaCitizen']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlUsaCitizen']"))
        select.select_by_visible_text(no)
        Logging().reportDebugStep(self, "Enter No US.res")
        return CAPage(self.driver)

    def select_investment_obj(self, investment_obj):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlInvestmentObjectivesStrategy']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlInvestmentObjectivesStrategy']"))
        if global_var.current_brand_name == "gmo":
            select.select_by_visible_text\
                ("I invest in anything I believe will bring high profits even if I risk losing my principal")
        else:
            select.select_by_visible_text(investment_obj)
        Logging().reportDebugStep(self, "Enter investment obj")
        return CAPage(self.driver)

    def select_result_of_trading(self, result_of_trading):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlFeelLostDepositedCapital']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlFeelLostDepositedCapital']"))
        if global_var.current_brand_name == "gmo":
            select.select_by_visible_text\
                ("I would be upset for a while but the loss will not affect my financial situation to a large extent")
        else:
            select.select_by_visible_text(result_of_trading)
        Logging().reportDebugStep(self, "Enter result of trading")
        return CAPage(self.driver)

    def select_inital_deposit(self, inital_deposit):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlBuyingPower']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlBuyingPower']"))
        select.select_by_visible_text(inital_deposit)
        Logging().reportDebugStep(self, "Enter initial deposit")
        return CAPage(self.driver)

    def select_fb_price(self, fb_price):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlFacebookShareDrop']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlFacebookShareDrop']"))
        select.select_by_visible_text(fb_price)
        Logging().reportDebugStep(self, "Enter fb price")
        return CAPage(self.driver)


    def select_price(self, price):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlPositiveFinancialReportAffect']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlPositiveFinancialReportAffect']"))
        select.select_by_visible_text(price)
        Logging().reportDebugStep(self, "Enter price")
        return CAPage(self.driver)

    def select_applies(self, applies):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlTradingWithLeverage']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlTradingWithLeverage']"))
        select.select_by_visible_text(applies)
        Logging().reportDebugStep(self, "Enter applies")
        return CAPage(self.driver)


    def select_trade_size(self, trade_size):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlLastYearTotalVolume']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlLastYearTotalVolume']"))
        if global_var.current_brand_name == "gmo":
            select.select_by_visible_text("Less than €3,000 in Stocks/Cryptos and/or €12,500 in Forex/Commodities")
        else:
            select.select_by_visible_text(trade_size)
        Logging().reportDebugStep(self, "Enter trade size")
        return CAPage(self.driver)


    def select_time_experience(self, time_experience):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlExperienceInDerivativeProducts']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlExperienceInDerivativeProducts']"))
        select.select_by_visible_text(time_experience)
        Logging().reportDebugStep(self, "Enter time experience")
        return CAPage(self.driver)


    def select_instrument(self, instrument):
        sleep(5)
        submit = super().wait_load_element(
            "//*[@id='cblTradesInPast']/li[1]/label[contains(text(), 'Stocks/Shares, Indices, Commodities ')]")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click check box " + instrument)
        return CAPage(self.driver)


    def select_time_last_trade(self, time_last_trade):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlLastTradeCarriedOut']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlLastTradeCarriedOut']"))
        select.select_by_visible_text(time_last_trade)
        Logging().reportDebugStep(self, "Enter time last trade")
        return CAPage(self.driver)


    def select_time_investing(self, time_investing):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlTimeOfInvesting']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlTimeOfInvesting']"))
        select.select_by_visible_text(time_investing)
        Logging().reportDebugStep(self, "Enter time investing")
        return CAPage(self.driver)


    def select_level(self, level):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlLevelOfEducation']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlLevelOfEducation']"))
        select.select_by_visible_text(level)
        Logging().reportDebugStep(self, "Enter level")
        return CAPage(self.driver)

    def select_incoming_funds(self, incoming_fund):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlExpectedOriginOfIncomingFunds']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlExpectedOriginOfIncomingFunds']"))
        select.select_by_visible_text(incoming_fund)
        Logging().reportDebugStep(self, "Enter incoming fund")
        return CAPage(self.driver)

    def select_estimate_amount(self, amount):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlEstimateAmountInvestYearly']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlEstimateAmountInvestYearly']"))
        select.select_by_visible_text(amount)
        Logging().reportDebugStep(self, "Enter amount")
        return CAPage(self.driver)

    def select_purpose(self, purpose):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlRequestingTradingAccount']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlRequestingTradingAccount']"))
        if global_var.current_brand_name == "gmo":
            select.select_by_visible_text("Long-term investment")
        else:
            select.select_by_visible_text(purpose)
        Logging().reportDebugStep(self, "Enter purpose")
        return CAPage(self.driver)

    def select_estimate_worth(self, estimate_worth):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlEstimatedNetWorth']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlEstimatedNetWorth']"))
        select.select_by_visible_text(estimate_worth)
        Logging().reportDebugStep(self, "Enter estimate worth")
        return CAPage(self.driver)

    def select_estimate_income(self, estimate_income):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlEstimatedAnnualIncome']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlEstimatedAnnualIncome']"))
        select.select_by_visible_text(estimate_income)
        Logging().reportDebugStep(self, "Enter estimate income")
        return CAPage(self.driver)

    def check_box_source_total(self, source):
        sleep(5)
        submit = super().wait_load_element("//*[@id='cblTotalWealth']/li[1]/label[contains(text(), 'Savings and investments ')]")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click check box " + source)
        return CAPage(self.driver)

    def check_box_source(self, source):
        sleep(5)
        submit = super().wait_load_element("//*[@id='cblSourceOfFunds']/li[1]/label[contains(text(), 'Savings and investments ')]")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click check box " + source)
        return CAPage(self.driver)

    def question_financial_instrument(self, yes):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlTradingKnowledge']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlTradingKnowledge']"))
        select.select_by_visible_text(yes)
        Logging().reportDebugStep(self, "Enter status")
        return CAPage(self.driver)

    def select_industry(self, industry):
        sleep(5)
        submit = super().wait_load_element("//*[@id='cblIndustry_0']")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click check box " + industry)
        return CAPage(self.driver)

    def select_employment_status(self, status):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlEmploymentStatus']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlEmploymentStatus']"))
        select.select_by_visible_text(status)
        Logging().reportDebugStep(self, "Enter status")
        return CAPage(self.driver)

    def fill_questionarie_triomarket(self,amount, purpose,anticipated, expirience, level,
                                     gloss, employment, worth, source, work, relate, yes, no,
                                     last_transaction, amount_select, invested_volume, knowledge,
                                     account, risk, tin):
        self.enter_amount(amount)
        self.enter_purpose(purpose)
        self.enter_anticipated(anticipated)
        self.enter_expirience(expirience)
        self.enter_level(level)
        self.enter_gloss(gloss)
        self.enter_employment(employment)
        self.enter_worth(worth)
        self.enter_source_trio(source)
        self.enter_work(work)
        self.enter_relate(relate)
        self.continue_click_trio()
        ## 2 step
        self.cfds(yes)
        self.margin(yes)
        self.stocks(yes)
        self.last_transaction(last_transaction)
        self.amount(amount_select)
        self.invested_volume(invested_volume)
        self.knowledge(knowledge)
        self.account(account)
        self.risk(risk)
        # self.us_reportable_person(no)
        self.enter_tin_trio(tin)
        self.check_box_updates()
        self.check_box_policy()
        self.check_box_correct_information()
        self.continue_click_trio_2_step()
        Logging().reportDebugStep(self, "Finished fill questionarie")
        return CAPage(self.driver)

    def check_box_correct_information(self):
        sleep(5)
        submit = super().wait_load_element("//*[@id='cbTrueInfo']")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click check box correct information")
        return CAPage(self.driver)

    def check_box_policy(self):
        sleep(5)
        submit = super().wait_load_element("//*[@id='cbTerms']")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click check box policy")
        return CAPage(self.driver)

    def check_box_updates(self):
        sleep(5)
        submit = super().wait_load_element("//*[@id='cbNews']")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click check box updates")
        return CAPage(self.driver)

    def enter_tin_trio(self, tin):
        sleep(3)
        funds_input = self.driver.find_element(By.XPATH, "//*[@id='TIN_Number']")
        funds_input.send_keys(tin)
        Logging().reportDebugStep(self, "Enter tin")
        return CAPage(self.driver)

    def risk(self, risk):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlMinimizeRisk']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlMinimizeRisk']"))
        select.select_by_visible_text(risk)
        Logging().reportDebugStep(self, "Enter risk")
        return CAPage(self.driver)

    def account(self, account):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlAccountWithBalance']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlAccountWithBalance']"))
        select.select_by_visible_text(account)
        Logging().reportDebugStep(self, "Enter account")
        return CAPage(self.driver)

    def knowledge(self, knowledge):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlOtherKnowledgeOrExperience']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlOtherKnowledgeOrExperience']"))
        select.select_by_visible_text(knowledge)
        Logging().reportDebugStep(self, "Enter knowledge")
        return CAPage(self.driver)

    def invested_volume(self, volume):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlAnnualAverageInvested']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlAnnualAverageInvested']"))
        select.select_by_visible_text(volume)
        Logging().reportDebugStep(self, "Enter invested volume")
        return CAPage(self.driver)

    def amount(self, amount_select):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlAnnualAverageAmount']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlAnnualAverageAmount']"))
        select.select_by_visible_text(amount_select)
        Logging().reportDebugStep(self, "Enter amount")
        return CAPage(self.driver)

    def last_transaction(self, transaction):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlLastTransaction']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlLastTransaction']"))
        select.select_by_visible_text(transaction)
        Logging().reportDebugStep(self, "Enter last transaction")
        return CAPage(self.driver)

    def stocks(self, yes):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlFamiliarWithTransferrable']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlFamiliarWithTransferrable']"))
        select.select_by_visible_text(yes)
        Logging().reportDebugStep(self, "Enter stocks")
        return CAPage(self.driver)

    def margin(self, yes):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlFamiliarWithProducts']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlFamiliarWithProducts']"))
        select.select_by_visible_text(yes)
        Logging().reportDebugStep(self, "Enter margin")
        return CAPage(self.driver)

    def cfds(self, yes):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlFamiliarWithCFD']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlFamiliarWithCFD']"))
        select.select_by_visible_text(yes)
        Logging().reportDebugStep(self, "Enter cfds")
        return CAPage(self.driver)

    def continue_click_trio(self):
        sleep(5)
        submit = super().wait_load_element("//*[@id='questionGroup2']/div[14]/a[2]")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click Continue")
        return CAPage(self.driver)

    def continue_click_trio_2_step(self):
        sleep(5)
        submit = super().wait_load_element("//*[@id='btnNext2']")
        # submit.click()
        self.driver.execute_script("arguments[0].click();", submit)
        Logging().reportDebugStep(self, "Click Continue")
        return CAPage(self.driver)

    def enter_source_trio(self, source):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlFundsSource']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlFundsSource']"))
        select.select_by_visible_text(source)
        Logging().reportDebugStep(self, "Enter source")
        return CAPage(self.driver)

    def enter_relate(self, relate):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlShareHome']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlShareHome']"))
        select.select_by_visible_text(relate)
        Logging().reportDebugStep(self, "Enter relate")
        return CAPage(self.driver)

    def enter_work(self, work):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlWorkForTheFollowing']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlWorkForTheFollowing']"))
        select.select_by_visible_text(work)
        Logging().reportDebugStep(self, "Enter work")
        return CAPage(self.driver)

    def enter_worth(self, worth):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlNetWorth']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlNetWorth']"))
        select.select_by_visible_text(worth)
        Logging().reportDebugStep(self, "Enter worth")
        return CAPage(self.driver)

    def enter_employment(self, employment):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlEmployment']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlEmployment']"))
        select.select_by_visible_text(employment)
        Logging().reportDebugStep(self, "Enter employment")
        return CAPage(self.driver)

    def enter_gloss(self, gloss):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlEstimatedGrossIncome']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlEstimatedGrossIncome']"))
        select.select_by_visible_text(gloss)
        Logging().reportDebugStep(self, "Enter gloss")
        return CAPage(self.driver)

    def enter_amount(self, amount):
        sleep(3)
        amount_input = self.driver.find_element(By.XPATH, "//*[@id='InvestmentAmount']")
        amount_input.send_keys(amount)
        Logging().reportDebugStep(self, "Enter amount")
        return CAPage(self.driver)

    def enter_purpose(self, purpose):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlPurposeBusiness']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlPurposeBusiness']"))
        select.select_by_visible_text(purpose)
        Logging().reportDebugStep(self, "Enter purpose")
        return CAPage(self.driver)

    def enter_anticipated(self, anticipated):
        sleep(3)
        amount_input = self.driver.find_element(By.XPATH, "//*[@id='txtAnticipated']")
        amount_input.send_keys(anticipated)
        Logging().reportDebugStep(self, "Enter anticipated")
        return CAPage(self.driver)

    def enter_expirience(self, expirience):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlTradingExp']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlTradingExp']"))
        select.select_by_visible_text(expirience)
        Logging().reportDebugStep(self, "Enter expirience")
        return CAPage(self.driver)

    def enter_level(self, level):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlEducationLevel']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlEducationLevel']"))
        select.select_by_visible_text(level)
        Logging().reportDebugStep(self, "Enter level")
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
        Logging().reportDebugStep(self, "Enter tin")
        return CAPage(self.driver)

    def enter_pep(self, pep):
        sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id = 'ddlPoliticallyPerson']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id = 'ddlPoliticallyPerson']"))
        select.select_by_visible_text(pep)
        Logging().reportDebugStep(self, "Enter pep")
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
        Logging().reportDebugStep(self, "Get status: " + status)
        return status

    def verify_ticket_status(self):
        status = super().wait_load_element("//*[@id='openTickets']/tbody/tr/td[4]").text
        Logging().reportDebugStep(self, "Get status: " + status)
        return status

    def get_ticket_number(self):
        ticket_number = super().wait_load_element("//*[@id='lblSuccessMessage']").text
        Logging().reportDebugStep(self, "Get ticket number: " + ticket_number)
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
        try:
            service_desk = super().wait_load_element("//*[@id='mainmenu']/li[2]/a")
            self.driver.execute_script("arguments[0].click();", service_desk)
            Logging().reportDebugStep(self, "Click Open Service Desk")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "There is no 'Service Desk' button")
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
        self.driver.execute_script("arguments[0].click();", my_account_button)
        # my_account_button.click()
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
        # select.click()
        self.driver.execute_script("arguments[0].click();", select)
        select_leverage = super().wait_load_element("//select[@id='SelLeverageP']/option[1]")
        self.driver.execute_script("arguments[0].click();", select_leverage)
        Logging().reportDebugStep(self, "Select USD currency")
        return CAPage(self.driver)

    def select_deposit(self):
        sleep(3)
        input = super().wait_load_element("//*[@id='TextInitialDepositP']")
        input.clear()
        input.send_keys("500000")
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
        sleep(0.3)
        click_submit = super().wait_load_element("//input[@class= 'green_btn popup_mod_btn centered']", timeout=35)
        try:
            self.driver.execute_script("arguments[0].click();", click_submit)
        except:
            click_submit.click()
        Logging().reportDebugStep(self, "Click Finish")
        return CAPage(self.driver)
