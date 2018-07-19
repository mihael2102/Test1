from src.main.python.ui.crm.model.constants.FilterConstants import FilterConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.utils.TestDataConstants import TestDataConstants
from src.main.python.utils.config import Config


class FilterPrecondition(object):

    def test_create_filter_service_desc(self):
        clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD))

        CRMHomePage().open_more_list_modules() \
            .select_service_desk_module_more_list(HelpDeskConstants.SERVICE_DESK_MODULE)

        clients_module_page.open_create_filter_pop_up() \
            .perform_create_filter_help_desk_module(FilterConstants.FIRST_NAME,
            Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME, FilterConstants.FIRST_COLUMN),
            Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME, FilterConstants.SECOND_COLUMN),
            Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME, FilterConstants.THIRD_COLUMN),
            Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME, FilterConstants.FOURTH_COLUMN),
            Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME, FilterConstants.FIFTH_COLUMN),
            Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME, FilterConstants.SIXTH_COLUMN)) \
            .click_save_button()
