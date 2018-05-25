from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class EditionTicketInfoPage(BrandBasePage):

    def __init__(self):
        super().__init__()

    def get_subject_status_text(self):
        subject_text = super().wait_load_element_present("//textarea[@name='subject']")
        return subject_text.text

    ''' 
         Returns the category status   
    '''

    def get_category_status_text(self):
        account = super().wait_load_element_present("//select[@name='ticket_statuses']")
        return account.text

    ''' 
         Returns the ticket status   
    '''

    def get_ticket_status_text(self):
        account = super().wait_load_element_present("//td[@colspan='3']//textarea[@name='description']")
        return account.text
