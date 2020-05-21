import pytest
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=10)
class MassAssignTestCRM(BaseTest):

    def test_clients_mass_assign(self):
        crm_client_profile = CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            ClientsPage(self.driver) \
                .perform_searching_by_fname(CRMConstants.TESTQA)
        else:
            ClientsPage(self.driver) \
                .perform_searching_by_email(CRMConstants.SHORT_EMAIL)

        crm_client_profile\
            .select_three_records_clients_module() \
            .open_mass_assign_module() \
            .search_user(MassEditConstants.USER_ONE) \
            .enter_check_box() \
            .click_save()

        confirmation_message = crm_client_profile.get_confirm_message()
        assert confirmation_message == CRMConstants().MASS_ASSIGN_MESSAGE
        crm_client_profile.click_ok()
