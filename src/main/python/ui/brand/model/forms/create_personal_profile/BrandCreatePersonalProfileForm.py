from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.forms.financial_transaction.BrandFinancialInformationForm import \
    BrandFinancialInformationForm


class BrandCreatePersonalProfileForm(BrandBasePage):

    def __init__(self):
        super().__init__()

    def set_first_name(self, name):
        first_name_field = self.driver.find_element(By.XPATH, "// input[ @ name = 'firstName']")
        first_name_field.send_keys(name)
        return BrandCreatePersonalProfileForm()

    def set_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
        last_name_field.send_keys(last_name)
        return BrandCreatePersonalProfileForm()

    def select_day(self, day):
        drop_down_day = self.driver.find_element(By.XPATH, "//custom-select[@name='day']")
        drop_down_day.click()

        sleep(1)
        select_day = self.driver.find_element(By.XPATH, "//custom-select[@name= 'day']//"
                                                        "following-sibling::span[contains(text(),'%s')]" % day)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_day)
        select_day.click()
        return BrandCreatePersonalProfileForm()

    def select_month(self, month):
        drop_down_month = self.driver.find_element(By.XPATH, "//custom-select[@name='month']")
        drop_down_month.click()
        sleep(1)
        select_month = self.driver.find_element(By.XPATH, "//custom-select[@name= 'month']//"
                                                          "following-sibling::span[contains(text(),'%s')]" % month)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_month)
        select_month.click()
        return BrandCreatePersonalProfileForm()

    def select_year(self, year):
        drop_down_year = self.driver.find_element(By.XPATH, "//custom-select[@name='year']")
        drop_down_year.click()
        sleep(1)

        select_year = self.driver.find_element(By.XPATH, "//custom-select[@name= 'year']//"
                                                         "following-sibling::span[contains(text(),'%s')]" % year)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_year)
        select_year.click()

        return BrandCreatePersonalProfileForm()

    def select_country(self, country):
        drop_down_country = self.driver.find_element(By.XPATH, "//custom-select[@name='country']")
        drop_down_country.click()
        sleep(1)
        select_country = self.driver.find_element(By.XPATH,
                                                  "//custom-select[@name='country']//following-sibling::*[contains(text(),'%s')]" % country)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_country)

        select_country.click()

        return BrandCreatePersonalProfileForm()

    def select_currency(self, currency):
        drop_down_currency = self.driver.find_element(By.XPATH, "//custom-select[@name='currency']")
        drop_down_currency.click()
        sleep(1)
        select_currency = self.driver.find_element(By.XPATH,
                                                   "//custom-select[@name= 'currency']//"
                                                   "following-sibling::*[contains(text(),'%s')]" % currency)
        self.driver.execute_script("arguments[0].scrollIntoView();", select_currency)
        select_currency.click()
        return BrandCreatePersonalProfileForm()

    def select_citizenship(self, citizenship):
        drop_down_citizenship = self.driver.find_element(By.XPATH, "//custom-select[@name='citizenship']")
        drop_down_citizenship.click()
        sleep(1)
        select_citizenship = self.driver.find_element(By.XPATH,
                                                      "//custom-select[@name='citizenship']//"
                                                      "following-sibling::*[contains(text(),'%s')]" % citizenship)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_citizenship)
        select_citizenship.click()
        return BrandCreatePersonalProfileForm()

    def set_city(self, city):
        field_city = self.driver.find_element(By.XPATH, "//input[@name='city']")
        field_city.clear()
        field_city.send_keys(city)
        return BrandCreatePersonalProfileForm()

    def set_post_code(self, post_code):
        field_post_code = self.driver.find_element(By.XPATH, "//input[@name='postCode']")
        field_post_code.clear()
        field_post_code.send_keys(post_code)
        return BrandCreatePersonalProfileForm()

    def set_address(self, address):
        field_address = self.driver.find_element(By.XPATH, "//input[@name='address']")
        field_address.clear()
        field_address.send_keys(address)
        return BrandCreatePersonalProfileForm()

    def set_phone(self, phone):
        field_phone = self.driver.find_element(By.XPATH, "//input[@name='phone']")
        field_phone.clear()
        field_phone.send_keys(phone)
        return BrandCreatePersonalProfileForm()

    def enter_next_button(self):
        next_button = self.driver.find_element(By.XPATH, "//button[@class='forex-button-pandats']")
        next_button.click()
        return BrandFinancialInformationForm()
