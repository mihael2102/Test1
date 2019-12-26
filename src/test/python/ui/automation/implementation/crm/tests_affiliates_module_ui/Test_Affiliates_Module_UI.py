import pytest

from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.test.python.ui.automation.utils.postconditions.affiliates.Affiliates_Postcondition import \
    AffiliatesPostcondition
from src.test.python.ui.automation.utils.preconditions.affiliates.Affiliates_Precondition import AffiliatesPrecondition
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.test.python.ui.automation.utils.preconditions.affiliates.Create_Affiliates_Precondition_UI import \
    CreateAffiliatesPreconditionUI


@pytest.mark.run(order=32)
class TestAffiliateModuleUI(BaseTest):

    def test_create_delete_affiliate_ui(self):
        CreateAffiliatesPreconditionUI(self.driver, self.config).create_delete_affiliate_ui()
