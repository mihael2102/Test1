from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants_ui.api_ui.ApiCustomerConstantsUI import ApiCustomerConstantsUI
from time import sleep


class ApiReadCustomerPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def read_customer_ui(self):
        """ Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Read Customer """
        token = ApiPage(self.driver)\
            .read_customer_module() \
            .enter_email_for_read_customer(ApiCustomerConstantsUI.EMAIL) \
            .send_read_customer() \
            .check_read_customer_details()
        count = 0
        while ApiCustomerConstantsUI.EMAIL not in token:
            sleep(2)
            token = ApiPage(self.driver)\
                .check_read_customer_details()
            count += 1
            if count == 5:
                break

        """ Verify data """
        assert ApiCustomerConstantsUI.EMAIL in token
        assert ApiCustomerConstantsUI.REFFERAL in token
        assert ApiCustomerConstantsUI.COUNTRY in token
        assert ApiCustomerConstantsUI.LNAME in token
        assert ApiCustomerConstantsUI.FNAME in token
