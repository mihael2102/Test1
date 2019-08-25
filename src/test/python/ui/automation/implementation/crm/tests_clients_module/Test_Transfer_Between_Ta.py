import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.transfer_between_ta.MT4TransferBetweenTa import MT4TransferBetweenTa
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.transfer_between_ta.TransferBetweenPrecondition import \
    TransferBetweenPrecondition


@pytest.mark.run(order=3)
class TransferBetweenTa(BaseTest):

    def test_transfer_between_ta(self):
        TransferBetweenPrecondition(self.driver, self.config).transfer_between_accounts()
