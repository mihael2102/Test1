from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from src.main.python.ui.ca.model.constants.sign_up.SignUpFirstStepConstants import SignUpFirstStepConstants
from time import sleep


class SignUpQ8Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def sign_up_q8(self):
        """ Registration form """
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .sign_up_q8(
                first_name=SignUpFirstStepConstants.F_NAME,
                last_name=SignUpFirstStepConstants.L_NAME,
                email=SignUpFirstStepConstants.EMAIL,
                phone=SignUpFirstStepConstants.PHONE,
                password=SignUpFirstStepConstants.PASSWORD)

        sleep(2)
        CALoginPage(self.driver).verify_client("my account")
