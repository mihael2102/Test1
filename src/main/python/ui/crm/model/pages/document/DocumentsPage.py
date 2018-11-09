from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.utils.logs.Loging import Logging


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