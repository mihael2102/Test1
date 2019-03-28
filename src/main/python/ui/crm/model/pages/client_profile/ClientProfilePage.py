import re
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from _decimal import Decimal
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.pages.edit_ticket.BrandEditionTicketInfoPage import EditionTicketInfoPage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.client_modules.client_deposit.CRMClientDeposit import CRMClientDeposit
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.modules.tasks_module.SmsNotifier import SmsNotifierModule
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from selenium.webdriver.support.select import Select
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class ClientProfilePage(CRMBasePage):

    '''
        Perform scroll_down
        returns Manage Accounts Module  instance    
    '''

    def perform_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Logging().reportDebugStep(self, "Perform scroll down ")
        sleep(2)
        return ClientProfilePage(self.driver)

    '''
        Perform scroll_down
        returns Manage Accounts Module  instance    
    '''

    def click_trading_accounts_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li//a[contains(text(),'Trading Accounts')][1]")))
        trading_account_tab = super().wait_load_element("//li//a[contains(text(),'Trading Accounts')][1]")
        self.driver.execute_script("arguments[0].click();", trading_account_tab)
        Logging().reportDebugStep(self, "Scroll to trading account section")
        return ClientProfilePage(self.driver)

    def get_client_status(self):
        client_status = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Client Status')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Client status is " + client_status.text)
        return client_status.text

    '''
         Perform scroll_down
         returns Manage Accounts Module  instance    
     '''

    def click_sms_tab(self):
        trading_account_tab = super().wait_element_to_be_clickable("//li//a[contains(text(),'SMS')][1]")
        trading_account_tab.click()
        Logging().reportDebugStep(self, "Open the sms tab ")
        return ClientProfilePage()

    '''
        Open the SMS tab
        returns Manage Accounts Module  instance    
    '''

    def open_sms_tab(self):
        trading_tab = super().wait_element_to_be_clickable("//a[@id='show_Accounts_SMS']")
        trading_tab.click()
        Logging().reportDebugStep(self, "Open the sms tab ")
        return ClientProfilePage()

    def open_sms_view_module(self, sms):
        sms_element_ = super().wait_element_to_be_clickable(
            "//table[@id='rld_table_content']//tr[2]//td[2]//div//a[contains(text(),'%s')]" % sms)
        sms_element_.click()
        Logging().reportDebugStep(self, "Open the sms view  ")
        return SmsNotifierModule()

    '''
        Open the Documents tab
        returns Manage Accounts Module  instance    
    '''

    def open_document_tab(self):
        document_tab = super().wait_element_to_be_clickable("//a[@id='show_Accounts_Documents']")
        document_tab.click()
        Logging().reportDebugStep(self, "Open the document tab ")
        return ClientProfilePage()

    '''
        Open the Documents module
        returns Manage Accounts Module  instance    
    '''

    def open_download_module(self):
        document_tab = super().wait_element_to_be_clickable("//input[@title='Add Document']")
        document_tab.click()
        Logging().reportDebugStep(self, "Open the document module ")
        return CreateDocumentModule()

    def get_counter_sms(self):
        counter_sms = super().wait_element_to_be_clickable("//span[@class='amount amount_SMS']")
        Logging().reportDebugStep(self, "Counter is " + counter_sms.text)
        return int(counter_sms.text)

    '''
         Perform scroll_top
         returns Manage Accounts Module  instance    
     '''

    def perform_scroll_up(self):
        self.driver.execute_script("scroll(0, 0);")
        Logging().reportDebugStep(self, "Perform scroll up ")
        return ClientProfilePage(self.driver)

    '''
        Open the trading tabs
        returns Manage Accounts Module  instance    
    '''

    def open_trading_accounts_tab(self):
        sleep(3)
        trading_tab = super().wait_element_to_be_clickable("//a[@id='show_Accounts_TradingAccounts']")
        # trading_tab.click()
        self.driver.execute_script("arguments[0].click();", trading_tab)
        Logging().reportDebugStep(self, "Open the trading account tab ")
        return ClientProfilePage(self.driver)

    '''
        Open the Finacial Transactions tabs
        returns Manage Accounts Module  instance    
    '''

    def open_financial_transactions_tab(self):
        sleep(1)
        trading_tab = super().wait_load_element("//a[@id='show_Accounts_FinancialTransactions']")
        trading_tab.click()
        Logging().reportDebugStep(self, "Open the financial transactions tab ")
        return ClientProfilePage()

    '''
        :returns client amount from Trading Accounts tabs 
    '''

    def get_amount_text(self, total_amount_crm):
        # Use it after deposit etc. because we need to wait some time
        # while deposit will be applied and displayed at the page
        Logging().reportDebugStep(self, "Returns the amount you placed on the deposit page \n" + total_amount_crm)
        return super().wait_until_element_present(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["deposit_sum"], total_amount_crm)

    '''
        :returns client total amount from Trading Accounts tabs 
    '''

    def get_total_amount_text(self, initial_amount, amount_deposit):
        total_amount = Decimal(initial_amount.replace(",", "")) + Decimal(amount_deposit.replace(",", ""))
        Logging().reportDebugStep(self, "Returns the total amount text " + str(total_amount))
        return str(total_amount)

    '''
        :returns client total amount withdraw from Trading Accounts tabs 
    '''

    def get_difference_amount_text(self, initial_amount, amount_deposit):
        total_amount = Decimal(initial_amount) - Decimal(amount_deposit)
        Logging().reportDebugStep(self, "Returns the total amount " + str(total_amount))
        return str(total_amount)

    def get_amount_of_credit_in(self):
        # add refresh page
        credit_in_amount_element = super().wait_visible_of_element("//*[@id='rld_table_content']/tbody/tr[2]/td[6]/span[1]")
        Logging().reportDebugStep(self, "Amount of Credit in is " + credit_in_amount_element.text)
        return credit_in_amount_element.text

    '''
        Open the client account 
        :parameter id client account ID 
        returns Trading Accounts_Info  instance    
    '''

    def open_client_account_by_account_id(self, account_id):
        super().wait_load_element("//div[@class ='link_field']//a[contains(text(),'%s')]" % account_id)
        account = self.driver.find_element(By.XPATH,
                                           "//div[@class ='link_field']//a[contains(text(),'%s')]" % account_id)
        account.click()
        Logging().reportDebugStep(self, "Open client_account ")
        return TradingAccountsInformationPage()

    '''
        :returns client account from trading accounts tabs 
    '''

    def get_client_account(self):
        sleep(1)
        account_number = super().wait_load_element("(//tr[@class='lvtColData'])[1]//td[1]")
        super().scroll_into_view(account_number)
        account_number = super().wait_load_element("(//tr[@class='lvtColData'])[1]//td[1]")
        Logging().reportDebugStep(self, "Client_account number: " + account_number.text)
        CRMConstants.CREDIT_ACCOUNT = account_number.text
        return account_number.text

    def open_client_account(self):
        account_number = super().wait_visible_of_element("//div[@id='tbl_Accounts_TradingAccounts']//tr[2]//a[2]")
        account_number.click()
        Logging().reportDebugStep(self, "The client account was opened")
        return TradingAccountsInformationPage()

    '''
       :returns second client account from trading accounts tabs 
    '''

    def get_second_client_account(self):
        sleep(3)
        account_number = super().wait_load_element("(//tr[@class='lvtColData'])[2]//td[1]")
        Logging().reportDebugStep(self, "Second client account number: " + account_number.text)
        return account_number.text

    '''
        Open the document tabs  
       :parameter id client account ID 
        returns Client Profile instance    
    '''

    def open_document_number(self):
        select_country = super().wait_load_element("//a[contains(text(),'Bear.jpg')]/../preceding-sibling::td[2]")
        select_country.click()
        Logging().reportDebugStep(self, "Open the document number ")
        return DocumentDetailViewPage()

    '''
        Returns the status of document from CRM 
    '''

    def get_document_status_text(self):
        document_status = super().wait_load_element("//span[@class ='clientStatusFTD']")
        Logging().reportDebugStep(self, "Returns the document status text " + document_status.text)
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
        return ClientProfilePage(self.driver)

    '''
         Open the action of the ticket number
         returns Edition Ticket Info instance    
    '''

    def open_action_help_desk(self):
        account = super().wait_load_element("//a[@class='glyphicons pencil cntrl'][1]")
        account.click()
        Logging().reportDebugStep(self, "Open help desc tab ")
        return EditionTicketInfoPage()

    def get_name_document(self):
        document_name = super().wait_load_element("//tr[@class='lvtColData']//td[3]//a[contains(text(),'Bear.jpg')]")
        Logging().reportDebugStep(self, "Returns the client status: " + document_name.text)
        return document_name.text

    '''
         Returns the status of ticket 
    '''

    def get_live_status_client(self):
        client_status = super().wait_load_element("//span[@class ='clientStatusFTD']")
        Logging().reportDebugStep(self, "Returns the client status: " + client_status.text)
        return client_status.text

    '''
         Select  the module in the MT4 actions 
    '''

    def open_mt4_actions(self, module):
        sleep(3)
        mt4_button = super().wait_load_element("//div[@class='mt4_act_box']")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", mt4_button)
        # mt4_button.click()
        sleep(5)
        Logging().reportDebugStep(self, "Open mt4 actions ")
        MT4DropDown(self.driver).mt4_actions(module)

    def close_popup_new_trading_account(self):
        sleep(1)
        popup_new_trading_account = super().wait_load_element("(//button[@class = 'btn btn-primary'])[2]")
        self.driver.execute_script("arguments[0].click();", popup_new_trading_account)
        sleep(2)
        return ClientProfilePage(self.driver)

    def wait_element_is_present(self):
        super().wait_until_element_present("//span[@class ='clientStatusFTD']")
        return ClientProfilePage(self.driver)

    '''
         Returns the initial amount 
    '''

    def get_initial_amount(self):
        initial_amount = super().wait_load_element("//tr[@class='lvtColData'][1]//td[3]")
        total_amount = re.sub('[$£CA€ [ ]', '', initial_amount.text)
        Logging().reportDebugStep(self, "Return initial amount text: " + total_amount)
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
        Logging().reportDebugStep(self, "Returns the phone number: " + parser_phone_text)
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
        parser_address_text = re.sub('[" "]', '', address.text)
        Logging().reportDebugStep(self, "Returns the address :" + parser_address_text)
        return parser_address_text

    '''
        Returns the email 
    '''

    def get_email_text(self):
        email = self.driver.find_element(By.XPATH,
                                         global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["email"])
        Logging().reportDebugStep(self, "Returns the email " + email.text)
        return email.text

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

    def perform_scroll(self, parameter):
        Logging().reportDebugStep(self, "Perform  the scroll")
        super().perform_scroll(parameter)

    '''
        Click Ok in the Deposit module
        :returns CRM Client Profile Page instance
    '''

    def click_ok(self):
        super().click_ok()
        Logging().reportDebugStep(self, "Click 'ok' button ")
        return ClientProfilePage(self.driver)

    '''
         Returns a confirmation  message if the user entered a valid password
    '''

    def get_confirm_message(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns a confirmation message: " + confirm_message.text)
        return confirm_message.text

    def refresh_page(self):
        super().refresh_page()
        return ClientProfilePage(self.driver)

    def get_gender_text(self):
        country = self.driver.find_element(By.XPATH, "//td[contains(text(),'Gender')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the gender: " + country.text)
        return country.text

    def get_assigned_to_text(self):
        assigned_to = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Assigned To')]//following-sibling::td[1]")
        new_line = assigned_to.text.strip()

        Logging().reportDebugStep(self, "Returns the assigned to: " + new_line)
        return new_line

    def get_client_source_text(self):
        client_source = self.driver.find_element(By.XPATH,
                                                 "//td[contains(text(),'Client Source')]//following-sibling::td[1]")
        parser_client_source_text = re.sub('[" "]', '', client_source.text, 1)
        Logging().reportDebugStep(self, "Returns the client source: " + parser_client_source_text)
        return parser_client_source_text

    def get_compliance_agent_text(self):
        compliance_agent = self.driver.find_element(By.XPATH,
                                                    "//td[contains(text(),'Compliance Agent')]//following-sibling::td[1]")

        new_line = compliance_agent.text.strip()
        Logging().reportDebugStep(self, "Returns the compliance_agent source: " + new_line)
        return new_line

    def get_compliance_notes_text(self):
        compliance_notes = self.driver.find_element(By.XPATH,
                                                    "//td[contains(text(),'Compliance Notes')]//following-sibling::td[1]")
        parser_compliance_notes_text = re.sub('[" "]', '', compliance_notes.text, 1)
        Logging().reportDebugStep(self, "Returns the compliance notes source: " + parser_compliance_notes_text)
        return parser_compliance_notes_text

    def get_client_status_text(self):
        client_status = self.driver.find_element(By.XPATH,
                                                 "//td[contains(text(),'Client Status')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the client status source: " + client_status.text)
        return client_status.text

    def get_retention_status_text(self):
        retention_status = self.driver.find_element(By.XPATH,
                                                    "//td[contains(text(),'Retention Status')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the retention status source: " + retention_status.text)
        return retention_status.text

    def get_description_text(self):
        description = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Description')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the description : " + description.text)
        return description.text

    def get_referral_text(self):
        self.perform_scroll(400)
        custom_info = self.driver.find_element(By.XPATH,
                                               "//b[contains(text(),'Custom Information')]")
        custom_info.click()

        referral = self.driver.find_element(By.XPATH,
                                            "//td[contains(text(),'Refferal')]//following-sibling::td[1]")
        parser_client_status_text = re.sub('[" "]', '', referral.text, 3)
        Logging().reportDebugStep(self, "Returns the referral : " + parser_client_status_text)
        return parser_client_status_text

    def open_deposit_for_client_in_menu(self):
        deposit_for_client_element = self.driver.find_element(By.XPATH, "//*[@id='sidebar']/table[1]/tbody/tr[4]/td/a")
        self.driver.execute_script("arguments[0].click();", deposit_for_client_element)
        # deposit_for_client_element.click()
        Logging().reportDebugStep(self, "Deposit for client popup was opened")
        return ClientProfilePage(self.driver)

    def fill_client_deposit_pop(self, account_number):
        try:
            trading_account_dropdown_list = super().wait_element_to_be_clickable(
                "//*[@id='ClientDepositConfirmation']//button[@title='Choose trading account']", 10)
            trading_account_dropdown_list.click()
            selected_live_trading_account = self.driver.find_element(By.XPATH,
                                                                     "//span[contains(text(), '%s')]" % account_number)
            super().scroll_into_view(selected_live_trading_account)
            selected_live_trading_account.click()
        except (NoSuchElementException, TimeoutException) as e:
            Logging().reportDebugStep(self, "There is no accounts drop down list")
        try:
            i_confirm_checkbox = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["i_confirm_checkbox"])
        except TimeoutException:
            # If client deposit popup hasn't been loaded completely,
            # we need to refresh the page and try to open popup again
            super().refresh_page()
            self.open_deposit_for_client_in_menu()
            try:
                trading_account_dropdown_list = super().wait_element_to_be_clickable(
                    "//*[@id='ClientDepositConfirmation']//button[@title='Choose trading account']", 10)
                trading_account_dropdown_list.click()
                selected_live_trading_account = self.driver.find_element(By.XPATH,
                                                                         "//span[contains(text(), '%s')]" % account_number)
                super().scroll_into_view(selected_live_trading_account)
                selected_live_trading_account.click()
            except (NoSuchElementException, TimeoutException) as e:
                Logging().reportDebugStep(self, "There is no accounts drop down list")
            i_confirm_checkbox = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["i_confirm_checkbox"])

        i_confirm_checkbox.click()
        ok_button = super().wait_element_to_be_clickable("//*[@id='confirmationform_action_button']")
        ok_button.click()
        Logging().reportDebugStep(self, "Click OK in Client Deposit popup")
        return CRMClientDeposit(self.driver)

    def Sign_Out(self):
        CRMBasePage(self.driver).refresh_page()
        sleep(2)
        user = super().wait_element_to_be_clickable("//img[@src='themes/panda/images/user.PNG']")
        # self.driver.execute_script("arguments[0].click();", user)
        user.click()
        sleep(2)
        sign_out = super().wait_element_to_be_clickable("//a[contains(text(), 'Sign Out')]")
        self.driver.execute_script("arguments[0].click();", sign_out)
        Logging().reportDebugStep(self, "Sign Out")
        return ClientProfilePage(self.driver)

    def click_activities_tab(self):
        activities_tab = super().wait_element_to_be_clickable("//li//a[contains(text(),'Activities')][1]")
        # activities_tab.click()
        self.driver.execute_script("arguments[0].click();", activities_tab)
        Logging().reportDebugStep(self, "Scroll to activities tab")
        return ClientProfilePage(self.driver)

    def open_activities_tab(self):
        sleep(1)
        activities_tab = super().wait_load_element("//a[@id='show_Accounts_Activities']")
        self.driver.execute_script("arguments[0].click();", activities_tab)
        Logging().reportDebugStep(self, "Open Activities tab ")
        return ClientProfilePage(self.driver)

    def click_delete_interaction(self):
        sleep(1)
        delete_interaction = super().wait_element_to_be_clickable("//*[@id='rld_table_content']/tbody/tr[2]/td[13]/div/div/a[2]")
        self.driver.execute_script("arguments[0].click();", delete_interaction)
        Logging().reportDebugStep(self, "Press Delete button")
        return ClientProfilePage(self.driver)

    def verify_delete_interaction_message(self, expected_message):
        sleep(1)
        delete_interaction_message = self.driver.find_element_by_xpath("//div[@class='bootstrap-dialog-message']").text
        assert expected_message == delete_interaction_message
        Logging().reportDebugStep(self, "Delete interaction message is verified")
        return ClientProfilePage(self.driver)

    def confirm_delete_interaction(self):
        delete_interaction_btn = super().wait_load_element("//button[contains(text(), 'OK')]")
        delete_interaction_btn.click()
        Logging().reportDebugStep(self, "Delete interaction is confirmed")
        return ClientProfilePage(self.driver)

    def interaction_successfully_deleted_message(self, expected_message):
        sleep(1)
        delete_interaction_message = self.driver.find_element_by_xpath("//div[@class='bootstrap-dialog-message']").text
        assert expected_message == delete_interaction_message
        ok_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'OK')]")
        self.driver.execute_script("arguments[0].click();", ok_btn)
        Logging().reportDebugStep(self, "Interaction was deleted successfully")
        return ClientProfilePage(self.driver)

    def check_event_exist(self):
        sleep(1)
        super().refresh_page()
        sleep(3)
        activities_counter = self.driver.find_element_by_xpath("//span[@class='amount amount_Activities']").text
        if (int(activities_counter) != 0):
            Logging().reportDebugStep(self, "Client's page contain events")
            return True
        else:
            Logging().reportDebugStep(self, "Client's page does not contain events")
            return False

    def scroll_to_financial_transactions_section(self):
        sleep(1)
        financial_transactions_section = super().wait_element_to_be_clickable("//a[@href='#header_Accounts_FinancialTransactions']")
        self.driver.execute_script("arguments[0].click();", financial_transactions_section)
        Logging().reportDebugStep(self, "Scroll to Financial Transactions section")
        return ClientProfilePage(self.driver)

    def get_trading_account_number(self):
        sleep(1)
        trading_account = self.driver.find_element_by_xpath("//*[@id='rld_table_content']/tbody/tr[2]/td[2]")
        trading_account_number = trading_account.text
        Logging().reportDebugStep(self, "Account number is " + trading_account_number)
        return trading_account_number

    def get_balance_in_trading_account(self):
        balance = super().wait_load_element("//*[@id='dtlview_Balance']").text
        Logging().reportDebugStep(self, "Verify balance")
        return balance

    def open_trading_account_page(self, account_number):
        sleep(2)
        link_trading_account = super().wait_load_element(
            "//tr[@class='lvtColData']/td/span/a[contains(text(), '%s')]" % account_number)
        sleep(1)
        self.driver.execute_script("arguments[0].click();", link_trading_account)
        Logging().reportDebugStep(self, "Open the trading account page ")
        return ClientProfilePage(self.driver)

    def change_client_status_with_pencil(self, status):
        sleep(2)
        edit_personal_details = super().wait_load_element("//*[@id='mouseArea_Client Status']")
        edit_personal_details.click()
        sleep(1)
        pencil = super().wait_load_element("//*[@id='crmspanid']/a/span")
        try:
            pencil.click()
        except:
            self.driver.execute_script("arguments[0].click();", pencil)
        sleep(1)
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='txtbox_Client Status']"))
        select.select_by_visible_text(status)
        sleep(1)
        save_personal_details = super().wait_load_element("//*[@id='editarea_Client Status']/div/a[1]/span")
        try:
            save_personal_details.click()
        except:
            self.driver.execute_script("arguments[0].click();", save_personal_details)
        Logging().reportDebugStep(self, "Click Edit")
        return ClientProfilePage(self.driver)


    def click_edit_personal_detail(self):
        sleep(2)
        btn_edit = self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr/td/div/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/input")
        btn_edit.click()
        Logging().reportDebugStep(self, "Click Edit")
        return ClientProfilePage(self.driver)

    def select_country(self, country):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='countries_popup']"))
        select.select_by_visible_text(country)
        Logging().reportDebugStep(self, "Select country" + country)
        return ClientProfilePage(self.driver)


    def click_save(self):
        sleep(2)
        btn_save = self.driver.find_element(By.XPATH,
                                            "//*[@id='updateBLform']/div[3]/input[2]")
        btn_save.click()
        Logging().reportDebugStep(self, "Click Save")
        return ClientProfilePage(self.driver)

    def enter_date_birth(self, date):
        sleep(2)
        if global_var.current_brand_name != "q8":
            btn_save = self.driver.find_element(By.XPATH,
                                                "//*[@id='birthday']")
            btn_save.clear()
            btn_save.send_keys(date)
        Logging().reportDebugStep(self, "Enter b-day")
        return ClientProfilePage(self.driver)

    def get_trading_account_info(self):
        info = self.driver.find_element_by_xpath("//*[@id='rld_table_content']/tbody/tr[2]").text
        Logging().reportDebugStep(self, "Get trading account information")
        return info

    def get_first_account_currency(self):
        currency = self.driver.find_element_by_xpath("//*[@id='rld_table_content']/tbody/tr[2]/td[10]").text
        Logging().reportDebugStep(self, "First trading account currency is: " + currency)
        return currency

    def get_second_account_currency(self):
        currency = self.driver.find_element_by_xpath("//*[@id='rld_table_content']/tbody/tr[3]/td[10]").text
        Logging().reportDebugStep(self, "Second trading account currency is: " + currency)
        return currency

    def get_trading_account_number_from_ta(self, account_number):
        ta_number = self.driver.find_element_by_xpath("//*[@id='rld_table_content']/tbody/tr[%s]/td[1]"
                                                                            % account_number).get_attribute("innerText")
        Logging().reportDebugStep(self, "Trading account number is: " + ta_number)
        return ta_number

    def get_balance_of_trading_account(self, account):
        sleep(2)
        balance = super().wait_load_element("//*[@id='rld_table_content']/tbody/tr[%s]/td[5]/span[1]" % account)
        total_amount = re.sub('[$£CA€ [ ]', '', balance.text)
        Logging().reportDebugStep(self, "Balance of trading account is: " + total_amount)
        return total_amount