from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule


class DragonPage(CRMBasePage):

    'Check invalid phone number displayed correctly: red number '

    def check_invalid_phone(self, phone):
        # Check number:
        number_text = super().wait_load_element("//div[@title='Click to Call']").get_attribute("innerText")
        actual_number = number_text.replace(' ', '')
        actual_number = actual_number.replace('+', '')
        assert actual_number == phone
        Logging().reportDebugStep(self, "Invalid Phone number is displayed: " + phone)
        # Check colour:
        super().wait_load_element("//div[@title='Click to Call' and @style='color: red']")
        Logging().reportDebugStep(self, "The colour of Invalid Phone number in list view is red")
        return DragonPage(self.driver)

    ' Check invalid phone number displayed correctly: *** '

    def check_valid_phone(self, phone):
        # Check number:
        number_text = super().wait_load_element("//div[@title='Click to Call']").get_attribute("innerText")
        actual_number = number_text.replace(' ', '')
        actual_number = actual_number.replace('+', '')
        assert actual_number == phone
        Logging().reportDebugStep(self, "Valid Phone number is displayed: " + phone)
        return DragonPage(self.driver)

    ' Check in list view mail displayed as "Send mail": '
    def check_email_address(self, email):
        email_address = super().wait_load_element("//a/div[@title='send mail']").get_attribute('innerText')
        assert email_address == email
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
        sleep(1)
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
