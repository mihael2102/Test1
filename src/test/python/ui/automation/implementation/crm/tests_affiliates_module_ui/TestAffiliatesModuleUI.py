import pytest

from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.affiliates_ui.Create_Affiliates_Precondition_UI import \
    CreateAffiliatesPreconditionUI


@pytest.mark.run(order=32)
class TestAffiliateModuleUI(BaseTest):

    def test_create_delete_affiliate_ui(self):
        CreateAffiliatesPreconditionUI(self.driver, self.config).create_delete_affiliate_ui()
