from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsPage import TradingAccountsPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.filter.FilterPrecondition import FilterPrecondition
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.FilterPageUI import FilterPageUI
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


class FilterClientsPreconditionUI(BaseTest):

    def create_filter_clients_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            new_design=0,
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        FilterPageUI(self.driver).create_filter_clients_ui()

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