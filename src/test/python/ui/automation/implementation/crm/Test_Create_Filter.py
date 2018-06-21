import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=6)
class CreateFilterTestCRM(BaseTest):

    def test_create_filter(self):
        clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        clients_module_page.open_create_filter_pop_up() \
            .perform_create_filter(Config.data.get_data_first_client(CRMConstants.FILTER_NAME),
                                   Config.data.get_data_first_client(CRMConstants.FIRST_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.SECOND_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.THIRD_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.FOURTH_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.FIFTH_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.SIXTH_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.SEVENTH_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.EIGHTH_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.NINTH_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.TENTH_COLUMN),
                                   Config.data.get_data_first_client(CRMConstants.ELEVENTH_COLUMN)) \
            .click_save_button()

        first_name__column = clients_module_page.get_first_name_column()
        second_name_column = clients_module_page.get_second_name_column()
        third_name__column = clients_module_page.get_third_name_column()
        fourth_name_column = clients_module_page.get_fourth_name_column()
        fifth_name_column = clients_module_page.get_fifth_name_column()
        sixth_name_column = clients_module_page.get_sixth_name_column()
        seventh_name_column = clients_module_page.get_seventh_name_column()
        eighth_name_column = clients_module_page.get_eighth_name_column()
        ninth_name_column = clients_module_page.get_ninth_name_column()
        tenth_name_column = clients_module_page.get_tenth_name_column()
        eleventh_name_column = clients_module_page.get_eleventh_name_column()

        assert Config.data.get_data_first_client(CRMConstants.FIRST_COLUMN) == first_name__column
        assert Config.data.get_data_first_client(CRMConstants.SECOND_COLUMN) == second_name_column
        assert Config.data.get_data_first_client(CRMConstants.THIRD_COLUMN) == third_name__column
        assert CRMConstants.FOURTH_COLUMN_OTHER_TYPE == fourth_name_column
        assert Config.data.get_data_first_client(CRMConstants.FIFTH_COLUMN) == fifth_name_column
        assert CRMConstants.SIXTH_COLUMN_OTHER_TYPE == sixth_name_column
        assert Config.data.get_data_first_client(CRMConstants.SEVENTH_COLUMN) == seventh_name_column
        assert Config.data.get_data_first_client(CRMConstants.EIGHTH_COLUMN) == eighth_name_column
        assert CRMConstants.NINTH_COLUMN_OTHER_TYPE == ninth_name_column
        assert CRMConstants.TENTH_COLUMN_OTHER_TYPE == tenth_name_column
        assert Config.data.get_data_first_client(CRMConstants.ELEVENTH_COLUMN) == eleventh_name_column

        clients_module_page.delete_filter().confirm_delete()
