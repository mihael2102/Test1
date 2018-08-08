from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.pages.trading_platform.BrandTradingPlatformPage import BrandTradingPlatformPage
from src.main.python.utils.logs.Loging import Logging


class BrandSignUpForm(BrandBasePage):

    def __init__(self):
        super().__init__()

    def set_email(self, email):
        self.email_locator = self.driver.find_element(By.XPATH, "//input[@name='email']")
        self.email_locator.clear()
        self.email_locator.send_keys(email)
        Logging().reportDebugStep(self, "The email was set: " + email)
        return BrandSignUpForm()

    def set_password(self, password):
        password_locator = self.driver.find_element(By.XPATH, "//*[@name='password']")
        password_locator.clear()
        password_locator.send_keys(password)
        Logging().reportDebugStep(self, "The password was set: " + password)
        return BrandSignUpForm()

    def set_confirm_password(self, confirm_password):
        confirmLocator = self.driver.find_element(By.XPATH, "//*[@name='passwordConfirm']")
        confirmLocator.clear()
        confirmLocator.send_keys(confirm_password)
        Logging().reportDebugStep(self, "The confirm password was set: " + confirm_password)
        return BrandSignUpForm()

    def set_promo_code(self, promo_code):
        promo_code_locator = self.driver.find_element(By.XPATH, "//*[@placeholder='Enter Promocode']")
        promo_code_locator.clear()
        promo_code_locator.send_keys(promo_code)
        Logging().reportDebugStep(self, "The promo code was set: " + promo_code)
        return BrandSignUpForm()

    def set_country(self, country):
        change_country_locator = self.driver.find_element(By.XPATH,
                                                          "//div[@class='country-pandats']//following-sibling::a")
        change_country_locator.click()
        exist_counter_locator = self.driver.find_element(By.XPATH, "//div[@class='content-pandats']//ul")
        search_locator = self.driver.find_element(By.XPATH,
                                                  "//div[@class='search-pandats']//following-sibling::input")

        search_locator.send_keys(country)
        exist_counter_locator.click()
        Logging().reportDebugStep(self, "The country was set: " + country)
        return BrandSignUpForm()

    def set_check_box(self):
        check_box_locator = self.driver.find_element(By.XPATH, "//div[@class='content-popup-pandats']//div[6]/label")
        check_box_locator.click()
        Logging().reportDebugStep(self, "The check box was set")
        return BrandSignUpForm()

    def set_accept_check_box(self):
        check_box_locator = self.driver.find_element(By.XPATH, "//div[@class='content-popup-pandats']//div[6]/label")
        check_box_locator.click()
        Logging().reportDebugStep(self, "The check box was set")
        return BrandSignUpForm()

    def set_first_name(self, name):
        first_name_field = self.driver.find_element(By.XPATH, "// input[ @ name = 'firstName']")
        first_name_field.send_keys(name)
        return BrandSignUpForm()

    def set_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The last name was set"+last_name)
        return BrandSignUpForm()

    def sign_up_button(self):
        submit_locator = self.driver.find_element(By.XPATH,
                                                 "//button[@class='forex-button-pandats signup-button-pandats']")

        submit_locator.click()
        Logging().reportDebugStep(self, "The sign up button was clicked")
        return BrandTradingPlatformPage()
