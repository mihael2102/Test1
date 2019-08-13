import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.dragon.DragonPrecondition import DragonPrecondition


@pytest.mark.run(order=35)
class CheckDragonTest(BaseTest):

    def test_dragon_valid_phone(self):
        DragonPrecondition(self.driver, self.config).check_dragon_valid_phone()

    def test_dragon_invalid_phone(self):
        DragonPrecondition(self.driver, self.config).check_dragon_invalid_phone()
