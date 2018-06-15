from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.pages.trading_platform.BrandTradingPlatformPage import BrandTradingPlatformPage

class BrandSignUpForm(BrandBasePage):

    def __init__(self):
        super().__init__()

    def set_email(self, email):
        self.email_locator = self.driver.find_element(By.XPATH, "//input[@name='email']")
        self.email_locator.clear()
        self.email_locator.send_keys(email)
        return BrandSignUpForm()

    def set_password(self, password):
        password_locator = self.driver.find_element(By.XPATH, "//*[@name='password']")
        password_locator.clear()
        password_locator.send_keys(password)
        return BrandSignUpForm()

    def set_confirm_password(self, confirm_password):
        confirmLocator = self.driver.find_element(By.XPATH, "//*[@name='passwordConfirm']")
        confirmLocator.clear()
        confirmLocator.send_keys(confirm_password)
        return BrandSignUpForm()

    def set_promo_code(self, promo_code):
        promo_code_locator = self.driver.find_element(By.XPATH, "//*[@placeholder='Enter Promocode']")
        promo_code_locator.clear()
        promo_code_locator.send_keys(promo_code)
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
        return BrandSignUpForm()

    def set_check_box(self):
        checkBoxLocator = self.driver.find_element(By.XPATH, "//label[@class='terms-pandats']")
        checkBoxLocator.click()
        return BrandSignUpForm()

    def sign_up_button(self):
        submitLocator = self.driver.find_element(By.XPATH,
                                                      "//button[@class='forex-button-pandats signup-button-pandats']")

        submitLocator.click()
        return BrandTradingPlatformPage()
