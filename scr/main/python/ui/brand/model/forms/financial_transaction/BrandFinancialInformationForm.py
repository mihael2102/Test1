from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from scr.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from scr.main.python.ui.brand.model.forms.trading_experience.BrandTradingExperienceForm import \
    BrandTradingExperienceForm


class BrandFinancialInformationForm(BrandBasePage):
    def __init__(self):
        super().__init__()

    def select_annual_income(self, annual_income):
        drop_down_annual_income = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//custom-select[@name='annualIncome']")))
        drop_down_annual_income.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'annualIncome']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % annual_income)
        select.click()
        return BrandFinancialInformationForm()

    def select_employye_status(self, employment_status):
        drop_down_employye_status = self.driver.find_element(By.XPATH, "//custom-select[@name='employmentStatus']")
        drop_down_employye_status.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'employmentStatus']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % employment_status)
        select.click()
        return BrandFinancialInformationForm()

    def select_risk(self, investment_knowledge):
        drop_down_annual_income = self.driver.find_element(By.XPATH, "//custom-select[@name='investmentKnowledge']")
        drop_down_annual_income.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'investmentKnowledge']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % investment_knowledge)
        select.click()
        return BrandFinancialInformationForm()

    def select_average_trade(self, atv):
        drop_down_average_trade = self.driver.find_element(By.XPATH, "//custom-select[@name='atv']")
        drop_down_average_trade.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'atv']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % atv)
        select.click()
        return BrandFinancialInformationForm()

    def select_saving_investment(self, saving_investment):
        drop_down_saving_investment = self.driver.find_element(By.XPATH, "//custom-select[@name='savingInvestment']")
        drop_down_saving_investment.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'savingInvestment']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % saving_investment)
        select.click()
        return BrandFinancialInformationForm()

    def enter_next_button(self):
        super().wait_load_element("//custom-select[@name='annualIncome']")
        next_button = self.driver.find_element(By.XPATH, "//button[@class='forex-button-pandats']")
        next_button.click()
        return BrandTradingExperienceForm()
