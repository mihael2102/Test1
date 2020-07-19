from src.main.python.ui.crm.model.constants_ui.filters_ui.TAFilterConstantsUI import TAFilterConstantsUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.FilterPageUI import FilterPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI


class FilterTAPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_filter_ta_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Trading Accounts module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TRADING_ACCOUNTS)

        """ Create Filter """
        FilterPageUI(self.driver) \
            .create_filter_ui(
                field1=TAFilterConstantsUI.FIELD_VIEW_NAME, view_name=TAFilterConstantsUI.TA_FILTER_NAME,
                column1=TAFilterConstantsUI.COLUMN1, column2=TAFilterConstantsUI.COLUMN2,
                column3=TAFilterConstantsUI.COLUMN3, column4=TAFilterConstantsUI.COLUMN4,
                column5=TAFilterConstantsUI.COLUMN5, column6=TAFilterConstantsUI.COLUMN6,
                column7=TAFilterConstantsUI.COLUMN7, column8=TAFilterConstantsUI.COLUMN8)

        """ Get and verify current filter title """
        self.driver.refresh()
        current_filter = FilterPageUI(self.driver) \
            .get_current_filter()
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(TAFilterConstantsUI.TA_FILTER_NAME,
                               current_filter)

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

        """ Verify titles are correct """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(TAFilterConstantsUI.COLUMN1, title1) \
            .comparator_string(TAFilterConstantsUI.COLUMN2, title2) \
            .comparator_string(TAFilterConstantsUI.COLUMN3, title3) \
            .comparator_string(TAFilterConstantsUI.COLUMN4, title4) \
            .comparator_string(TAFilterConstantsUI.COLUMN5, title5) \
            .comparator_string(TAFilterConstantsUI.COLUMN6, title6) \
            .comparator_string(TAFilterConstantsUI.COLUMN7, title7) \
            .comparator_string(TAFilterConstantsUI.COLUMN8, title8)

        """ Delete Filter """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_ALL)
        self.driver.refresh()
        self.driver.refresh()
        FilterPageUI(self.driver) \
            .delete_filter(TAFilterConstantsUI.TA_FILTER_NAME) \
            .approve_deleting() \
            .verify_success_message() \
            .click_ok() \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_ALL)

        """ Check filter not exist in list """
        filter_exist = FilterPageUI(self.driver)\
            .verify_filter_in_list(TAFilterConstantsUI.TA_FILTER_NAME)
        while filter_exist:
            FilterPageUI(self.driver) \
                .delete_filter(TAFilterConstantsUI.TA_FILTER_NAME) \
                .approve_deleting() \
                .verify_success_message() \
                .click_ok() \
                .select_filter_new_ui(FiltersConstantsUI.FILTER_ALL)
            filter_exist = FilterPageUI(self.driver) \
                .verify_filter_in_list(TAFilterConstantsUI.TA_FILTER_NAME)
