from time import sleep
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskDetailsPageUI import HelpDeskDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDModuleConstantsUI import HDModuleConstantsUI
from src.main.python.utils.logs.Loging import Logging


class HelpDeskModulePageUI(CRMBasePage):

    def open_ticket(self, row=1):
        sleep(0.1)
        ticket_no = super().wait_element_to_be_clickable(
            "(//span[@class='td-link' and contains(text(),'TT')])[%s]" % row)
        ticket_no.click()
        sleep(1)
        self.wait_loading_to_finish_new_ui(15)
        Logging().reportDebugStep(self, "Click Ticket number")
        return HelpDeskDetailsPageUI(self.driver)

    def set_data_column_field(self, column, data):
        GlobalModulePageUI(self.driver)\
            .set_data_column_field(column, data)
        return HelpDeskModulePageUI(self.driver)

    def delete_ticket_list_view(self, row=1):
        GlobalModulePageUI(self.driver)\
            .open_actions_list() \
            .click_delete_icon_list_view(row) \
            .approve_deleting() \
            .verify_success_message() \
            .click_ok()
        return HelpDeskModulePageUI(self.driver)

    def verify_data_not_found(self):
        GlobalModulePageUI(self.driver) \
            .verify_data_not_found()
        return HelpDeskModulePageUI(self.driver)
