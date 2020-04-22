from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.trading_ui.TradingModuleConstantsUI import TradingModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


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
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Trading Accounts module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TRADING_ACCOUNTS) \
            .open_tab_list_view_ui(TradingModuleConstantsUI.TAB_ALL)

        """ Get data from the first row of list view """
        ta_login = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_TA_LOGIN,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        server = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_SERVER,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        currency = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_CURRENCY,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        ta_name = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_TA_NAME,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TradingModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                        row=TradingModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalModulePageUI(self.driver)
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
        result = GlobalModulePageUI(self.driver)
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
