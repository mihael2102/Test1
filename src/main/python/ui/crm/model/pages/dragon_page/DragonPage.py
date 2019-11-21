from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class DragonPage(CRMBasePage):

    ' Check invalid phone number displayed correctly: red number '

    def check_invalid_phone(self, phone):
        # Check number:
        sleep(1)
        number_text = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                ["number_text"]).get_attribute("innerText")
        actual_number = number_text.replace(' ', '')
        actual_number = actual_number.replace('+', '')
        assert phone in actual_number
        Logging().reportDebugStep(self, "Invalid Phone number is displayed: " + phone)
        # Check colour:
        super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                                                    ["number_color_red"])
        Logging().reportDebugStep(self, "The colour of Invalid Phone number in list view is red")
        return DragonPage(self.driver)

    ' Check invalid phone number displayed correctly: *** '

    def check_valid_phone(self, phone):
        # Check number:
        sleep(1)
        number_text = super().wait_load_element("//div[@title='Click to Call']").get_attribute("innerText")
        actual_number = number_text.replace(' ', '')
        actual_number = actual_number.replace('+', '')
        assert phone in actual_number
        Logging().reportDebugStep(self, "Valid Phone number is displayed: " + phone)
        return DragonPage(self.driver)

    ' Check Valid Phone Icon exist: '

    def check_valid_phone_icon(self):
        sleep(0.2)
        try:
            super().wait_load_element("//span[contains(@class,'phone-valid')]")
            Logging().reportDebugStep(self, "'Valid Phone Icon' is displayed")
            return True
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "'Valid Phone Icon' does not displayed")
            return False

    ' Check in list view mail displayed as "Send mail": '

    def check_email_address(self, email):
        email_address = super().wait_load_element("//a/div[@title='send mail']").get_attribute('innerText')
        assert email in email_address
        Logging().reportDebugStep(self, "Valid Email address in list view is displayed as: " + email_address)
        return DragonPage(self.driver)

    ' Check email address in Send Mail popup displayed as: *** '
    def check_email_in_send_mail_popup(self, email):
        email_address_link = super().wait_load_element("//a/div[@title='send mail']")
        try:
            self.driver.execute_script("arguments[0].click();", email_address_link)
        except:
            email_address_link.click()
        Logging().reportDebugStep(self, "Click Email address link in client details page")
        sleep(2)
        email_address = super().wait_load_element("//input[@id='parent_name']").get_attribute("value")
        assert email_address == email
        Logging().reportDebugStep(self, "Email address in Send Mail popup is displayed as: " + email_address)
        cancel_btn = super().wait_element_to_be_clickable("//input[@name='Cancel [Alt+X]']")
        try:
            self.driver.execute_script("arguments[0].click();", cancel_btn)
        except:
            cancel_btn.click()
        sleep(0.1)
        self.wait_element_to_be_disappear("//input[@name='Cancel [Alt+X]']", timeout=25)
        Logging().reportDebugStep(self, "Close Send Mail popup")
        return DragonPage(self.driver)

    def click_show_phone_btn(self):
        sleep(1)
        try:
            show_phone_btn = super().wait_load_element("//span[@title='Show Phone Number']")
            self.driver.execute_script("arguments[0].click();", show_phone_btn)
            Logging().reportDebugStep(self, "Click Show Phone Number button")
            return True
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "There are no 'Show Phone Number' button")
            return False
