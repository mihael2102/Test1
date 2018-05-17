import re
from _decimal import Decimal
from time import sleep

from selenium.webdriver.common.by import By

from scr.main.python.ui.brand.model.pages.edit_ticket.BrandEditionTicketInfoPage import EditionTicketInfoPage
from scr.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from scr.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from scr.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from scr.main.python.ui.crm.model.pages.trading_accounts_information.CRMTradingAccountsInformationPage import \
    CRMTradingAccountsInformationPage


class CRMClientProfilePage(CRMBasePage):

    def __init__(self):
        super().__init__()

    '''
        Perform scroll_down
        return Manage Accounts Module  instance    
    '''

    def perform_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        return CRMClientProfilePage()

    def click_trading_accounts_tab(self):
        sleep(2)
        trading_account_tab = super().wait_load_element("//li//a[contains(text(),'Trading Accounts')][1]")
        trading_account_tab.click()
        return CRMClientProfilePage()

    '''
         Perform scroll_top
         return Manage Accounts Module  instance    
     '''

    def perform_scroll_up(self):
        self.driver.execute_script("scroll(0, 0);")
        return CRMClientProfilePage()

    '''
        Open the trading tabs
        return Manage Accounts Module  instance    
    '''

    def open_trading_accounts_tab(self):
        trading_tab = super().wait_load_element("//a[@id='show_Accounts_TradingAccounts']")
        trading_tab.click()
        sleep(3)
        return CRMClientProfilePage()

    '''
            Open the Finacial Transactions tabs
            return Manage Accounts Module  instance    
        '''

    def open_financial_transactions_tab(self):
        trading_tab = super().wait_load_element("//a[@id='show_Accounts_FinancialTransactions']")
        trading_tab.click()
        return CRMClientProfilePage()

    '''
           :return client amount from Trading Accounts tabs 
    '''

    def get_amount_text(self, total_amount_crm):
        return super().wait_until_element_present("//tr[@class='lvtColData'][1]//td[3]", total_amount_crm)

    '''
        :return client total amount from Trading Accounts tabs 
    '''

    def get_total_amount_text(self, amount, initial_amount):
        total_amount = Decimal(amount) + Decimal(initial_amount)
        print(total_amount)
        return str(total_amount)

    '''
        Open the client account 
        :parameter id client account ID 
        return Trading Accounts_Info  instance    
    '''

    def open_client_account(self, account_id):
        super().wait_load_element("//div[@class ='link_field']//a[contains(text(),'%s')]" % account_id)
        account = self.driver.find_element(By.XPATH,
                                           "//div[@class ='link_field']//a[contains(text(),'%s')]" % account_id)
        account.click()
        return CRMTradingAccountsInformationPage()

    '''
        :return client account from trading accounts tabs 
    '''

    def get_client_account(self):
        account_number = super().wait_load_element("//tr[@class='lvtColData'][1]//td[1]")
        return account_number.text

    '''
            :return second client account from trading accounts tabs 
        '''

    def get_second_client_account(self):
        account_number = super().wait_load_element("//tr[@class='lvtColData'][2]//td[1]")
        return account_number.text

    '''
            Open the document tabs  
            :parameter id client account ID 
            return Client Profile instance    
        '''

    def open_document_tab(self):
        select_country = super().wait_load_element("//a[@id='show_Accounts_Documents']")
        select_country.click()
        return CRMClientProfilePage()

    def open_document_number(self):
        select_country = super().wait_load_element("//a[contains(text(),'bear.jpg')]/../preceding-sibling::td[2]")
        select_country.click()
        return DocumentDetailViewPage()

    '''
             Returns the status of document from CRM 
    '''

    def get_document_status_text(self):
        document_status = super().wait_load_element("//span[@class ='clientStatusFTD']")
        print(document_status.text)
        return document_status.text

    '''
        Open the help deck tabs  
        :parameter id client account ID 
        return Client Profile instance    
    '''

    def open_help_desk_tab(self):
        select_country = super().wait_load_element("//a[@id='show_Accounts_HelpDesk']")
        select_country.click()
        return CRMClientProfilePage()

    '''
         Open the action of the ticket number
         return Edition Ticket Info instance    
    '''

    def open_action_help_desk(self):
        account = super().wait_load_element("//a[@class='glyphicons pencil cntrl'][1]")
        account.click()
        return EditionTicketInfoPage()

    '''
         Returns the status of ticket 
    '''

    def get_status_client(self):
        client_status = super().wait_load_element("//span[@class ='clientStatusFTD']")
        print(client_status.text)
        return client_status.text

    '''
         Select  the module in the MT4 actions 
    '''

    def open_mt4_actions(self, module):
        mt4_button = super().wait_load_element("//div[@class='mt4_act_box']")
        mt4_button.click()
        sleep(2)
        MT4DropDown().mt4_actions(module)

    def refresh_page(self):
        sleep(5)
        self.driver.refresh()
        return CRMClientProfilePage()

    def wait_element_is_present(self):
        super().wait_until_element_present("//span[@class ='clientStatusFTD']")
        return CRMClientProfilePage()

    def get_initial_amount(self):
        initial_amount = super().wait_load_element("//tr[@class='lvtColData'][1]//td[3]")
        total_amount = re.sub('[ ]', '', initial_amount.text)
        return total_amount

    def get_date_birthday(self):
        date = self.driver.find_element(By.XPATH, "//td[contains(text(),'Date Of Birth')]//following-sibling::td[1]")
        parser_data = re.sub('[-]', '', date.text)
        return parser_data

    def get_first_name(self):
        first_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'First Name')]//following-sibling::td[1]")
        return first_name.text

    def get_last_name(self):
        last_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'Last Name')]//following-sibling::td[1]")
        return last_name.text

    def get_citizenship_text(self):
        citizenship_text = self.driver.find_element(By.XPATH,
                                                    "//td[contains(text(),'Citizenship')]//following-sibling::td[1]")
        return citizenship_text

    def get_city_text(self):
        self.driver.execute_script("scroll(0, 300);")
        city_text = self.driver.find_element(By.XPATH, "//td[contains(text(),'Address')]//following-sibling::td[1]")
        return city_text.text

    def get_address_text(self):
        city_text = self.driver.find_element(By.XPATH, "//td[contains(text(),'Address')]//following-sibling::td[1]")
        return city_text.text
