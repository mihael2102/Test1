import re
from _decimal import Decimal
from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.brand.model.pages.edit_ticket.BrandEditionTicketInfoPage import EditionTicketInfoPage
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.ui.crm.model.pages.trading_accounts_information.CRMTradingAccountsInformationPage import \
    CRMTradingAccountsInformationPage
from src.main.python.utils.logs.Loging import Logging


class CRMClientProfilePage(CRMBasePage):

    def __init__(self):
        super().__init__()

    '''
        Perform scroll_down
        returns Manage Accounts Module  instance    
    '''

    def perform_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Logging().reportDebugStep(self, "Perform scroll down ")
        sleep(2)
        return CRMClientProfilePage()

    '''
          Perform scroll_down
          returns Manage Accounts Module  instance    
     '''

    def click_trading_accounts_tab(self):
        sleep(2)
        trading_account_tab = super().wait_load_element("//li//a[contains(text(),'Trading Accounts')][1]")
        trading_account_tab.click()
        Logging().reportDebugStep(self, "Open the trading account tab ")
        return CRMClientProfilePage()

    '''
         Perform scroll_top
         returns Manage Accounts Module  instance    
     '''

    def perform_scroll_up(self):
        self.driver.execute_script("scroll(0, 0);")
        Logging().reportDebugStep(self, "Perform scroll up ")
        return CRMClientProfilePage()

    '''
        Open the trading tabs
        returns Manage Accounts Module  instance    
    '''

    def open_trading_accounts_tab(self):
        trading_tab = super().wait_load_element("//a[@id='show_Accounts_TradingAccounts']")
        trading_tab.click()
        Logging().reportDebugStep(self, "Open the trading account tab ")
        sleep(3)
        return CRMClientProfilePage()

    '''
         Open the Finacial Transactions tabs
         returns Manage Accounts Module  instance    
    '''

    def open_financial_transactions_tab(self):
        trading_tab = super().wait_load_element("//a[@id='show_Accounts_FinancialTransactions']")
        trading_tab.click()
        Logging().reportDebugStep(self, "Open the financial transactions tab ")
        return CRMClientProfilePage()

    '''
        :returns client amount from Trading Accounts tabs 
    '''

    def get_amount_text(self, total_amount_crm):
        Logging().reportDebugStep(self, "Return the amount text " + total_amount_crm)
        return super().wait_until_element_present("//tr[@class='lvtColData'][1]//td[3]", total_amount_crm)

    '''
        :returns client total amount from Trading Accounts tabs 
    '''

    def get_total_amount_text(self, amount, initial_amount):
        total_amount = Decimal(amount) + Decimal(initial_amount)
        Logging().reportDebugStep(self, "Return the total amount text " + str(total_amount))
        return str(total_amount)

    '''
        Open the client account 
        :parameter id client account ID 
        returns Trading Accounts_Info  instance    
    '''

    def open_client_account(self, account_id):
        super().wait_load_element("//div[@class ='link_field']//a[contains(text(),'%s')]" % account_id)
        account = self.driver.find_element(By.XPATH,
                                           "//div[@class ='link_field']//a[contains(text(),'%s')]" % account_id)
        account.click()
        Logging().reportDebugStep(self, "Open client_account ")
        return CRMTradingAccountsInformationPage()

    '''
        :returns client account from trading accounts tabs 
    '''

    def get_client_account(self):
        account_number = super().wait_load_element("//tr[@class='lvtColData'][1]//td[1]")
        Logging().reportDebugStep(self, "Return the client_account  text " + account_number.text)
        return account_number.text

    '''
       :returns second client account from trading accounts tabs 
    '''

    def get_second_client_account(self):
        account_number = super().wait_load_element("//tr[@class='lvtColData'][2]//td[1]")
        Logging().reportDebugStep(self, "Return the second client account " + account_number.text)
        return account_number.text

    '''
        Open the document tabs  
        :parameter id client account ID 
         returns Client Profile instance    
    '''

    def open_document_tab(self):
        select_country = super().wait_load_element("//a[@id='show_Accounts_Documents']")
        select_country.click()
        Logging().reportDebugStep(self, "Open the document tab ")
        return CRMClientProfilePage()

    '''
        Open the document tabs  
       :parameter id client account ID 
        returns Client Profile instance    
    '''

    def open_document_number(self):
        select_country = super().wait_load_element("//a[contains(text(),'bear.jpg')]/../preceding-sibling::td[2]")
        select_country.click()
        Logging().reportDebugStep(self, "Open the document number ")
        return DocumentDetailViewPage()

    '''
        Returns the status of document from CRM 
    '''

    def get_document_status_text(self):
        document_status = super().wait_load_element("//span[@class ='clientStatusFTD']")
        Logging().reportDebugStep(self, "Return the document status text " + document_status.text)
        return document_status.text

    '''
        Open the help deck tabs  
        :parameter id client account ID 
        returns Client Profile instance    
    '''

    def open_help_desk_tab(self):
        select_country = super().wait_load_element("//a[@id='show_Accounts_HelpDesk']")
        select_country.click()
        Logging().reportDebugStep(self, "Open help desc tab ")
        return CRMClientProfilePage()

    '''
         Open the action of the ticket number
         returns Edition Ticket Info instance    
    '''

    def open_action_help_desk(self):
        account = super().wait_load_element("//a[@class='glyphicons pencil cntrl'][1]")
        account.click()
        Logging().reportDebugStep(self, "Open help desc tab ")
        return EditionTicketInfoPage()

    '''
         Returns the status of ticket 
    '''

    def get_client_status(self):
        client_status = super().wait_load_element("//span[@class ='clientStatusFTD']")
        Logging().reportDebugStep(self, "Return the client status: " + client_status.text)
        return client_status.text

    '''
         Select  the module in the MT4 actions 
    '''

    def open_mt4_actions(self, module):
        mt4_button = super().wait_load_element("//div[@class='mt4_act_box']")
        mt4_button.click()
        sleep(2)
        Logging().reportDebugStep(self, "Open mt4 actions ")
        MT4DropDown().mt4_actions(module)

    def refresh_page(self):
        sleep(5)
        self.driver.refresh()
        Logging().reportDebugStep(self, "The page is refreshed")
        return CRMClientProfilePage()

    def wait_element_is_present(self):
        super().wait_until_element_present("//span[@class ='clientStatusFTD']")
        return CRMClientProfilePage()

    '''
         Returns the initial amount 
    '''

    def get_initial_amount(self):
        initial_amount = super().wait_load_element("//tr[@class='lvtColData'][1]//td[3]")
        total_amount = re.sub('[ ]', '', initial_amount.text)
        Logging().reportDebugStep(self, "Return the total amount text: " + total_amount)
        return total_amount

    '''
         Returns the date birthday 
    '''

    def get_date_birthday(self):
        date = self.driver.find_element(By.XPATH, "//td[contains(text(),'Date Of Birth')]//following-sibling::td[1]")
        parser_data = re.sub('[-]', '', date.text)
        Logging().reportDebugStep(self, "Returns the date birthday:  " + parser_data)
        return parser_data

    '''
         Returns the first name
    '''

    def get_first_name(self):
        first_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'First Name')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the first name: " + first_name.text)
        return first_name.text

    '''
         Returns the phone 
    '''

    def get_phone_text(self):
        phone = self.driver.find_element(By.XPATH, "//td[contains(text(),'Phone')]//following-sibling::td[1]")
        parser_phone_text = re.sub('[+," "]', '', phone.text)
        Logging().reportDebugStep(self, "Returns the first name: " + parser_phone_text)
        return parser_phone_text

    '''
        Returns the last_name
    '''

    def get_last_name(self):
        last_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'Last Name')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the last name:  " + last_name.text)
        return last_name.text

    '''
        Returns the citizenship
    '''

    def get_citizenship_text(self):
        citizenship = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Citizenship')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the citizenship " + citizenship.text)
        return citizenship.text

    '''
        Returns the address 
    '''

    def get_address_text(self):
        self.driver.execute_script("scroll(0, 300);")
        address = self.driver.find_element(By.XPATH, "//td[contains(text(),'Address')]//following-sibling::td[1]")
        print("--------------------------")
        print(address.text)
        parser_address_text = re.sub('[" "]', '', address.text)
        Logging().reportDebugStep(self, "Returns the address :" + parser_address_text)
        return parser_address_text

    '''
        Returns the city
    '''

    def get_city_text(self):
        city = self.driver.find_element(By.XPATH, "//td[contains(text(),'City')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the city: " + city.text)
        return city.text

    '''
        Returns the code
    '''

    def get_code_text(self):
        code = self.driver.find_element(By.XPATH, "//td[contains(text(),'Code')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the code: " + code.text)
        return code.text

    '''
        Returns the country
    '''

    def get_country_text(self):
        country = self.driver.find_element(By.XPATH, "//td[contains(text(),'Country')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the country: " + country.text)
        return country.text
