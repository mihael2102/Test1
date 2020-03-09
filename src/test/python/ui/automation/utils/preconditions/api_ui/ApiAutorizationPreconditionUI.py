import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants.APIConstants import APIConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants_ui.affiliates_ui.AffiliatesModuleConstantsUI import \
    AffiliatesModuleConstantsUI
from src.main.python.ui.crm.model.pages.affiliates_module_ui.AffiliatesModulePageUI import AffiliatesModulePageUI


class ApiAutorizationPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def autorization_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                new_design=0,
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Affiliates module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_AFFILIATES)

        """ Search by Partner ID: get secret key and api link """
        secret_key = GlobalTablePageUI(self.driver)\
            .set_data_column_field(column=AffiliatesModuleConstantsUI.COLUMN_PARTNER_ID,
                                   data=var.get_var("ApiPrecondition")["partner_id"]) \
            .get_data_from_list_view_ui(column=AffiliatesModuleConstantsUI.COLUMN_SECRET_KEY,
                                        row=AffiliatesModuleConstantsUI.ROW_1)
        api_link = AffiliatesModulePageUI(self.driver)\
            .get_link_api()

        """ Autorization """
        ApiPage(self.driver)\
            .open_first_tab_page(api_link) \
            .enter_secret_key(secret_key) \
            .authorization_module() \
            .input_partner_id(var.get_var("ApiPrecondition")["partner_id"]) \
            .generate_time() \
            .generate_accessKey() \
            .send_authorization()
        check_token = ApiPage(self.driver)\
            .check_token()

        assert APIConstants.STATUS_OK in check_token
