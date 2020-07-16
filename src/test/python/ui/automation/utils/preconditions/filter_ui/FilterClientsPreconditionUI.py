from src.main.python.ui.crm.model.constants_ui.filters_ui.ClientsFilterConstantsUI import ClientsFilterConstantsUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.FilterPageUI import FilterPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI


class FilterClientsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_filter_clients_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Create Filter """
        FilterPageUI(self.driver) \
            .create_filter_ui(
                field1=ClientsFilterConstantsUI.FIELD_VIEW_NAME, view_name=ClientsFilterConstantsUI.CLIENTS_FILTER_NAME,
                column1=ClientsFilterConstantsUI.COLUMN1, column2=ClientsFilterConstantsUI.COLUMN2,
                column3=ClientsFilterConstantsUI.COLUMN3, column4=ClientsFilterConstantsUI.COLUMN4,
                column5=ClientsFilterConstantsUI.COLUMN5, column6=ClientsFilterConstantsUI.COLUMN6,
                column7=ClientsFilterConstantsUI.COLUMN7, column8=ClientsFilterConstantsUI.COLUMN8,
                column9=ClientsFilterConstantsUI.COLUMN9, column10=ClientsFilterConstantsUI.COLUMN10,
                column11=ClientsFilterConstantsUI.COLUMN11)

        """ Get and verify current filter title """
        self.driver.refresh()
        # current_filter = FilterPageUI(self.driver) \
        #     .get_current_filter()
        # CRMBaseMethodsPage(self.driver) \
        #     .comparator_string(ClientsFilterConstantsUI.CLIENTS_FILTER_NAME,
        #                        current_filter)

        """ Get titles of new filter columns """
        title = GlobalModulePageUI(self.driver)

        title1 = title\
            .get_column_title("1").strip()
        title2 = title \
            .get_column_title("2").strip()
        title3 = title \
            .get_column_title("3").strip()
        title4 = title \
            .get_column_title("4").strip()
        title5 = title \
            .get_column_title("5").strip()
        title6 = title \
            .get_column_title("6").strip()
        title7 = title \
            .get_column_title("7").strip()
        title8 = title \
            .get_column_title("8").strip()
        title9 = title \
            .get_column_title("9").strip()
        title10 = title \
            .get_column_title("10").strip()
        title11 = title \
            .get_column_title("11").strip()

        """ Verify titles are correct """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN1, title1) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN2, title2) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN3, title3) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN4, title4) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN5, title5) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN6, title6) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN7, title7) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN8, title8) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN9, title9) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN10, title10) \
            .comparator_string(ClientsFilterConstantsUI.COLUMN11, title11)

        """ Delete Filter """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_ALL)
        self.driver.refresh()
        self.driver.refresh()
        FilterPageUI(self.driver) \
            .delete_filter(ClientsFilterConstantsUI.CLIENTS_FILTER_NAME) \
            .approve_deleting() \
            .verify_success_message() \
            .click_ok() \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_ALL)

        """ Check filter not exist in list """
        filter_exist = FilterPageUI(self.driver)\
            .verify_filter_in_list(ClientsFilterConstantsUI.CLIENTS_FILTER_NAME)
        while filter_exist:
            FilterPageUI(self.driver) \
                .delete_filter(ClientsFilterConstantsUI.CLIENTS_FILTER_NAME) \
                .approve_deleting() \
                .verify_success_message() \
                .click_ok() \
                .select_filter_new_ui(FiltersConstantsUI.FILTER_ALL)
            filter_exist = FilterPageUI(self.driver) \
                .verify_filter_in_list(ClientsFilterConstantsUI.CLIENTS_FILTER_NAME)
