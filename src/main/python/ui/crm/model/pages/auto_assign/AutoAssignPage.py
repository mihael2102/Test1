from src.main.python.ui.crm.model.pages.auto_assign.AddRuleModule import AddRuleModule
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class AutoAssignPage(CRMBasePage):
    def __init__(self) -> None:
        super().__init__()

    def open_add_rule_module(self):
        add_rule_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add Rule')]")
        add_rule_button.click()
        Logging().reportDebugStep(self, "The Add rule module was opened")
        return AddRuleModule()

    def get_successfull_message(self):
        message = super().wait_visible_of_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "The Add rule module was opened")
        return message.text

    def click_ok(self):
        super().click_ok()
        return AddRuleModule()
