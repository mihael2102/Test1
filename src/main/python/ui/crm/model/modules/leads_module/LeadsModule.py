from time import sleep
from datetime import *
#import allure
#from allure_commons.types import AttachmentType
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.modules.leads_module.MassAssignLeadModule import MassAssignLeadModule
from src.main.python.ui.crm.model.modules.leads_module.MassEditLeadModule import MassEditLeadModule
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.ui.crm.model.pages.leads.ImportLeadPage import ImportLeadPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.waitting_utils.WaitingUtils import WaitingUtils
import autoit
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeadsModule(CRMBasePage):

    def get_saved_mail_lead(self, mail):
        sleep(4)
        mail_lead = self.driver.find_element(By.XPATH,
                                                 "//*[@id='rld_table_content']//a[contains(text(), '%s')]" % mail)
        Logging().reportDebugStep(self, "Open lead email section")
        return mail_lead.text

    def open_email_section(self):
        email_section = self.driver.find_element(By.XPATH, "//a[@id='show_Leads_Emails']/span[@class='glyphicons collapse']")
        try:
            email_section.click()
        except:
            self.driver.execute_script("arguments[0].click();", email_section)
        Logging().reportDebugStep(self, "Open lead email section")
        return LeadsModule(self.driver)

    def open_lead_personal_details(self):
        sleep(10)
        lead = self.driver.find_element(By.XPATH, "//a[contains(text(), 'LEA')]")
        try:
            lead.click()
        except:
            self.driver.execute_script("arguments[0].click();", lead)
        Logging().reportDebugStep(self, "Open lead personal details")
        return LeadsModule(self.driver)


    def click_save(self):
        sleep(4)
        self.driver.switch_to.default_content()
        click_save = self.driver.find_element(By.XPATH, "//div[@class='modal-footer new-modal-footer']/input[3]")
        try:
            click_save.click()
        except:
            self.driver.execute_script("arguments[0].click();", click_save)
        Logging().reportDebugStep(self, "Click save")
        return LeadsModule(self.driver)

    def enter_body_mail(self, body):
        sleep(4)
        self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//*[@id='cke_1_contents']/iframe"))
        enter_body_mail = self.driver.find_element(By.XPATH, "/html/body/p")
        self.driver.execute_script("arguments[0].textContent = arguments[1];", enter_body_mail, body)
        # enter_body_mail.send_keys(body)
        Logging().reportDebugStep(self, "Enter body mail")
        return LeadsModule(self.driver)

    def enter_subject_mail(self, subject):
        sleep(4)
        enter_subject_mail = self.driver.find_element(By.XPATH, "//*[@id='subject']")
        enter_subject_mail.send_keys(subject)
        Logging().reportDebugStep(self, "Enter subject mail")
        return LeadsModule(self.driver)

    def get_lead_email_pop_up(self):
        sleep(7)
        first_lead_email = self.driver.find_element(By.XPATH, "//input[@id='parent_name']").get_attribute("value")
        Logging().reportDebugStep(self, "Get lead email pop up")
        return first_lead_email


    def check_third_step(self):
        sleep(4)
        check_third_step = self.driver.find_element(By.XPATH, "//div[@class='steps']/h1").text
        Logging().reportDebugStep(self, "Click NEXT import leads")
        return check_third_step

    def click_next_second_step(self):
        sleep(4)
        click_import_leads = self.driver.find_element(By.XPATH, "//*[@id='importAdvanced']/div[2]/input[1]")
        click_import_leads.click()
        Logging().reportDebugStep(self, "Click NEXT import leads")
        return LeadsModule(self.driver)

    def select_import_status(self):
        sleep(4)
        status = self.driver.find_element(By.XPATH, "//*[@id='default_values']/div[3]/div[2]/button")
        try:
            status.click()
        except:
            self.driver.execute_script("arguments[0].click();", status)
        if global_var.current_brand_name == "tradospot":
            status_leads = self.driver.find_element(By.XPATH, "//*[@id='default_values']/div[3]/div[2]/div/ul/li[3]/a")
        else:
            status_leads = self.driver.find_element(By.XPATH, "//*[@id='default_values']/div[3]/div[2]/div/ul/li[6]/a")
        try:
            status_leads.click()
        except:
            self.driver.execute_script("arguments[0].click();", status_leads)
        Logging().reportDebugStep(self, "Select status leads")
        return LeadsModule(self.driver)

    def select_import_source_name(self, name):
        sleep(4)
        click_import_leads = self.driver.find_element(By.XPATH, "//input[@id='source_name']")
        click_import_leads.send_keys(name)
        Logging().reportDebugStep(self, "Enter source name")
        return LeadsModule(self.driver)

    def select_import_source(self):
        sleep(4)
        source = self.driver.find_element(By.XPATH, "//*[@id='default_values']/div[1]/div[2]/button")
        try:
            source.click()
        except:
            self.driver.execute_script("arguments[0].click();", source)
        source_leads = self.driver.find_element(By.XPATH, "//*[@id='default_values']/div[1]/div[2]/div/ul/li[7]/a/span")
        try:
            source_leads.click()
        except:
            self.driver.execute_script("arguments[0].click();", source_leads)
        Logging().reportDebugStep(self, "Select source leads")
        return LeadsModule(self.driver)

    def click_next_import_leads(self):
        sleep(4)
        click_import_leads = self.driver.find_element(By.XPATH, "//input[@value='Next Step']")
        click_import_leads.click()
        Logging().reportDebugStep(self, "Click NEXT import leads")
        return LeadsModule(self.driver)

    def click_browse_import_leads(self):
        sleep(5)
        browse_documents = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Browse')]")
        browse_documents.click()
        autoit.win_wait_active("Open")
        autoit.send("Leads_Import.csv")
        autoit.send("{ENTER}")
        Logging().reportDebugStep(self, "Click on button Choose File")
        return LeadsModule(self.driver)

    def click_import_leads(self):
        sleep(4)
        click_import_leads = self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/div/button[5]")
        click_import_leads.click()
        Logging().reportDebugStep(self, "Click import leads")
        return LeadsModule(self.driver)

    def click_check_box_leads(self, i):
        sleep(4)
        check_box = self.driver.find_element(By.XPATH, "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[1]/input")
        self.driver.execute_script("arguments[0].scrollIntoView();", check_box)
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        if i == 4:
            Logging().reportDebugStep(self, "Click check box leads")
        return LeadsModule(self.driver)

    def get_email_lead(self, i):
        sleep(4)
        email_lead = super().wait_element_to_be_clickable("//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[8]").text
        if i == 29:
            Logging().reportDebugStep(self, "Verify email leads")
        return email_lead

    def get_lead_fname(self):
        lead_fname = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='mouseArea_First Name']")))
        Logging().reportDebugStep(self, "Verified the lead first name: " + lead_fname.text)
        return lead_fname.text

    def get_lead_lname(self):
        lead_lname = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='mouseArea_Last Name']")))
        Logging().reportDebugStep(self, "Verified the lead last name: " + lead_lname.text)
        return lead_lname.text

    def get_first_name_lead(self, i):
        first_name_lead = super().wait_element_to_be_clickable("//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[4]").text
        if i == 29:
            Logging().reportDebugStep(self, "Verify first name leads")
        return first_name_lead

    def get_lead_email(self):
        lead_email = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='mouseArea_Email']")))
        Logging().reportDebugStep(self, "Verified the lead email: " + lead_email.text)
        return lead_email.text

    def click_export_pop_ups(self):
        sleep(4)
        click_export_leads = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Export Leads')]")
        click_export_leads.click()
        sleep(10)
        click_close = self.driver.find_element(By.XPATH, "//button[@class = 'close new-close']")
        click_close.click()
        Logging().reportDebugStep(self, "Click 'Export Leads' in pop ups")
        return LeadsModule(self.driver)

    def click_export_leads(self):
        sleep(4)
        click_export_leads = self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/div/button[6]")
        self.driver.execute_script("arguments[0].scrollIntoView();", click_export_leads)
        try:
            click_export_leads.click()
        except:
            self.driver.execute_script("arguments[0].click();", click_export_leads)
        Logging().reportDebugStep(self, "Click 'Export Leads'")
        return LeadsModule(self.driver)

    def click_save_mass_edit(self):
        sleep(4)
        click_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='massassignform_action_button']")
        click_mass_assign.click()
        sleep(1)
        self.wait_loading_to_finish(200)
        sleep(1)
        Logging().reportDebugStep(self, "Click 'Save'")
        return LeadsModule(self.driver)

    def edit_country(self, country):
        sleep(4)
        click_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='country_mass_edit_check']/div[1]/div")
        click_mass_assign.click()
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='country']"))
        select.select_by_visible_text(country)
        Logging().reportDebugStep(self, "Click 'country' check box and select country")
        return LeadsModule(self.driver)

    def edit_source(self, source):
        sleep(4)
        click_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='leadsource_mass_edit_check']/div[1]/div")
        click_mass_assign.click()
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='leadsource']"))
        select.select_by_visible_text(source)
        Logging().reportDebugStep(self, "Click 'source' check box and select source")
        return LeadsModule(self.driver)

    def edit_status(self, status):
        sleep(4)
        edit_status = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["edit_status"])
        edit_status.click()
        sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='leadstatus']"))
        select.select_by_visible_text(status)
        Logging().reportDebugStep(self, "Click 'Status' check box and select status")
        return LeadsModule(self.driver)

    def mass_edit_leads(self):
        sleep(5)
        mass_edit_leads = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["mass_edit_leads"])
        try:
            mass_edit_leads.click()
        except:
            self.driver.execute_script("arguments[0].click();", mass_edit_leads)
        if global_var.current_brand_name == "itrader" or global_var.current_brand_name == "stoxmarket":
            mass_edit_leads.click()
        Logging().reportDebugStep(self, "Click Mass Edit Leads")
        sleep(20)
        return LeadsModule(self.driver)

    def check_assign_leads(self, i):
        if global_var.current_brand_name == "swiftcfd" or global_var.current_brand_name == "royal_cfds" or global_var.current_brand_name == "brokerz" or global_var.current_brand_name == "ptbanc" or global_var.current_brand_name == "aztrades" or global_var.current_brand_name == "tradospot" or global_var.current_brand_name == "24btcmarket" or global_var.current_brand_name == "newforexstage2":
            assign_leads = self.driver.find_element(By.XPATH, "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[13]").text
        else:
            assign_leads = self.driver.find_element(By.XPATH,
                                                    "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[14]").text
        if i == 10:
            Logging().reportDebugStep(self, "Verify assign")
        return assign_leads

    def check_status_leads(self, i):
        sleep(4)
        if global_var.current_brand_name == "swiftcfd" or global_var.current_brand_name == "royal_cfds" or global_var.current_brand_name == "brokerz" or global_var.current_brand_name == "ptbanc" or global_var.current_brand_name == "aztrades" or global_var.current_brand_name == "tradospot" or global_var.current_brand_name == "24btcmarket" or global_var.current_brand_name == "newforexstage2":
            status = self.driver.find_element(By.XPATH, "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[6]").text
        else:
            status = self.driver.find_element(By.XPATH, "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[7]").text
        if i == 10:
            Logging().reportDebugStep(self, "Verify status")
        return status

    def check_country_leads(self, i):
        sleep(4)
        if global_var.current_brand_name == "swiftcfd" or global_var.current_brand_name == "royal_cfds" or global_var.current_brand_name == "brokerz" or global_var.current_brand_name == "ptbanc" or global_var.current_brand_name == "aztrades" or global_var.current_brand_name == "tradospot" or global_var.current_brand_name == "24btcmarket" or global_var.current_brand_name == "newforexstage2":
            country = self.driver.find_element(By.XPATH, "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[7]").text
        else:
            country = self.driver.find_element(By.XPATH, "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[8]").text
        if i == 19:
            Logging().reportDebugStep(self, "Verify country")
        return country

    def check_source_leads(self, i):
        sleep(4)
        source = self.driver.find_element(By.XPATH, "//tbody[@id = 'listBody']/tr[" + str(i) + "]/td[16]").text
        if i == 19:
            Logging().reportDebugStep(self, "Verify source")
        return source

    def select_status(self, select_status):
        sleep(4)
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='leadstatus']"))
        select.select_by_visible_text(select_status)
        Logging().reportDebugStep(self, "The status was selected: " + select_status)
        return LeadsModule(self.driver)

    def click_status(self):
        sleep(4)
        click_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='leadstatus_mass_edit_check']")
        click_mass_assign.click()
        Logging().reportDebugStep(self, "Click check box Status")
        return LeadsModule(self.driver)

    def mass_assign_result(self, user):
        sleep(4)
        mass_assign_result = self.driver.find_element(By.XPATH,
                                                     "//div[contains(text(), 'accounts assigned to %s')]" % user)
        btn_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary'][contains(text(), 'OK')]")
        btn_ok.click()
        Logging().reportDebugStep(self, "Close succsesfull result pop ups")
        return LeadsModule(self.driver)

    def click_assign(self):
        sleep(4)
        click_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='massassignform_action_button']")
        click_mass_assign.click()
        Logging().reportDebugStep(self, "Click assign pop ups")
        return LeadsModule(self.driver)

    def select_user_assign(self, user):
        sleep(4)
        click_mass_assign = self.driver.find_element(By.XPATH, "//div[2][contains (text(), '%s')]" % user)
        click_mass_assign.click()
        Logging().reportDebugStep(self, "Select user")
        return LeadsModule(self.driver)

    def input_mass_assign(self, user):
        sleep(10)
        input_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='searchstring']")
        input_mass_assign.send_keys(user)
        Logging().reportDebugStep(self, "Enter user name")
        return LeadsModule(self.driver)

    def click_mass_assign(self):
        sleep(4)
        if global_var.current_brand_name == "aztrades":
            click_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='list_action_buttons']/input[2]")
        else:
            click_mass_assign = self.driver.find_element(By.XPATH, "//*[@id='list_action_buttons']/input[3]")
        click_mass_assign.click()
        Logging().reportDebugStep(self, "Click mass assign btn")
        return LeadsModule(self.driver)

    def click_check_box_all_leads(self):
        sleep(4)
        click_check_box_all_leads = self.driver.find_element(By.XPATH, "//*[@id='selectCurrentPageRec']")
        try:
            click_check_box_all_leads.click()
        except:
            self.driver.execute_script("arguments[0].click();", click_check_box_all_leads)
        Logging().reportDebugStep(self, "Click check box all leads")
        return LeadsModule(self.driver)

    def check_first_line_exist(self):
        sleep(1)
        check_first_line_exist = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["check_first_line_exist"]).text
        Logging().reportDebugStep(self, "Verify sorting by Exist: " + check_first_line_exist)
        return check_first_line_exist

    def check_first_line_email(self):
        sleep(7)
        check_first_line_email_1 = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["check_first_line_email_1"]).text
        email_1 = check_first_line_email_1.replace('pandaqa+','')
        number_email__str1 = email_1.replace('@pandats.com','')
        number_email_1 = int(number_email__str1)
        check_first_line_email_2 = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["check_first_line_email_2"]).text
        email_2 = check_first_line_email_2.replace('pandaqa+', '')
        number_email_str2 = email_2.replace('@pandats.com', '')
        number_email_2 = int(number_email_str2)
        number_email_diff = number_email_1 - number_email_2
        Logging().reportDebugStep(self, "Verify sorting by Email: " + str(number_email_diff))
        return number_email_diff

    def check_first_line_leads_no(self):
        sleep(2)
        check_first_line_leads_no1 = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["check_first_line_leads_no1"])
        if global_var.current_brand_name != "brokerz":
            self.driver.execute_script("arguments[0].scrollIntoView();", check_first_line_leads_no1)
        check_first_line_leads_no = check_first_line_leads_no1.text
        if global_var.current_brand_name == "stoxmarket":
            number_str_1 = check_first_line_leads_no.replace('LEAD', '')
        else:
            number_str_1 = check_first_line_leads_no.replace('LEA', '')
        number_1 = int(number_str_1)
        check_first_line_leads_no2 = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["check_first_line_leads_no2"]).text
        if global_var.current_brand_name == "stoxmarket":
            number_str_2 = check_first_line_leads_no2.replace('LEAD', '')
        else:
            number_str_2 = check_first_line_leads_no2.replace('LEA', '')
        number_2 = int(number_str_2)
        number_diff = number_1 - number_2
        Logging().reportDebugStep(self, "Verify sorting by Leads no: " + str(number_diff))
        return number_diff

    def sorting_lead_by_leads_no(self):
        sleep(1)
        sorting_lead_by_leads_no = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Lead No')]")
        try:
            sorting_lead_by_leads_no.click()
        except:
            self.driver.execute_script("arguments[0].click();", sorting_lead_by_leads_no)
        self.wait_vtiger_loading_to_finish_custom(55)
        Logging().reportDebugStep(self, "Click sorting by Leads no")
        return LeadsModule(self.driver)

    def sorting_lead_by_email(self):
        sleep(4)
        sorting_lead_by_email = self.driver.find_element(By.XPATH,"//*[@id='listHeaderemail']")
        try:
            sorting_lead_by_email.click()
        except:
            self.driver.execute_script("arguments[0].click();", sorting_lead_by_email)
        self.wait_vtiger_loading_to_finish_custom(55)
        Logging().reportDebugStep(self, "Click sorting by Email")
        return LeadsModule(self.driver)

    def sorting_lead_by_exist(self):
        sleep(4)
        sorting_lead_by_exist = self.driver.find_element(By.XPATH,"//*[@id='listHeaderalreadyexists']")
        try:
            sorting_lead_by_exist.click()
        except:
            self.driver.execute_script("arguments[0].click();", sorting_lead_by_exist)
        self.wait_vtiger_loading_to_finish_custom(55)
        Logging().reportDebugStep(self, "Click sorting by Exist")
        return LeadsModule(self.driver)

    def perform_searching_lead_module(self, first_name, last_name, email, assigned_to, tittle, lead_source, lead_status,
                                         language):
        self.wait_element_to_be_clickable("//td[@class='txt_al_c']")
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        # self.enter_assigned_to(assigned_to)
        # self.enter_tittle(tittle)
        # self.enter_lead_source(lead_source)
        # self.enter_lead_status(lead_status)
        # self.enter_language(language)
        self.click_search_button_leads_module()
        self.wait_crm_loading_to_finish()
        return LeadsModule()

    def perform_searching_lead_by_mail(self, email):
        self.wait_element_to_be_clickable("//td[@class='txt_al_c']")
        self.enter_email(email)
        self.click_search_button_leads_module()
        sleep(4)
        self.wait_crm_loading_to_finish()
        return LeadsModule(self.driver)

    def open_create_lead_module(self):
        task_module = super().wait_load_element("//td[@class='moduleName']//button[1]")
        task_module.click()
        Logging().reportDebugStep(self, "Create leads module is opened")
        return CreateLeadsProfilePage(self.driver)

    def open_create_filter_pop_up(self):
        filter_button = super().wait_element_to_be_clickable("//a[@title='Create Filter']")
        filter_button.click()
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterPage(self.driver)

    def open_import_page(self):
        import_page = super().wait_element_to_be_clickable("//button[@title='Import Leads']")
        import_page.click()
        Logging().reportDebugStep(self, "The import_page was opened")
        return ImportLeadPage(self.driver)

    def open_today_lead_tab(self):
        today_lead_tab = super().wait_element_to_be_clickable("//li[contains(text(),'Today Leads')]")
        today_lead_tab.click()
        Logging().reportDebugStep(self, "The today tab was opened")
        return LeadsModule(self.driver)

    def get_import_lead(self, last_name_lead):
        WaitingUtils().wait_util_element_is_displayed(last_name_lead, self.driver)
        return LeadsModule(self.driver)

    '''
         Returns a confirmation  message if the user entered a valid password
    '''

    def get_confirm_message_lead_module(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns a confirmation message: " + confirm_message.text)
        return confirm_message.text

    def select_three_records_task_module(self):
        sleep(1)
        first_check_box = super().wait_element_to_be_clickable("//tbody[@id='listBody']//tr[1]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[2]//td[1]")
        second_check_box.click()
        third_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[3]//td[1]")
        third_check_box.click()
        Logging().reportDebugStep(self, "The records were selected")
        return LeadsModule(self.driver)

    ''' 
           Select the filter in drop-down   
          :parameter test_filter the filter that is created in the filters drop down
          :return Home Page instance
       '''

    def select_filter(self, test_filter):
        drop_down_filter = super().wait_load_element("//span[@class='filter-option pull-left']")
        drop_down_filter.click()
        Logging().reportDebugStep(self, "Click the  drop down filter ")
        field_found = self.driver.find_element(By.XPATH, "//input[@class='input-block-level form-control']")
        field_found.clear()
        field_found.send_keys(test_filter)
        Logging().reportDebugStep(self, "The field found is : " + test_filter)
        select_test_filter = self.driver.find_element(By.XPATH, "//a/span[contains(., '%s')]" % test_filter)
        select_test_filter.click()
        Logging().reportDebugStep(self, "Click the selected filter")
        self.wait_crm_loading_to_finish()
        return LeadsModule(self.driver)

    def open_mass_edit_task(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass Edit']")
        mass_edit_module.click()
        return MassEditLeadModule(self.driver)

    def open_mass_assign_lead_module(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass assign']")
        mass_edit_module.click()
        return MassAssignLeadModule(self.driver)

    '''
            Returns a task was_updated  message if the user entered a valid password
     '''

    def get_message_lead_module(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns the message task  : " + confirm_message.text)
        return confirm_message.text

    def click_ok(self):
        super().click_ok()
        return LeadsModule(self.driver)

    def perform_screen_shot_lead_module(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/leads_module/leads_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        # allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
        #                             type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return LeadsModule(self.driver)

    def perform_screen_shot_import_lead_module(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/leads_module/leads_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        # allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
        #                             type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed,the grid with leads is empty ")
        return LeadsModule(self.driver)

    def perform_screen_shot_confirm_import_lead_module(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/leads_module/leads_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        # allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
        #                             type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed,the lead is displayed")
        return LeadsModule(self.driver)

    def select_leads(self):
        select_lead_check_box = super().wait_element_to_be_clickable("//td[@class='lvtCol']//input")
        select_lead_check_box.click()
        Logging().reportDebugStep(self, "All imported leads were selected")
        return LeadsModule(self.driver)

    def click_delete_button(self):
        delete_lead_check_box = super().wait_element_to_be_clickable("//input[@value='Delete']")
        delete_lead_check_box.click()
        allert = self.driver.switch_to_alert()
        allert.accept()
        Logging().reportDebugStep(self, "All imported leads were deleted")
        return LeadsModule(self.driver)

    def delete_filter_lead_module(self):
        delete_filter_button = super().wait_element_to_be_clickable("//a[@title='Delete']")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "The delete button was clicked")
        return LeadsModule(self.driver)

    def confirm_delete_lead_module(self):
        delete_filter_button = super().wait_element_to_be_clickable("//button[contains(text(),'OK')]")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "Three lead were deleted")
        return LeadsModule(self.driver)

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_firstname']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "The first name was entered : " + first_name)
        return LeadsModule(self.driver)

    def enter_last_name(self, last_name):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_lastname']")
        first_name_field.clear()
        first_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The last name was entered : " + last_name)
        return LeadsModule(self.driver)

    def enter_email(self, email):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_email']")
        first_name_field.clear()
        first_name_field.send_keys(email)
        Logging().reportDebugStep(self, "The email was entered : " + email)
        return LeadsModule(self.driver)

    def enter_assigned_to(self, assigned_to):
        country_drop_down = self.driver.find_element(By.XPATH,
                                    "//tr[@id='customAdvanceSearch']//td[5]//span[@class='multiselect-selected-text']")

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                            "//tr[@id='customAdvanceSearch']//td[5]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(assigned_to)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % assigned_to)
        country_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The brand  was selected : " + assigned_to)
        return LeadsModule(self.driver)

    def enter_tittle(self, tittle):
        tittle_name_field = self.driver.find_element(By.XPATH,
                                                     "//tr[@name='customAdvanceSearch']//input[@id='tks_designation']")
        tittle_name_field.clear()
        tittle_name_field.send_keys(tittle)
        Logging().reportDebugStep(self, "The assigned_to was entered : " + tittle)
        return LeadsModule(self.driver)

    def enter_lead_source(self, lead_source):
        lead_source_drop_down = self.driver.find_element(By.XPATH,
                                                         "//tr[@id='customAdvanceSearch']//td[7]//span[@class='multiselect-selected-text']")

        lead_source_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[7]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(lead_source)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % lead_source)
        country_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The brand  was selected : " + lead_source)
        return LeadsModule(self.driver)

    def enter_lead_status(self, lead_status):
        lead_source_drop_down = self.driver.find_element(By.XPATH,
                                                         "//tr[@id='customAdvanceSearch']//td[8]//span[@class='multiselect-selected-text']")

        lead_source_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[8]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(lead_status)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % lead_status)
        country_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The lead_status  was selected : " + lead_status)
        return LeadsModule(self.driver)

    def enter_language(self, language):
        first_name_field = self.driver.find_element(By.XPATH,
                                                    "//tr[@name='customAdvanceSearch']//input[@name='tks_cf_1092']")
        first_name_field.clear()
        first_name_field.send_keys(language)
        Logging().reportDebugStep(self, "The language was entered : " + language)
        return LeadsModule(self.driver)


    def get_first_lead_email(self):
        sleep(4)
        first_lead_email = self.driver.find_element(By.XPATH, "(//tr[1]//a//div[contains(text(), 'pandaqa')])[1]")
        Logging().reportDebugStep(self, "Get first lead email")
        return first_lead_email.text


    def click_first_lead_email(self):
        sleep(3)
        first_lead_email = self.driver.find_element(By.XPATH, "(//tr[1]//a//div[contains(text(), 'pandaqa')])[1]")
        sleep(1)
        try:
            first_lead_email.click()
        except:
            self.driver.execute_script("arguments[0].click();", first_lead_email)
        Logging().reportDebugStep(self, "Click first lead email")
        return LeadsModule(self.driver)

    def click_search_button_leads_module(self):
        search_button = self.driver.find_element(By.XPATH, "//td[@class='txt_al_c']")
        self.driver.execute_script("arguments[0].click();", search_button)
        try:
            search_button.click()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView();", search_button)
        self.wait_vtiger_loading_to_finish_custom(55)
        Logging().reportDebugStep(self, "The search button was clicked ")
        return LeadsModule(self.driver)

    def change_personal_info_pencil_icon(self, phone):
        sleep(2)
        edit_personal_details = super().wait_load_element("//*[@id='mouseArea_Mobile']")
        edit_personal_details.click()
        sleep(1)
        pencil = super().wait_load_element("//*[@id='crmspanid']/a/span")
        try:
            pencil.click()
        except:
            self.driver.execute_script("arguments[0].click();", pencil)
        sleep(1)
        input = self.driver.find_element(By.XPATH, "//input[@id= 'txtbox_Mobile']")
        input.clear()
        input.send_keys(phone)
        sleep(1)
        save_personal_details = super().wait_load_element("//*[@id='editarea_Mobile']/div/a[1]/span")
        try:
            save_personal_details.click()
        except:
            self.driver.execute_script("arguments[0].click();", save_personal_details)
        Logging().reportDebugStep(self, "Click phone: " + phone)
        return LeadsModule(self.driver)

    def open_first_lead(self):
        sleep(3)
        first_lead = self.driver.find_element(By.XPATH, "//tr[1]//a[contains(text(), 'LEA')]")
        sleep(1)
        try:
            first_lead.click()
        except:
            self.driver.execute_script("arguments[0].click();", first_lead)
        Logging().reportDebugStep(self, "Click first lead")
        return LeadsModule(self.driver)

    def get_results_count(self):
        refresh_icon = self.driver.find_elements(By.XPATH, "//span[@class='fa fa-refresh']")[0]
        refresh_icon.click()
        result_count_xpath = "//*[contains(text(), 'Showing Records')]"
        self.wait_visible_of_element(result_count_xpath)
        results_count_text = self.driver.find_elements(By.XPATH, result_count_xpath)[0].text
        results_split = results_count_text.split(" ")
        result_count = int(results_split[len(results_split) - 1])
        Logging().reportDebugStep(self, "Record is found")
        return result_count

    def get_first_name_column(self):
        name_first_column = super().wait_element_to_be_clickable(
            "//table[@id='resizeble_cols']//td[2]")
        Logging().reportDebugStep(self, "First column name  : " + name_first_column.text)
        return name_first_column.text

    def get_second_name_column(self):
        name_second_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[3]")
        Logging().reportDebugStep(self, "Second column name: " + name_second_column.text)
        return name_second_column.text

    def get_third_name_column(self):
        name_third_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[4]")
        Logging().reportDebugStep(self, "Third column name: " + name_third_column.text)
        return name_third_column.text

    def get_fourth_name_column(self):
        name_fourth_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[5]")
        Logging().reportDebugStep(self, "Fourth column name : " + name_fourth_column.text)
        return name_fourth_column.text

    def get_fifth_name_column(self):
        name_fifth_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[6]")
        Logging().reportDebugStep(self, "Fifth column name : " + name_fifth_column.text)
        return name_fifth_column.text

    def get_sixth_name_column(self):
        name_sixth_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[7]")
        Logging().reportDebugStep(self, "Sixth column name : " + name_sixth_column.text)
        return name_sixth_column.text

    def get_seventh_name_column(self):
        name_seventh_column = self.driver.find_element(By.XPATH,
                                                       "//table[@id='resizeble_cols']//td[8]")
        Logging().reportDebugStep(self, "Seventh column name : " + name_seventh_column.text)
        return name_seventh_column.text

    def get_eighth_name_column(self):
        name_eighth_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[9]")
        Logging().reportDebugStep(self, "Seventh column name : " + name_eighth_column.text)
        return name_eighth_column.text

    def get_mobile_text(self):
        get_mobile_text = self.driver.find_element(By.XPATH,
                                                      "//*[@id='dtlview_Mobile']")
        Logging().reportDebugStep(self, "Mobile changed : " + get_mobile_text.text)
        return get_mobile_text.text

    def get_lead_assignedto(self):
        lead_assigned = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='dtlview_Assigned To']")))
        Logging().reportDebugStep(self, "Lead assigned to: " + lead_assigned.text)
        return lead_assigned.text

    def open_personal_details_lead(self):
        lead = super().wait_element_to_be_clickable("//a[contains(text(),'LEA')]")
        lead.click()
        Logging().reportDebugStep(self, "Go to personal details lead")
        return LeadsModule(self.driver)