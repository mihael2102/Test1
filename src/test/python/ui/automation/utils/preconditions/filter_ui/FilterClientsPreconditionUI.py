from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants_ui.filters_ui.ClientsFilterConstantsUI import ClientsFilterConstantsUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.filter.FilterPrecondition import FilterPrecondition
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.FilterPageUI import FilterPageUI


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
            new_design=0,
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        FilterPageUI(self.driver) \
            .create_filter_clients_ui(
                field1=ClientsFilterConstantsUI.FIELD_VIEW_NAME, view_name=ClientsFilterConstantsUI.CLIENTS_FILTER_NAME,
                column1=ClientsFilterConstantsUI.COLUMN1, column2=ClientsFilterConstantsUI.COLUMN2,
                column3=ClientsFilterConstantsUI.COLUMN3, column4=ClientsFilterConstantsUI.COLUMN4,
                column5=ClientsFilterConstantsUI.COLUMN5, column6=ClientsFilterConstantsUI.COLUMN6,
                column7=ClientsFilterConstantsUI.COLUMN7, column8=ClientsFilterConstantsUI.COLUMN8,
                column9=ClientsFilterConstantsUI.COLUMN9, column10=ClientsFilterConstantsUI.COLUMN10,
                column11=ClientsFilterConstantsUI.COLUMN11)

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

        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.FIRST_COLUMN) == first_name__column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.SECOND_COLUMN) == second_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.THIRD_COLUMN) == third_name__column
        assert CRMConstants.FOURTH_COLUMN_OTHER_TYPE == fourth_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FIFTH_COLUMN) == fifth_name_column
        assert CRMConstants.SIXTH_COLUMN_OTHER_TYPE == sixth_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.SEVENTH_COLUMN) == seventh_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.EIGHTH_COLUMN) == eighth_name_column
        assert CRMConstants.NINTH_COLUMN_OTHER_TYPE == ninth_name_column
        assert CRMConstants.TENTH_COLUMN_OTHER_TYPE == tenth_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.ELEVENTH_COLUMN) == eleventh_name_column

        FilterPrecondition(self.driver, self.config).delete_clients_module_filter()