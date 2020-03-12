from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants.APIConstants import APIConstants
from src.main.python.ui.crm.model.constants_ui.api_ui.ApiLeadConstantsUI import ApiLeadConstantsUI


class ApiReadLeadsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def read_leads_ui(self):
        """ Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Read Leads """
        token = ApiPage(self.driver)\
            .read_leads_module() \
            .enter_leads_page(APIConstants.PAGE) \
            .enter_leads_limit(APIConstants.LIMIT) \
            .send_leads_read() \
            .check_read_leads_token()

        assert ApiLeadConstantsUI.EMAIL in token
