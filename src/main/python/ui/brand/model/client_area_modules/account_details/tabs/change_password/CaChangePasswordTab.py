from selenium.webdriver.common.by import By

from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class CaChangePasswordTab(BrandBasePage):
    def __init__(self):
        super().__init__()

    def perform_change_password(self, old_password, new_password):
        old_password_field = super().wait_load_element("//input[@name='oldPassword']")
        old_password_field.send_keys(old_password)
        new_password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        new_password_field.send_keys(new_password)
        repeat_password = self.driver.find_element(By.XPATH, "//input[@name='passwordConfirm']")
        repeat_password.send_keys(new_password)
        repeat_password = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save Changes')]")
        repeat_password.click()
        return CaChangePasswordTab()


    def close_client_area_pop_up(self):
        super().close_client_area_pop_up()
        return CaChangePasswordTab()

    def refreshing_wait(self):
        super().refreshing_wait()
        return CaChangePasswordTab()

    def get_password_changed(self):
        password_changed = self.driver.find_element(By.XPATH, "//div[@class='toast-content-pandats']")
        return password_changed.text
