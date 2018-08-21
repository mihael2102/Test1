from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging


class CaChangePasswordTab(BrandBasePage):
    def __init__(self):
        super().__init__()

    def perform_change_password(self, old_password, new_password):
        old_password_field = super().wait_load_element_present("//input[@name='oldPassword']")
        old_password_field.send_keys(old_password)
        Logging().reportDebugStep(self,
                                  "Enter the  old password in the field :  " + old_password)
        new_password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        new_password_field.send_keys(new_password)
        Logging().reportDebugStep(self,
                                  "Enter the new password in the field :  " + new_password)
        repeat_password = self.driver.find_element(By.XPATH, "//input[@name='passwordConfirm']")
        repeat_password.send_keys(new_password)
        repeat_password = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save Changes')]")
        Logging().reportDebugStep(self,
                                  "Enter the confirmation of the new password in the field  : " + new_password)
        repeat_password.click()
        Logging().reportDebugStep(self,
                                  "Password changed successfully, new password is: " + new_password)
        return CaChangePasswordTab()

    def close_client_area_pop_up(self):
        super().close_client_area_pop_up()
        Logging().reportDebugStep(self,
                                  "Pop up the client area was closed")
        return CaChangePasswordTab()

    def refreshing_wait(self):
        super().refreshing_wait()
        Logging().reportDebugStep(self, "Page refreshed")
        return CaChangePasswordTab()

    def get_password_changed(self):
        password_changed = super().wait_element_to_be_clickable("//div[@class='toast-content-pandats']")
        Logging().reportDebugStep(self, "Returns a confirmation message: " + password_changed.text)
        return password_changed.text
