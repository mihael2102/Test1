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
            "/html/body/bs-modal[7]/div/div/div/div[2]/form/div/span/span[1]/button")
        btn_delete_workflow.click()
        Logging().reportDebugStep(self, "Click OK")
        return WorkflowsPage(self.driver)

    def delete_workflow(self):
        sleep(2)
        btn_delete_workflow = self.driver.find_element_by_xpath\
            ("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-list/div/div/div/div[2]/div/grid-simple/div/div[2]/table/tbody/tr[3]/td[6]/div[4]")
        btn_delete_workflow.click()
        Logging().reportDebugStep(self, "Click delete workflow")
        return WorkflowsPage(self.driver)

    def check_name_workflow(self):
        sleep(2)
        try:
            self.wait_element_to_be_disappear("//div[@class='spinner']", timeout=95)
        except TimeoutException:
            self.refresh_page()
            self.wait_element_to_be_disappear("//div[@class='spinner']", timeout=95)
        name_workflow = self.driver.find_element_by_xpath\
            ("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-list/div/div/div/div[2]/div/grid-simple/div/div[2]/table/tbody/tr[3]/td[1]/div")
        Logging().reportDebugStep(self, "Check name workflow in table")
        return name_workflow.text

    def click_add_new_workflow(self):
        sleep(5)
        try:
            self.wait_element_to_be_disappear("//div[@class='spinner']", timeout=95)
        except TimeoutException:
            self.refresh_page()
            self.wait_element_to_be_disappear("//div[@class='spinner']", timeout=95)
        btn_add_new_workflow = super().wait_element_to_be_clickable("//button[contains(text(), 'New Workflow')]")
        btn_add_new_workflow.click()
        Logging().reportDebugStep(self, "Click 'New Workflow' button")
        return WorkflowsPage(self.driver)

    def enter_workflow_name(self, name):
        sleep(2)
        input = self.driver.find_element_by_xpath("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-type/div[2]/div/div[1]/div[2]/input")
        input.send_keys(name)
        Logging().reportDebugStep(self, "Enter workflow name")
        return WorkflowsPage(self.driver)

    def enter_workflow_priority(self, priority):
        sleep(2)
        input = self.driver.find_element_by_xpath("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-type/div[2]/div/div[2]/div[2]/input")
        input.send_keys(priority)
        Logging().reportDebugStep(self, "Enter workflow priority")
        return WorkflowsPage(self.driver)

    def click_radio_btn_modified(self):
        sleep(2)
        radio_btn = self.driver.find_element_by_xpath("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-type/div[2]/div/div[3]/div[2]/div[4]/label/input")
        radio_btn.click()
        Logging().reportDebugStep(self, "Click Every time the record is modified")
        return WorkflowsPage(self.driver)

    def select_second_country(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[2]/div/div[3]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select Client's Country: " + name)
        return WorkflowsPage(self.driver)

    def click_next(self):
        sleep(2)
        btn_next = self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
        btn_next.click()
        Logging().reportDebugStep(self, "Click Next")
        return WorkflowsPage(self.driver)

    def select_module(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//div[@class='select-filter']")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[1]/div[2]/select-search/div/div[2]/span[1]/input")
        clients.send_keys(name)
        sleep(2)
        select = self.driver.find_element_by_xpath("//span[contains(text(), '%s')]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select Clients module")
        return WorkflowsPage(self.driver)

    def click_add_condition_group(self):
        sleep(3)
        btn_add_condition = self.driver.find_element_by_xpath("//button[contains(text(), 'Add Condition Group')]")
        btn_add_condition.click()
        Logging().reportDebugStep(self, "Click add condition")
        return WorkflowsPage(self.driver)

    def select_accept_promotions(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//div[@class='col-md-5']//div[@class='select-filter']")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/ \
            workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value/ \
            div/div[1]/select-search/div/div[2]/span[1]/input")
        clients.send_keys(name)
        sleep(2)
        select = self.driver.find_element_by_xpath("//span[text()=' %s ']" % name)
        select.click()
        Logging().reportDebugStep(self, "Select Clients Status")
        return WorkflowsPage(self.driver)

    def select_condition(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value/div/div[2]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition: " + name)
        return WorkflowsPage(self.driver)

    def select_status(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH,
                "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value/div/div[3]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select Clients Status: " + name)
        return WorkflowsPage(self.driver)

    def click_add_condition(self):
        sleep(2)
        btn_next = self.driver.find_element_by_xpath("//button[contains(text(), 'Add Condition')]")
        btn_next.click()
        Logging().reportDebugStep(self, "Click Add Condition")
        return WorkflowsPage(self.driver)

    def select_second_accept_promotions(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//field-condition-value[2]//div[@class='select-filter']")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[2]/div/div[1]/select-search/div/div[2]/span[1]/input")
        clients.send_keys(name)
        sleep(3)
        if global_var.current_brand_name == "itrader" or global_var.current_brand_name == "gmo":
            select = self.driver.find_element_by_xpath("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[2]/div/div[1]/select-search/div/div[2]/span[3][contains(text(), '%s')]" % name)
        else:
            select = self.driver.find_element_by_xpath(
                "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[2]/div/div[1]/select-search/div/div[2]/span[2][contains(text(), '%s')]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select " + name)
        return WorkflowsPage(self.driver)

    def select_second_condition(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[2]/div/div[2]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition " + name)
        return WorkflowsPage(self.driver)

    def click_enter_email(self):
        sleep(2)
        btn_next = self.driver.find_element_by_xpath("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[3]/div/div[3]/input")
        btn_next.click()
        Logging().reportDebugStep(self, "Click enter email")
        return WorkflowsPage(self.driver)

    def enter_email(self, email):
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "/html/body/bs-modal[8]/div/div/bs-modal-body/div/value-definition/div/div[2]/textarea")
        clients.send_keys(email)
        Logging().reportDebugStep(self, "Emaer email: " + email)
        return WorkflowsPage(self.driver)

    def click_save_value(self):
        sleep(2)
        btn_next = self.driver.find_element_by_xpath(
            "/html/body/bs-modal[8]/div/div/bs-modal-footer/div/button[1]")
        btn_next.click()
        Logging().reportDebugStep(self, "Click Save")
        return WorkflowsPage(self.driver)

    def select_second_condition_between(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[2]/div/div[4]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition " + name)
        return WorkflowsPage(self.driver)

    def select_condition_between(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[1]/div/div[4]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition " + name)
        return WorkflowsPage(self.driver)

    def select_third_accept_promotions(self, name):
        sleep(2)
        module = self.driver.find_element_by_xpath("//field-condition-value[3]//div[@class='select-filter']")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[3]/div/div[1]/select-search/div/div[2]/span[1]/input")
        clients.send_keys(name)
        sleep(3)
        select = self.driver.find_element_by_xpath(
            "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[3]/div/div[1]/select-search/div/div[2]/span[2][contains(text(), '%s')]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select " + name)
        return WorkflowsPage(self.driver)

    def select_third_conditions(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH,
                                                 "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-conditions/div[3]/groups-conditions/div[1]/div/group-conditions/field-condition-value[3]/div/div[2]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition " + name)
        return WorkflowsPage(self.driver)

    def select_add_task(self, name):
        sleep(2)
        btn_add_task = self.driver.find_element_by_xpath(
            "/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[2]/div/workflow-edit-tasks/div[1]/div/button")
        btn_add_task.click()
        sleep(2)
        select = self.driver.find_element_by_xpath("//li[contains(text(), '%s')]" % name)
        select.click()
        Logging().reportDebugStep(self, "Click Add Task and select: " + name)
        return WorkflowsPage(self.driver)

    def enter_task_title(self, name):
        sleep(2)
        input = self.driver.find_element_by_xpath("/html/body/bs-modal[6]/div/div/bs-modal-body/div/workflow-task/div/div[1]/div[2]/input")
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
        module = self.driver.find_element_by_xpath("/html/body/bs-modal[6]/div/div/bs-modal-body/div/workflow-task/div/div[2]/div[3]/field-value/div/div[1]/select-search/div")
        module.click()
        sleep(2)
        clients = self.driver.find_element_by_xpath(
            "/html/body/bs-modal[6]/div/div/bs-modal-body/div/workflow-task/div/div[2]/div[3]/field-value/div/div[1]/select-search/div/div[2]/span[1]/input")
        clients.send_keys(name)
        sleep(3)
        select = self.driver.find_element_by_xpath(
            "//span[contains(text(), '%s')]" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select " + name)
        return WorkflowsPage(self.driver)

    def click_enter_value(self):
        sleep(2)
        btn = self.driver.find_element_by_xpath("/html/body/bs-modal[6]/div/div/bs-modal-body/div/workflow-task/div/div[2]/div[3]/field-value/div/div[2]/input")
        btn.click()
        Logging().reportDebugStep(self, "Click enter value")
        return WorkflowsPage(self.driver)

    def enter_value(self, name):
        sleep(2)
        textarea = self.driver.find_element_by_xpath("/html/body/bs-modal[8]/div/div/bs-modal-body/div/value-definition/div/div[2]/textarea")
        textarea.send_keys(name)
        Logging().reportDebugStep(self, "Enter value " + name)
        return WorkflowsPage(self.driver)

    def click_save_value_task(self):
        sleep(2)
        btn_save = self.driver.find_element_by_xpath("/html/body/bs-modal[8]/div/div/bs-modal-footer/div/button[1]")
        btn_save.click()
        Logging().reportDebugStep(self, "Click Save")
        return WorkflowsPage(self.driver)

    def select_second_field(self, name):
        sleep(2)
        select = self.driver.find_element_by_xpath("//field-value[2]//div[@class='select-filter']")
        select.click()
        clients = self.driver.find_element_by_xpath(
            "/html/body/bs-modal[6]/div/div/bs-modal-body/div/workflow-task/div/div[2]/div[3]/field-value[2]/div/div[1]/select-search/div/div[2]/span[1]/input")
        clients.send_keys(name)
        sleep(3)
        select = self.driver.find_element_by_xpath(
            "/html/body/bs-modal[6]/div/div/bs-modal-body/div/workflow-task/div/div[2]/div[3]/field-value[2]/div/div[1]/select-search/div/div[2]/span[text() = ' %s ']" % name)
        try:
            select.click()
        except:
            self.driver.execute_script("arguments[0].click();", select)
        Logging().reportDebugStep(self, "Select " + name)
        return WorkflowsPage(self.driver)

    def select_country(self, name):
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH,"/html/body/bs-modal[6]/div/div/bs-modal-body/div/workflow-task/div/div[2]/div[3]/field-value[2]/div/div[2]/select"))
        select.select_by_visible_text(name)
        Logging().reportDebugStep(self, "Select condition " + name)
        return WorkflowsPage(self.driver)

    def click_save_task(self):
        sleep(2)
        btn_save = self.driver.find_element_by_xpath("/html/body/bs-modal[6]/div/div/bs-modal-footer/div/button[1]")
        btn_save.click()
        Logging().reportDebugStep(self, "Click Save task")
        return WorkflowsPage(self.driver)

    def click_save_workflow(self):
        sleep(2)
        btn_save = self.driver.find_element_by_xpath\
            ("/html/body/app-root/configuration/div/div/div[2]/div/div/workflow/div/workflow-edit/div[3]/div/button[3]")
        btn_save.click()
        Logging().reportDebugStep(self, "Click Save workflow")
        return WorkflowsPage(self.driver)
