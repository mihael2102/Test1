import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.EditLeadConstantsUI import EditLeadConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsModulePageUI import LeadsModulePageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.CreateLeadPageUI import CreateLeadPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsDetailsPageUI import LeadsDetailsPageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.EditLeadPageUI import EditLeadPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsDetailsConstantsUI import LeadsDetailsConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.ConvertLeadPageUI import ConvertLeadPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=31)
class EditPencilLeadPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def edit_pencil_lead_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS)

        """ Search lead """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_LEADS) \
            .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   data=LeadsModuleConstantsUI.SHORT_EMAIL)

        """ Edit field via Pencil button """
        mobile = LeadsModulePageUI(self.driver) \
            .open_lead('3') \
            .edit_text_field_via_pencil_icon(
                field=LeadsDetailsConstantsUI.FIELD_MOBILE,
                text=LeadsDetailsConstantsUI.MOBILE_EDIT) \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_MOBILE)

        """ Verify field was updated """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(mobile, LeadsDetailsConstantsUI.MOBILE_EDIT) \
            .refresh_page()

        """ Verify field will not change after page reload """
        mobile = LeadsDetailsPageUI(self.driver) \
            .get_data_from_field_click_to_view(LeadsDetailsConstantsUI.FIELD_MOBILE)

        CRMBaseMethodsPage(self.driver) \
            .comparator_string(mobile, LeadsDetailsConstantsUI.MOBILE_EDIT)
