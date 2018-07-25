from src.main.python.ui.crm.model.constants.FilterConstants import FilterConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.utils.config import Config


class FilterPrecondition(object):

    def create_filter(self):
        clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        CRMHomePage().open_help_desk_page()
        clients_module_page.open_create_filter_pop_up() \
            .perform_create_filter_help_desk_module(FilterConstants.FIRST_NAME,
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.FIRST_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.SECOND_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.THIRD_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.FOURTH_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.FIFTH_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.SIXTH_COLUMN)) \
            .click_save_button()

    def create_filter_service_desk(self):
        CRMHomePage().open_help_desk_page() \
            .open_create_filter_pop_up() \
            .perform_create_filter_help_desk_module(FilterConstants.FIRST_NAME,
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.FIRST_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.SECOND_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.THIRD_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.FOURTH_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.FIFTH_COLUMN),
                                                    Config.data.get_data_filter_crm(FilterConstants.FIRST_FILTER_NAME,
                                                                                    FilterConstants.SIXTH_COLUMN)) \
            .click_save_button()
