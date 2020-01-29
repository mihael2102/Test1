import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4DepositConstantsUI import MT4DepositConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4WithdrawConstantsUI import MT4WithdrawConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4WithdrawPageUI import MT4WithdrawPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI


@pytest.mark.run(order=13)
class LoadSwitchTabsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_switch_tabs_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                new_design=1,
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Switch between Clients and Leads module """
        counter = 0
        while counter != 30:
            CRMBaseMethodsPage(self.driver) \
                .open_module_ui(TestDataConstants.MODULE_CLIENTS)
            sleep(1)
            CRMBaseMethodsPage(self.driver) \
                .open_module_ui(TestDataConstants.MODULE_LEADS)
            sleep(1)
            counter += 1
