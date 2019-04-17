import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.chat.Chat_Precondition import Chat_Precondition

class TestChat(BaseTest):

    def test_chat_vtiger(self):
        Chat_Precondition(self.driver, self.config).chat_vtiger_test()

    def test_chat_laravel(self):
        Chat_Precondition(self.driver, self.config).chat_laravel_test()