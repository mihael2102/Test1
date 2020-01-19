from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.trading_ui.TradingModuleConstantsUI import TradingModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI


class TradingSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def trading_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Trading Accounts module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TRADING_ACCOUNTS) \
            .open_tab_list_view_ui(TradingModuleConstantsUI.TAB_ALL)

        """ Get data from the first row of list view """
        ta_login = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_TA_LOGIN,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        server = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_SERVER,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        currency = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_CURRENCY,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        ta_name = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_TA_NAME,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalTablePageUI(self.driver)
        if ta_login:
            search\
                .set_data_column_field(column=TradingModuleConstantsUI.COLUMN_TA_LOGIN,
                                       data=ta_login)
        if server:
            search\
                .select_data_column_field(column=TradingModuleConstantsUI.COLUMN_SERVER,
                                          data=server)
        if currency:
            search\
                .select_data_column_field(column=TradingModuleConstantsUI.COLUMN_CURRENCY,
                                          data=currency)
        if assigned_to:
            search\
                .select_data_column_field(column=TradingModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                          data=assigned_to)
        if ta_name:
            search\
                .set_data_column_field(column=TradingModuleConstantsUI.COLUMN_TA_NAME,
                                       data=ta_name)

        """ Verify correct data found """
        result = GlobalTablePageUI(self.driver)
        if ta_login:
            result\
                .global_data_checker_new_ui(ta_login)
        if server:
            result\
                .global_data_checker_new_ui(server)
        if currency:
            result\
                .global_data_checker_new_ui(currency)
        if assigned_to:
            result\
                .global_data_checker_new_ui(assigned_to)
        if ta_name:
            result\
                .global_data_checker_new_ui(ta_name)

        """ Verify, only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver)\
            .get_number_records()
        assert number_records == 1
