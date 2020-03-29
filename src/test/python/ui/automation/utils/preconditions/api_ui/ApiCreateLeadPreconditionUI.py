from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants_ui.api_ui.ApiLeadConstantsUI import ApiLeadConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsDetailsPageUI import LeadsDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsDetailsConstantsUI import LeadsDetailsConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsModulePageUI import LeadsModulePageUI
from time import sleep


class ApiCreateLeadPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_lead_ui(self):
        """ API Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Create Lead """
        token = ApiPage(self.driver) \
            .create_lead_module() \
            .enter_email_lead(ApiLeadConstantsUI.EMAIL) \
            .enter_firstName_lead(ApiLeadConstantsUI.FNAME) \
            .enter_lastName_lead(ApiLeadConstantsUI.LNAME) \
            .enter_phone_lead(ApiLeadConstantsUI.PHONE) \
            .send_create_lead() \
            .check_create_lead_token()
        count = 0
        while ApiLeadConstantsUI.STATUS_OK not in token:
            sleep(1)
            token = ApiPage(self.driver)\
                .check_create_lead_token()
            count += 1
            if count == 5:
                break
        assert ApiLeadConstantsUI.STATUS_OK in token

        """ CRM: get lead's data """
        CRMLoginPageUI(self.driver) \
            .switch_first_tab_page()
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_LEADS) \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   ApiLeadConstantsUI.EMAIL)
        LeadsModulePageUI(self.driver) \
            .open_lead()

        details = LeadsDetailsPageUI(self.driver)

        first_name = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_FNAME)
        last_name = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_LNAME)
        phone = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_PHONE)
        email = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_EMAIL)

        """ Verify lead's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(first_name, ApiLeadConstantsUI.FNAME) \
            .comparator_string(last_name, ApiLeadConstantsUI.LNAME)

        if "*" not in email and "..." not in email:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(email, ApiLeadConstantsUI.EMAIL)
        elif "*" not in email:
            email = email.replace('...', '')
            assert email in ApiLeadConstantsUI.EMAIL

        if "*" not in phone:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(phone, ApiLeadConstantsUI.PHONE)
