from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.utils.logs.Loging import Logging
import autoit
import os


class DocumentsPage(CRMBasePage):

    # def __init__(self):
    #     super().__init__()

    def open_create_filter_pop_up(self):
        element = super().wait_element_to_be_clickable("//a[contains(text(),'Create Filter')]")
        self.driver.execute_script("arguments[0].click();", element)
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterPage(self.driver)

    def open_create_document_module(self):
        document_module = self.driver.find_element(By.XPATH, "//button[@title='Create Document']")
        document_module.click()
        Logging().reportDebugStep(self, "The Create Document module was opened")
        return CreateDocumentModule()

    def browse_documents(self):
        sleep(2)
        browse_documents = self.driver.find_element(By.XPATH, "//div/span[contains(text(),'Browse')]")
        browse_documents.click()
        # autoit.win_wait_active("Открытие")
        autoit.win_wait_active("Open")
        autoit.send("Bear.jpg")
        # autoit.send("Bear")
        autoit.send("{ENTER}")
        Logging().reportDebugStep(self, "Click on button Browse")
        return DocumentsPage()

    def select_document_type(self, type):
        sleep(2)
        document_type = Select(self.driver.find_element(By.XPATH, "//*[@id='doctype']"))
        document_type.select_by_visible_text(type)
        Logging().reportDebugStep(self, "Select document type")
        return DocumentsPage()

    def select_document_status(self, status):
        sleep(1)
        document_type = Select(self.driver.find_element(By.XPATH, "//*[@id='doc_status']"))
        document_type.select_by_visible_text(status)
        Logging().reportDebugStep(self, "Select document status")
        return DocumentsPage()

    def select_document_sub_type(self, sub_type):
        sleep(1)
        document_type = Select(self.driver.find_element(By.XPATH, "//*[@id='docsubtype']"))
        document_type.select_by_visible_text(sub_type)
        Logging().reportDebugStep(self, "Select document sub type")
        return DocumentsPage()

    def input_message(self, msg):
        sleep(1)
        input_message = self.driver.find_element(By.XPATH, "//*[@id='notecontent']")
        input_message.send_keys(msg)
        Logging().reportDebugStep(self, "Fill comments")
        return DocumentsPage()

    def input_expiry_date(self, date):
        expiry_date = self.driver.find_element(By.XPATH, "//*[@id='crm_expiry_date']")
        expiry_date.send_keys(date)
        Logging().reportDebugStep(self, "Fill date")
        return DocumentsPage()


    def attached_to(self, client_attached):
        user_attached = self.driver.find_element(By.XPATH, "//*[@id='upload_document']/div[2]/div[1]/div/div/img[1]")
        user_attached.click()
        sleep(10)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        sleep(5)
        input_attached = self.driver.find_element(By.XPATH, "//*[@id='search_txt']")
        input_attached.send_keys(client_attached)
        sleep(3)
        document_type = Select(self.driver.find_element(By.XPATH, "//select[@name='search_field']"))
        document_type.select_by_visible_text("Client Name")
        sleep(3)
        button_click_search = self.driver.find_element(By.XPATH, "//input[@name='search']")
        button_click_search.click()
        sleep(3)
        select_client = self.driver.find_element(By.XPATH, "//a[contains(text(),'testqa')]")
        select_client.click()
        Logging().reportDebugStep(self, "Click attached To")
        return DocumentsPage()

    def save_document(self):
        sleep(2)
        window_after = self.driver.window_handles[0]
        self.driver.switch_to_window(window_after)
        sleep(2)
        button_save = self.driver.find_element(By.XPATH, "//*[@id='save_document']")
        button_save.click()
        Logging().reportDebugStep(self, "Save document")
        return DocumentsPage()


    def get_successful_message(self):
        message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "The message is : " + message.text)
        return message.text

    '''
        Click Ok in the Deposit module
        :returns CRM Client Profile Page instance
    '''

    def click_ok(self):
        super().click_ok()
        return DocumentsPage()

    def open_pending_tab(self):
        sleep(2)
        pending_tab_element = super().wait_element_to_be_clickable("//a[contains(text(),'Pending')]")
        pending_tab_element.click()
        Logging().reportDebugStep(self, "The pending tab was opened ")
        return DocumentsPage()

    def open_document_number(self):
        pending_tab_element = self.driver.find_element(By.XPATH,
                                                       "//tbody[@id='listBody']//tr[1]//td[2]")
        pending_tab_element.click()
        Logging().reportDebugStep(self, "The document number was opened ")
        return DocumentDetailViewPage()

    def select_document_by_delete_button(self):
        check_box = super().wait_element_to_be_clickable("//tbody[@id='listBody']//tr[1]//td[7]//a[2]")
        check_box.click()
        Logging().reportDebugStep(self, "Delete document module was opened ")
        return DocumentsPage()

    def click_yes_button(self):
        check_box = super().wait_element_to_be_clickable("//button[contains(text(),'Yes')]")
        check_box.click()
        Logging().reportDebugStep(self, "Click the Yes button was performed ")
        return DocumentsPage()

    def get_all_tab_text(self):
        pending_tab_element = super().wait_element_to_be_clickable("//a[contains(text(),'All')]")
        pending_tab_element.click()
        sleep(1)
        pending_tab_text = super().wait_element_to_be_clickable("//a[contains(text(),'All')]")
        Logging().reportDebugStep(self, "The first tab is : " + pending_tab_text.text)
        return pending_tab_text.text

    def get_approved_tab_name_text(self):
        approved_tab_element = super().wait_element_to_be_clickable("//a[contains(text(),'Approved')]")
        approved_tab_element.click()
        sleep(1)
        approved__tab_text = super().wait_element_to_be_clickable("//a[contains(text(),'Approved')]")
        Logging().reportDebugStep(self, "The second tab is : " + approved__tab_text.text)
        return approved__tab_text.text

    def get_not_approved_text(self):
        not_approved_tab_element = super().wait_element_to_be_clickable("//a[contains(text(),'Not Approved')]")
        not_approved_tab_element.click()
        sleep(1)
        not_approved__tab_text = super().wait_element_to_be_clickable("//a[contains(text(),'Not Approved')]")
        Logging().reportDebugStep(self, "The second tab is : " + not_approved__tab_text.text)
        return not_approved__tab_text.text

    def get_pending_tab_text(self):
        pending_tab_element = super().wait_element_to_be_clickable("//a[contains(text(),'Pending')]")
        pending_tab_element.click()
        sleep(1)
        pending_tab_text = super().wait_element_to_be_clickable("//a[contains(text(),'Pending')]")
        Logging().reportDebugStep(self, "The fourth tab is : " + pending_tab_text.text)
        return pending_tab_text.text

    def get_first_name_column(self):
        name_first_column = super().wait_element_to_be_clickable(
            "//table//td[@class='lvtCol'][2]/a")
        Logging().reportDebugStep(self, "First column name  : " + name_first_column.text)
        return name_first_column.text

    def get_second_name_column(self):
        name_second_column = self.driver.find_element(By.XPATH,
                                                      "//table//td[@class='lvtCol'][3]/a")
        Logging().reportDebugStep(self, "Second column name: " + name_second_column.text)
        return name_second_column.text

    def get_third_name_column(self):
        name_third_column = self.driver.find_element(By.XPATH,
                                                     "//table//td[@class='lvtCol'][4]/a")
        Logging().reportDebugStep(self, "Third column name: " + name_third_column.text)
        return name_third_column.text

    def get_fourth_name_column(self):
        name_fourth_column = self.driver.find_element(By.XPATH,
                                                      "//table//td[@class='lvtCol'][5]/a")
        Logging().reportDebugStep(self, "Fourth column name : " + name_fourth_column.text)
        return name_fourth_column.text

    def Sign_Out(self):
        CRMBasePage(self.driver).refresh_page()
        sleep(2)
        user = super().wait_element_to_be_clickable("//img[@src='themes/panda/images/user.PNG']")
        # self.driver.execute_script("arguments[0].click();", user)
        user.click()
        sleep(2)
        sign_out = super().wait_element_to_be_clickable("//a[contains(text(), 'Sign Out')]")
        self.driver.execute_script("arguments[0].click();", sign_out)
        Logging().reportDebugStep(self, "'Sign_Out")
        return DocumentsPage(self.driver)

    def search_by_attached_to(self, client_name):
        input_attached_to = self.driver.find_element(By.XPATH, "//*[@id='tks_crmid']")
        input_attached_to.send_keys(client_name)
        Logging().reportDebugStep(self, "Fill attached to")
        return DocumentsPage(self.driver)

    def search_document_module(self):
        button_search = super().wait_element_to_be_clickable("//input[@id='tks_searchbutton']")
        button_search.click()
        Logging().reportDebugStep(self, "Click Search")
        return DocumentsPage(self.driver)

    def open_doc(self):
        sleep(3)
        id_doc = super().wait_element_to_be_clickable("//a[contains(text(), 'DOC')]")
        id_doc.click()
        Logging().reportDebugStep(self, "Open document details")
        return DocumentsPage(self.driver)

    def get_attached_to(self):
        field_attached_to = self.driver.find_element(By.XPATH, "//*[@id='tblBasicInformation']/table/tbody/tr[3]/td[4]/a").text
        Logging().reportDebugStep(self, "Get client name from document details page")
        return field_attached_to

    def get_status(self):
        field_status = self.driver.find_element(By.XPATH, "//*[@id='tblBasicInformation']/table/tbody/tr[4]/td[4]").text
        Logging().reportDebugStep(self, "Get status from document details page")
        return field_status

    def get_link(self):
        field_status = self.driver.find_element(By.XPATH, "//*[@id='tblFileInformation']/table/tbody/tr[1]/td[4]").text
        Logging().reportDebugStep(self, "Get link from document details page")
        return field_status


