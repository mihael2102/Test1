from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.utils.config import Config


class HelpDeskPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config) -> None:
        self.driver = driver
        self.config = config

    def create_first_ticket(self):
        CRMHomePage(self.driver) \
            .open_more_list_modules() \
            .open_help_desk_page()\
            .open_create_ticket_page() \
            .perform_create_new_ticket(HelpDeskConstants.FIRST_TITTLE,
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_RELATED_TO),
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_ASSIGNED_TO),
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_STATUS),
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_PRIORITY),
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_CATEGORY),
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_TICKET_SOURCE),
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_DESCRIPTION),
                                       self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                      HelpDeskConstants.FIRST_NOTES))
        return HelpDeskPrecondition(self.driver, self.config)
