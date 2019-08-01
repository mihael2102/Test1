from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule


class DragonPage(CRMBasePage):

    'Check invalid phone number displayed correctly: red number '

    def check_invalid_phone_leads(self, phone):
        # Check number:
        number_text = super().wait_load_element("//div[@title='Click to Call']").get_attribute("innerText")
        actual_number = number_text.replace(' ', '')
        actual_number = actual_number.replace('+', '')
        assert actual_number == phone
        Logging().reportDebugStep(self, "Invalid Phone number is displayed: " + phone)
        # Check colour:
        super().wait_load_element("//div[@title='Click to Call' and @style='color: red']")
        Logging().reportDebugStep(self, "The colour of Invalid Phone number in list view is red")
        return LeadsModule(self.driver)

    ' Check invalid phone number displayed correctly: *** '

    def check_valid_phone_leads(self, phone):
        # Check number:
        number_text = super().wait_load_element("//div[@title='Click to Call']").get_attribute("innerText")
        actual_number = number_text.replace(' ', '')
        actual_number = actual_number.replace('+', '')
        assert actual_number == phone
        Logging().reportDebugStep(self, "Valid Phone number is displayed: " + phone)
        return LeadsModule(self.driver)
