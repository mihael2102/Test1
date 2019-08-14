import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.dragon.DragonPrecondition import DragonPrecondition


@pytest.mark.run(order=35)
class CheckDragonTest(BaseTest):

    # CRM tests:
    def test_dragon_clients(self):
        DragonPrecondition(self.driver, self.config).check_dragon_clients()

    def test_dragon_leads(self):
        DragonPrecondition(self.driver, self.config).check_dragon_leads()

    # CA tests:
    def test_ca_dragon_valid_phone(self):
        DragonPrecondition(self.driver, self.config).check_ca_dragon_valid_phone()

    def test_ca_dragon_invalid_phone(self):
        DragonPrecondition(self.driver, self.config).check_ca_dragon_invalid_phone()
