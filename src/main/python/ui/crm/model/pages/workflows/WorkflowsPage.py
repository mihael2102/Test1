import re
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from _decimal import Decimal
from time import sleep
from selenium.webdriver.support.select import Select
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
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WorkflowsPage(CRMBasePage):

    def confirmation_delete_workflow(self):
        sleep(2)
        btn_delete_workflow = self.driver.find_element_by_xpath(
            "//span[text()=' Delete ']")
        btn_delete_workflow.click()
        sleep(1)
        Logging().reportDebugStep(self, "Click Delete button")
        return WorkflowsPage(self.driver)

    def delete_workflow(self):
        sleep(2)
        more_btn = super().wait_element_to_be_clickable("//mat-icon[text()='more_vert']")
        more_btn.click()
        btn_delete_workflow = self.driver.find_element_by_xpath("//mat-icon[text()='delete']")
        btn_delete_workflow.click()
        Logging().reportDebugStep(self, "Click delete workflow")
        return WorkflowsPage(self.driver)


    def check_name_workflow(self, name):
        sleep(3)
        name_workflow = self.driver.find_element_by_xpath("//span[text()='%s']" % name)
        Logging().reportDebugStep(self, "Check name workflow in table")
        return name_workflow.text


    def click_add_new_workflow(self):
        sleep(2)
        btn_add_new_workflow = self.driver.find_element_by_xpath("//span[contains(text(), 'New Workflow')]")
        btn_add_new_workflow.click()
        Logging().reportDebugStep(self, "Click add new workflow")
        return WorkflowsPage(self.driver)

    def enter_workflow_name(self, name):
        sleep(3)
        input = self.driver.find_element_by_xpath("//input[@id='wf_name']")
        input.send_keys(name)
        Logging().reportDebugStep(self, "Enter workflow name: " + name)
        return WorkflowsPage(self.driver)

    def enter_workflow_priority(self, priority):
        sleep(2)
        input = self.driver.find_element_by_xpath("//input[@id='wf_priority']")
        input.send_keys(priority)
        Logging().reportDebugStep(self, "Enter workflow priority: " + priority)
        return WorkflowsPage(self.driver)

    def click_radio_btn_modified(self):
        sleep(2)
        radio_btn = self.driver.find_element_by_xpath("//span[text()='Every time the record is modified.']")
        radio_btn.click()
        Logging().reportDebugStep(self, "Click Every time the record is modified")
        return WorkflowsPage(self.driver)

    def select_second_country(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
            "(//div[contains(@class,'select-wrap')]/select[contains(@class,'condition-value')])[2]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select Clients Country" + name)
        return WorkflowsPage(self.driver)

    def click_next(self):
        sleep(2)
        btn_next = self.driver.find_element_by_xpath("//span[contains(text(), 'Next')]")
        btn_next.click()
        Logging().reportDebugStep(self, "Click Next")
        return WorkflowsPage(self.driver)

    def select_module(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//div[@class='select-filter']")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "//span[@class='filter-search-container']/input[@placeholder='Search...']")
        clients.send_keys(name)
        sleep(2)
        select = self.driver.find_element_by_xpath("//span[contains(text(), '%s')]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select Clients module")
        return WorkflowsPage(self.driver)

    def click_add_condition(self):
        sleep(2)
        btn_add_condition = self.driver.find_element_by_xpath("//button[contains(text(), 'Add Condition Group')]")
        btn_add_condition.click()
        Logging().reportDebugStep(self, "Click add condition")
        return WorkflowsPage(self.driver)

    def select_accept_promotions(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//div[@class='multi-select-title']/span[contains(text(),'Accept')]")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "(//span[@class='filter-search-container']/input[@placeholder='Search...'])[2]")
        clients.send_keys(name)
        sleep(2)
        select = self.driver.find_element_by_xpath("//span[text()=' %s ']" % name)
        select.click()
        Logging().reportDebugStep(self, "Select Clients Status")
        return WorkflowsPage(self.driver)

    def select_condition(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
            "//div[@class='select-wrap']/select[contains(@class,'condition-operator')]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition: " + name)
        return WorkflowsPage(self.driver)

    def select_status(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
                                    "//div[contains(@class,'select-wrap')]/select[contains(@class,'condition-value')]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select Clients Status: " + name)
        return WorkflowsPage(self.driver)

    def select_second_accept_promotions(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//div[@class='multi-select-title']/span[contains(text(),'Accept')]")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "//div[@class='select-options options-enabled']/span[@class='filter-search-container']/input[@placeholder='Search...']")
        clients.send_keys(name)
        sleep(3)
        select = self.driver.find_element_by_xpath("(//span[text()=' %s '])[2]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select " + name)
        return WorkflowsPage(self.driver)

    def select_second_condition(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
            "(//div[@class='select-wrap']/select[contains(@class,'condition-operator')])[2]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition: " + name)
        return WorkflowsPage(self.driver)

    def click_enter_email(self):
        sleep(2)
        btn_next = self.driver.find_element_by_xpath("//input[contains(@class,'condition-value')]")
        btn_next.click()
        Logging().reportDebugStep(self, "Click enter email")
        return WorkflowsPage(self.driver)

    def enter_email(self, email):
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "(//textarea[contains(@class,'form-control')])[3]")
        clients.send_keys(email)
        Logging().reportDebugStep(self, "Emaer email: " + email)
        return WorkflowsPage(self.driver)

    def click_save_value(self):
        sleep(2)
        btn_next = self.driver.find_element_by_xpath(
            "(//button[text()='Save '])[3]")
        btn_next.click()
        Logging().reportDebugStep(self, "Click Save")
        return WorkflowsPage(self.driver)

    def select_second_condition_between(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
            "(//div[contains(@class,'select-wrap')]/select[contains(@class,'form-control')])[6]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition: " + name)
        return WorkflowsPage(self.driver)

    def select_condition_between(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
            "(//div[contains(@class,'select-wrap')]/select[contains(@class,'form-control')])[3]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition: " + name)
        return WorkflowsPage(self.driver)

    def select_third_accept_promotions(self, name):
        sleep(2)
        self.perform_scroll_down()
        module = self.driver.find_element_by_xpath("//div[@class='multi-select-title']/span[contains(text(),'Accept')]")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "//div[@class='select-options options-enabled']/span[@class='filter-search-container']/input[@placeholder='Search...']")
        clients.send_keys(name)
        sleep(3)
        select = self.driver.find_element_by_xpath(
            "(//span[text()=' %s '])[3]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select: " + name)
        return WorkflowsPage(self.driver)

    def select_third_conditions(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
            "(//div[@class='select-wrap']/select[contains(@class,'condition-operator')])[3]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition: " + name)
        return WorkflowsPage(self.driver)

    def select_add_task(self, name):
        sleep(2)
        btn_add_task = self.driver.find_element_by_xpath("//span[text()='Add Task']")
        btn_add_task.click()
        sleep(2)
        select = self.driver.find_element_by_xpath("//span[text()='%s']" % name)
        select.click()
        Logging().reportDebugStep(self, "Click Add Task and select: " + name)
        return WorkflowsPage(self.driver)

    def enter_task_title(self, name):
        sleep(2)
        input = self.driver.find_element_by_xpath("//input[@placeholder='Task Title']")
        input.send_keys(name)
        Logging().reportDebugStep(self, "Enter task title " + name)
        return WorkflowsPage(self.driver)

    def click_add_field(self):
        sleep(2)
        btn_add_field = self.driver.find_element_by_xpath("//button/b[contains(text(), 'Add Field')]")
        btn_add_field.click()
        Logging().reportDebugStep(self, "Click add field")
        return WorkflowsPage(self.driver)

    def select_field(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//span[text()='Select field']")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath("//span/input[@placeholder='Search...']")
        clients.send_keys(name)
        sleep(3)
        select = self.driver.find_element_by_xpath(
            "//span[contains(text(), ' %s ')]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select: " + name)
        return WorkflowsPage(self.driver)

    def click_enter_value(self):
        sleep(2)
        btn = self.driver.find_element_by_xpath("//div[@class='col-md-6']/input[contains(@class, 'form-control')]")
        btn.click()
        Logging().reportDebugStep(self, "Click enter value")
        return WorkflowsPage(self.driver)

    def enter_value(self, name):
        sleep(2)
        textarea = self.driver.find_element_by_xpath("//div[@class='row current-value']/textarea")
        textarea.send_keys(name)
        Logging().reportDebugStep(self, "Enter value " + name)
        return WorkflowsPage(self.driver)

    def click_save_value_task(self):
        sleep(2)
        btn_save = self.driver.find_element_by_xpath("(//button[text()='Save '])[2]")
        btn_save.click()
        Logging().reportDebugStep(self, "Click Save")
        return WorkflowsPage(self.driver)

    def select_second_field(self, name):
        sleep(2)
        select = self.driver.find_element_by_xpath("//span[text()='Select field']")
        select.click()
        clients = self.driver.find_element_by_xpath(
            "(//span/input[@placeholder='Search...'])[2]")
        clients.send_keys(name)
        sleep(3)
        select = self.driver.find_element_by_xpath(
            "(//span[text()=' %s '])[2]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select " + name)
        return WorkflowsPage(self.driver)

    def select_country(self, name):
        sleep(2)
        select = Select(self.driver.find_element_by_xpath(
            "//div[@class='col-md-6']/select[contains(@class,'form-control')]"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition " + name)
        return WorkflowsPage(self.driver)

    def click_save_task(self):
        sleep(2)
        btn_save = self.driver.find_element_by_xpath("(//button[text()='Save '])[1]")
        btn_save.click()
        Logging().reportDebugStep(self, "Click Save")
        return WorkflowsPage(self.driver)

    def click_save_workflow(self):
        sleep(2)
        btn_save = self.driver.find_element_by_xpath("//span[text()=' Save ']")
        btn_save.click()
        Logging().reportDebugStep(self, "Click Save")
        return WorkflowsPage(self.driver)

    def search_workflow_by_name(self, name):
        sleep(2)
        try:
            name_field = super().wait_element_to_be_clickable(
                "//div[@class='mat-form-field-infix']/input[@placeholder='Search' and @id='mat-input-4']")
        except:
            name_field = super().wait_element_to_be_clickable(
                "//div[@class='mat-form-field-infix']/input[@id='mat-input-3']")
        name_field.clear()
        name_field.send_keys(name)
        sleep(2)
        Logging().reportDebugStep(self, "Searching by workflow name: " + name)
        return WorkflowsPage(self.driver)

    def check_workflow_not_found(self):
        sleep(1)
        super().wait_load_element("//tr[@class='no-results']/td[text()='No results']")
        Logging().reportDebugStep(self, "'No results' message is displayed")
        return WorkflowsPage(self.driver)
