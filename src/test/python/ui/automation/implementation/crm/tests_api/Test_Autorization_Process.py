import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *


class AutorizationProcess(BaseTest):

    def test_autorization_process(self):
        ApiPrecondition(self.driver, self.config).autorization_process()
