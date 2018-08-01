from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.utils.config import Config


class HelpDeskPostCondition(object):
    def __init__(self) -> None:
        super().__init__()

    def delete_ticket_by_pencil(self):
        message_delete_ticket = HelpDeskPage().select_filter(
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .delete_ticket() \
            .get_confirm_delete_ticket()
        return message_delete_ticket
