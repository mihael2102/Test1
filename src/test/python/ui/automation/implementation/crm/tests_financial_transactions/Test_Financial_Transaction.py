from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.test.python.ui.automation.BaseTest import *


class FinancialTransaction(BaseTest):



    def test_check_all_tab_from_financial_transactions(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        create_leads_module = CRMHomePage().open_lead_module() \
            .perform_searching(Config.data.get_data_first_client(CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_first_client(CRMConstants.SHORT_E_MAIL),
                               Config.data.get_data_first_client(CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_first_client(TestDataConstants.FIRST_COUNTRY),
                               Config.data.get_data_first_client(CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_first_client(CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_first_client(TestDataConstants.CITY),
                               Config.data.get_data_first_client(CRMConstants.BRAND_NEW_FOREX)) \
            .open_client_id()