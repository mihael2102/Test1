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







    def test_make_transfer_between_ta(self):
        TransferBetweenPrecondition().add_two_usd_currencies().make_deposit()

        crm_client_profile = ClientProfilePage()

        first_client_profile = crm_client_profile.get_client_account()
        second_client_profile = crm_client_profile.get_second_client_account()

        amount_initial = crm_client_profile.get_initial_amount()

        difference_amount = crm_client_profile \
            .get_difference_amount_text(amount_initial, CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA)

        crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.TRANSFER_BETWEEN_TA)

        MT4TransferBetweenTa().make_transfer_between_ta(first_client_profile, second_client_profile,
                                                        CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA,
                                                        CRMConstants.DESCRIPTION_TRANSFER_BETWEEN_TA)

        confirmation_message = crm_client_profile.get_confirm_message()
        assert confirmation_message == CRMConstants.TRANSFER_BETWEEN_TA_MESSAGE

        amount_transfer = crm_client_profile.click_ok() \
            .click_trading_accounts_tab().get_amount_text(difference_amount)

        assert amount_transfer == difference_amount
