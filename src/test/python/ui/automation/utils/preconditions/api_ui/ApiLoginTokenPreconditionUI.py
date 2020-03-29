from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants_ui.api_ui.ApiCustomerConstantsUI import ApiCustomerConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI


class ApiLoginTokenPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def login_token_ui(self):
        """ Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Login Token """
        token = ApiPage(self.driver) \
            .login_token_module() \
            .enter_email_for_login_token(ApiCustomerConstantsUI.EMAIL) \
            .send_login_token() \
            .check_login_token()
        token = token.replace(' ', '')
        token = token.replace('{\n"data":{\n"url":"', '')
        token = token.replace('"\n}\n}', '')

        CRMLoginPageUI(self.driver) \
            .open_first_tab_page(token)

        assert ApiCustomerConstantsUI.FOREX_DEPOSIT in token
