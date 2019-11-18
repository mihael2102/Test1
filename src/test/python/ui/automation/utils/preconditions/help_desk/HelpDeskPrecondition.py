from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.utils.config import Config


class HelpDeskPrecondition(object):
    # def __init__(self) -> None:
    #     super().__init__()
    driver = None
    config = None

    def __init__(self, driver, config) -> None:
        self.driver = driver
        self.config = config

    def create_first_ticket(self):
        CRMHomePage(self.driver)\
            .open_help_desk_page()\
            .open_create_ticket_page() \
            .perform_create_new_ticket(HelpDeskConstants.FIRST_TITTLE,
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_RELATED_TO),
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_ASSIGNED_TO),
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_STATUS),
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_PRIORITY),
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_CATEGORY),
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_TICKET_SOURCE),
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_DESCRIPTION),
                                       Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_NOTES))
        return HelpDeskPrecondition(self.driver, self.config)
