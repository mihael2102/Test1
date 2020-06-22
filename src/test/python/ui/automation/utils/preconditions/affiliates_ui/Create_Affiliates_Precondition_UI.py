from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.AffiliatesModuleConstantsUI import AffiliatesModuleConstantsUI
from src.main.python.ui.crm.model.pages.affiliates_module_ui.AffiliatesModulePageUI import AffiliatesModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.affiliates_module_ui.CreateAffiliatesPageUI import CreateAffiliatesPageUI
from src.main.python.ui.crm.model.constants.CreateAffiliateConstants import CreateAffiliateConstants
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


class CreateAffiliatesPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_delete_affiliate_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Affiliates page """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_AFFILIATES)

        """ Create new affiliate """
        CreateAffiliatesPageUI(self.driver)\
            .click_add_new_affiliate_btn()\
            .set_partner_name(CreateAffiliateConstants.PARTNER_NAME)\
            .select_brand()\
            .set_allowed_ip(CreateAffiliateConstants.ALLOWED_IP)\
            .verify_allowed_ip_added(CreateAffiliateConstants.ALLOWED_IP)\
            .select_allowed_methods(CreateAffiliateConstants.ALLOWED_METHOD)\
            .select_blocked_countries(CreateAffiliateConstants.BLOCKED_COUNTRY)\
            .click_save()

        """ Verify Success message """
        CRMBaseMethodsPage(self.driver)\
            .verify_success_message()\
            .click_ok()

        """ Verify affiliate exist in table """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column=AffiliatesModuleConstantsUI.COLUMN_PARTNER_NAME,
                                   data=CreateAffiliateConstants.PARTNER_NAME) \
            .global_data_checker_new_ui(CreateAffiliateConstants.PARTNER_NAME)

        """ Open affiliate's details page and verify Partner name """
        AffiliatesModulePageUI(self.driver)\
            .click_on_partner_name(CreateAffiliateConstants.PARTNER_NAME) \
            .verify_name_on_affiliate_details(CreateAffiliateConstants.PARTNER_NAME)\
            .came_back_on_previous_page()

        """ Delete affiliate """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column=AffiliatesModuleConstantsUI.COLUMN_PARTNER_NAME,
                                   data=CreateAffiliateConstants.PARTNER_NAME)
        AffiliatesModulePageUI(self.driver) \
            .click_more_icon()\
            .click_delete_icon()\
            .click_delete_btn()

        """ Verify Success message """
        CRMBaseMethodsPage(self.driver) \
            .verify_success_message() \
            .click_ok()\
            .refresh_page()

        """ Verify affiliate was deleted """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column=AffiliatesModuleConstantsUI.COLUMN_PARTNER_NAME,
                                   data=CreateAffiliateConstants.PARTNER_NAME)
        AffiliatesModulePageUI(self.driver) \
            .verify_data_not_found()
