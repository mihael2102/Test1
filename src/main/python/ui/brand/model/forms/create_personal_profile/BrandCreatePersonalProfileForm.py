from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.forms.financial_transaction.BrandFinancialInformationForm import \
    BrandFinancialInformationForm
from src.main.python.utils.logs.Loging import Logging


class BrandCreatePersonalProfileForm(BrandBasePage):

    def __init__(self):
        super().__init__()

    def set_first_name(self, name):
        first_name_field = self.driver.find_element(By.XPATH, "// input[ @ name = 'firstName']")
        first_name_field.clear()
        first_name_field.send_keys(name)
        return BrandCreatePersonalProfileForm()

    def set_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The last name was set"+last_name)
        return BrandCreatePersonalProfileForm()

    def select_day(self, day):
        drop_down_day = self.driver.find_element(By.XPATH, "//custom-select[@name='day']")
        drop_down_day.click()

        #sleep(1)
        select_day = super().wait_element_to_be_clickable("//custom-select[@name= 'day']//"
                                                        "following-sibling::span[contains(text(),'%s')]" % day)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_day)
        select_day.click()
        Logging().reportDebugStep(self, "The day was set" + day)
        return BrandCreatePersonalProfileForm()

    def select_month(self, month):
        drop_down_month = self.driver.find_element(By.XPATH, "//custom-select[@name='month']")
        drop_down_month.click()
        #sleep(1)
        select_month = super().wait_element_to_be_clickable("//custom-select[@name= 'month']//"
                                                          "following-sibling::span[contains(text(),'%s')]" % month)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_month)
        select_month.click()
        Logging().reportDebugStep(self, "The month was set" + month)
        return BrandCreatePersonalProfileForm()

    def select_year(self, year):
        drop_down_year = self.driver.find_element(By.XPATH, "//custom-select[@name='year']")
        drop_down_year.click()
        #sleep(1)

        select_year = super().wait_element_to_be_clickable("//custom-select[@name= 'year']//"
                                                         "following-sibling::span[contains(text(),'%s')]" % year)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_year)
        select_year.click()
        Logging().reportDebugStep(self, "The year was set" + year)
        return BrandCreatePersonalProfileForm()

    def select_country(self, country):
        drop_down_country = self.driver.find_element(By.XPATH, "//custom-select[@name='country']")
        drop_down_country.click()
        #sleep(1)
        select_country = super().wait_element_to_be_clickable(
                                                  "//custom-select[@name='country']//following-sibling::*[contains(text(),'%s')]" % country)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_country)

        select_country.click()
        Logging().reportDebugStep(self, "The country was set" + country)
        return BrandCreatePersonalProfileForm()

    def select_currency(self, currency):
        drop_down_currency = self.driver.find_element(By.XPATH, "//custom-select[@name='currency']")
        drop_down_currency.click()
        #sleep(1)
        select_currency = super().wait_element_to_be_clickable(
                                                   "//custom-select[@name= 'currency']//"
                                                   "following-sibling::*[contains(text(),'%s')]" % currency)
        self.driver.execute_script("arguments[0].scrollIntoView();", select_currency)
        select_currency.click()
        Logging().reportDebugStep(self, "The currency was set" + currency)
        return BrandCreatePersonalProfileForm()

    def select_citizenship(self, citizenship):
        drop_down_citizenship = self.driver.find_element(By.XPATH, "//custom-select[@name='citizenship']")
        drop_down_citizenship.click()
        #sleep(1)
        select_citizenship = super().wait_element_to_be_clickable(
                                                      "//custom-select[@name='citizenship']//"
                                                      "following-sibling::*[contains(text(),'%s')]" % citizenship)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_citizenship)
        select_citizenship.click()
        Logging().reportDebugStep(self, "The citizenship was set" + citizenship)
        return BrandCreatePersonalProfileForm()

    def set_city(self, city):
        field_city = self.driver.find_element(By.XPATH, "//input[@name='city']")
        field_city.clear()
        field_city.send_keys(city)
        Logging().reportDebugStep(self, "The city was set" + city)
        return BrandCreatePersonalProfileForm()

    def set_post_code(self, post_code):
        field_post_code = self.driver.find_element(By.XPATH, "//input[@name='postCode']")
        field_post_code.clear()
        field_post_code.send_keys(post_code)
        Logging().reportDebugStep(self, "The post_code was set" + post_code)
        return BrandCreatePersonalProfileForm()

    def set_address(self, address):
        field_address = self.driver.find_element(By.XPATH, "//input[@name='address']")
        field_address.clear()
        field_address.send_keys(address)
        Logging().reportDebugStep(self, "The address was set" + address)
        return BrandCreatePersonalProfileForm()

    def set_phone(self, phone):
        field_phone = self.driver.find_element(By.XPATH, "//input[@name='phone']")
        field_phone.clear()
        field_phone.send_keys(phone)
        Logging().reportDebugStep(self, "The phone was set" + phone)
        return BrandCreatePersonalProfileForm()

    def enter_next_button(self):
        next_button = self.driver.find_element(By.XPATH, "//button[@class='forex-button-pandats']")
        next_button.click()
        Logging().reportDebugStep(self, "the next button was clicked")
        return BrandFinancialInformationForm()
