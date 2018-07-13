from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.parser.ParserDate import ParserDate


class CaPersonalInformationTab(BrandBasePage):
    date_parser = None
    month_parser = None
    year_parser = None

    def __init__(self):
        super().__init__()

    def perform_change_personal_information(self, first_name, last_name, day, month, year, country, citizenship, city,
                                            zip_code, address, phone):
        global date_parser
        global month_parser
        global year_parser

        date_parser = day
        month_parser = month
        year_parser = year

        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.select_day(day)
        self.select_month(month)
        self.select_year(year)
        self.select_citizenship(citizenship)
        self.select_country(country)
        self.set_city(city)
        self.set_zip_code(zip_code)
        self.set_address(address)
        self.set_phone(phone)
        return CaPersonalInformationTab()

    def set_first_name(self, name):
        first_name_field = self.driver.find_element(By.XPATH, "// input[ @ name = 'firstName']")
        first_name_field.clear()
        first_name_field.send_keys(name)
        Logging().reportDebugStep(self, "The first name was set:" + name)
        return CaPersonalInformationTab()

    def set_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The last name was set:" + last_name)
        return CaPersonalInformationTab()

    def select_day(self, day):
        drop_down_day = self.driver.find_element(By.XPATH, "//custom-select[@name='day']")
        drop_down_day.click()

        sleep(1)
        select_day = self.driver.find_element(By.XPATH, "//custom-select[@name= 'day']//"
                                                        "following-sibling::span[contains(text(),'%s')]" % day)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_day)
        select_day.click()
        Logging().reportDebugStep(self, "The day was set:" + day)
        return CaPersonalInformationTab()

    def select_month(self, month):
        drop_down_month = self.driver.find_element(By.XPATH, "//custom-select[@name='month']")
        drop_down_month.click()
        sleep(1)
        select_month = self.driver.find_element(By.XPATH, "//custom-select[@name= 'month']//"
                                                          "following-sibling::span[contains(text(),'%s')]" % month)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_month)
        select_month.click()
        Logging().reportDebugStep(self, "The month was set:" + month)
        return CaPersonalInformationTab()

    def select_year(self, year):
        drop_down_year = self.driver.find_element(By.XPATH, "//custom-select[@name='year']")
        drop_down_year.click()
        sleep(1)

        select_year = self.driver.find_element(By.XPATH, "//custom-select[@name= 'year']//"
                                                         "following-sibling::span[contains(text(),'%s')]" % year)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_year)
        select_year.click()
        Logging().reportDebugStep(self, "The year was set:" + year)
        return CaPersonalInformationTab()

    def select_country(self, country):
        drop_down_country = self.driver.find_element(By.XPATH, "//custom-select[@name='country']")
        drop_down_country.click()
        sleep(2)
        select_country = self.driver.find_element(By.XPATH,
                                                  "//custom-select[@name='country']//following-sibling::*[contains(text(),'%s')]" % country)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_country)

        select_country.click()
        Logging().reportDebugStep(self, "The country was set:" + country)
        return CaPersonalInformationTab()

    def select_citizenship(self, citizenship):
        drop_down_citizenship = self.driver.find_element(By.XPATH, "//custom-select[@name='citizenship']")
        drop_down_citizenship.click()
        sleep(2)
        select_citizenship = self.driver.find_element(By.XPATH,
                                                      "//custom-select[@name='citizenship']//"
                                                      "following-sibling::*[contains(text(),'%s')]" % citizenship)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_citizenship)
        select_citizenship.click()
        Logging().reportDebugStep(self, "The citizenship was set:" + citizenship)
        return CaPersonalInformationTab()

    def set_city(self, city):
        field_city = self.driver.find_element(By.XPATH, "//input[@name='city']")
        field_city.clear()
        field_city.send_keys(city)
        Logging().reportDebugStep(self, "The city was set:" + city)
        return CaPersonalInformationTab()

    def set_post_code(self, post_code):
        field_post_code = self.driver.find_element(By.XPATH, "//input[@name='postCode']")
        field_post_code.clear()
        field_post_code.send_keys(post_code)
        Logging().reportDebugStep(self, "The post code was set:" + post_code)
        return CaPersonalInformationTab()

    def set_address(self, address):
        field_address = self.driver.find_element(By.XPATH, "//input[@name='address']")
        field_address.clear()
        field_address.send_keys(address)
        Logging().reportDebugStep(self, "The address was set:" + address)
        return CaPersonalInformationTab()

    def set_phone(self, phone):
        field_phone = self.driver.find_element(By.XPATH, "//input[@name='phone']")
        field_phone.clear()
        field_phone.send_keys(phone)
        Logging().reportDebugStep(self, "The phone was set:" + phone)
        return CaPersonalInformationTab()

    def perform_save_changed(self):
        save_button = self.driver.find_element(By.XPATH, "//button[@class='forex-button-pandats']")
        save_button.click()
        Logging().reportDebugStep(self, "Perform change of personal information")
        return CaPersonalInformationTab()

    def set_zip_code(self, zip_code):
        field_phone = self.driver.find_element(By.XPATH, "//input[@name='postCode']")
        field_phone.clear()
        field_phone.send_keys(zip_code)
        Logging().reportDebugStep(self, "The zip code was set:" + zip_code)
        return CaPersonalInformationTab()

    def get_date_birthday(self):
        date = year_parser + ParserDate().get_month_number(month_parser) + date_parser
        Logging().reportDebugStep(self, "Returns the date of birthday" + date)
        return date

    def get_first_name(self):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//div[@class='form-group-pandats']//input[@name='firstName']")
        Logging().reportDebugStep(self, "Returns the first name" + first_name_field.text)
        return first_name_field.text

    def get_last_name(self):
        last_name_field = self.driver.find_element(By.XPATH, "//input[@name = 'lastName']")
        Logging().reportDebugStep(self, "Returns the last name" + last_name_field.text)
        return last_name_field.text

    def get_date_of_birthday(self):
        date = self.driver.find_element(By.XPATH, "//custom-select[@name= 'day']")
        month = self.driver.find_element(By.XPATH, "//custom-select[@name= 'month']")
        year = self.driver.find_element(By.XPATH, "//custom-select[@name= 'year']")
        date = year.text + ParserDate().get_month_number(month.text) + date.text
        Logging().reportDebugStep(self, "Returns the date of birthday" + date)
        return date

    def get_country_text(self):
        country = self.driver.find_element(By.XPATH, "//custom-select[@name='country']")
        Logging().reportDebugStep(self, "Returns the country " + country.text)
        return country.text

    def get_citizen_ship_text(self):
        citizen = self.driver.find_element(By.XPATH, "//custom-select[@name='citizenship']")
        Logging().reportDebugStep(self, "Returns the citizen ship " + citizen.text)
        return citizen.text
