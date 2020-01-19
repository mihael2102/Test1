import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.trading_ui.TradingSearchingColumnsPreconditionUI \
    import TradingSearchingColumnsPreconditionUI


@pytest.mark.run(order=3)
class TestTradingModuleUI(BaseTest):

    def test_trading_searching_columns_ui(self):
        TradingSearchingColumnsPreconditionUI(self.driver, self.config).trading_searching_columns_ui()
