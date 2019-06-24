from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from time import sleep
import glob
import os
import csv
from datetime import *
from requests import get
import random
import xlrd
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


class LeadPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_email_popup(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL) \
                                .click_search_button_leads_module()
        lead_email = LeadsModule(self.driver).get_first_lead_email()
        LeadsModule(self.driver).check_email_link_is_clickable()\
                                .click_first_lead_email()
        value = LeadsModule(self.driver).get_lead_email_pop_up()
        lead_email_pop_up = value.replace(',','')
        assert lead_email == lead_email_pop_up
        LeadsModule(self.driver).enter_subject_mail(CRMConstants.SUBJECT_LEAD_MAIL)
        LeadsModule(self.driver).enter_body_mail(CRMConstants.BODY_LEAD_MAIL)
        LeadsModule(self.driver).click_save()
        CRMHomePage(self.driver).click_ok()
        sleep(7)
        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        LeadsModule(self.driver).enter_email(lead_email) \
                                .click_search_button_leads_module()\
                                .open_lead_personal_details()\
                                .open_email_section()
        mail = LeadsModule(self.driver).get_saved_mail_lead(CRMConstants.SUBJECT_LEAD_MAIL)
        assert mail == CRMConstants.SUBJECT_LEAD_MAIL

    def test_edit_lead_pencil_icon(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL)\
                                .click_search_button_leads_module()\
                                .open_first_lead()\
                                .change_personal_info_pencil_icon(CRMConstants.CHANGE_PHONE_LEAD)

        changed_phone = LeadsModule(self.driver).get_mobile_text()
        assert changed_phone == CRMConstants.CHANGE_PHONE_LEAD

    def fill_questioner_new_client(self, client):

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        CRMHomePage(self.driver).open_client_module() \
            .select_filter(self.config.get_value(
            TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(client)

        ClientProfilePage(self.driver).click_fill_questionnaire_btn()
        ClientProfilePage(self.driver).fill_questionnaire(CRMConstants.STATUS,
                                                          CRMConstants.INCOME,
                                                          CRMConstants.ESTIMATE,
                                                          CRMConstants.PURPOSE,
                                                          CRMConstants.ESTIMATE_YEAR,
                                                          CRMConstants.INCOMING_FUNDS,
                                                          CRMConstants.LEVEL_EDUCATION,
                                                          CRMConstants.TIME_INVESTING,
                                                          CRMConstants.LAST_TRADE,
                                                          CRMConstants.LEVEL_EXPERIENCE,
                                                          CRMConstants.VOLUME,
                                                          CRMConstants.LEVERAGE,
                                                          CRMConstants.APPLE,
                                                          CRMConstants.FACEBOOK,
                                                          CRMConstants.INITIAL_DEPOSIT,
                                                          CRMConstants.RESULT_TRADING,
                                                          CRMConstants.INVESTMENT_OBJECTIVES,
                                                          CRMConstants.COUNTRY,
                                                          CRMConstants.TIN)

        ClientProfilePage(self.driver).click_ok()

    def import_leads(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).click_import_leads()
        ##Create new leads for import
        with open('D:/Leads_Import.csv', mode='w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            first_import_lead = str(random.randrange(1, 999))
            second_import_lead = str(random.randrange(1, 999))
            third_import_lead = str(random.randrange(1, 999))

            filewriter.writerow(["Lead No","Language","First Name","Last Name","Lead Status","Country","Email","Phone","Exists","Client Exist","Lead Source","Assigned To","Department of assigned user","Last Comment"])
            filewriter.writerow(["LEA8149237","English","testqaIMPORT","DoeA","R - New","Germany","pandaqa+" + first_import_lead + "@pandats.com","***","1","testqaIWNNKA Doe","Conference","pandaqa pandaqa","Retention",""])
            filewriter.writerow(["LEA8149236","English","testqaIMPORT","DoeA","R - New","Germany","pandaqa+" + second_import_lead + "@pandats.com","***","0","","Conference","pandaqa pandaqa","Retention",""])
            filewriter.writerow(["LEA8149235","English","testqaIMPORT","DoeA","R - New","Germany","pandaqa+" + third_import_lead + "@pandats.com","***","0","","Conference","pandaqa pandaqa","Retention",""])

        LeadsModule(self.driver).click_browse_import_leads()
        LeadsModule(self.driver).click_next_import_leads()
        LeadsModule(self.driver).select_import_source()
        LeadsModule(self.driver).select_import_source_name(CRMConstants.PANDAQA_ASSIGN)
        LeadsModule(self.driver).select_import_status()
        LeadsModule(self.driver).click_next_second_step()
        check_third_step = LeadsModule(self.driver).check_third_step()
        assert check_third_step == CRMConstants.THIRD_STEP_IMPORT_LEADS
        sleep(120)
        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        i = 1
        for i in range(1, 3):
            lead_first_name = LeadsModule(self.driver).get_first_name_lead(i)
            lead_email = LeadsModule(self.driver).get_email_lead(i)
            path_to_latest_file = 'D:/Leads_Import.csv'
            count = 0
            with open(path_to_latest_file) as f_obj:
                reader = csv.reader(f_obj, delimiter=',')
                for line in reader:
                    if lead_first_name and lead_email in line:
                        count = count + 1

            assert count >= 1

    def export_select_records(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL)
        LeadsModule(self.driver).click_search_button_leads_module()
        i = 1
        for i in range(1, 5):
            LeadsModule(self.driver).click_check_box_leads(i)

        LeadsModule(self.driver).click_export_leads()
        LeadsModule(self.driver).click_export_pop_ups()
        i = 1
        for i in range(1, 5):
            lead_first_name = LeadsModule(self.driver).get_first_name_lead(i)
            lead_email = LeadsModule(self.driver).get_email_lead(i)

            sleep(10)
            ip = get('https://api.ipify.org').text
            if ip == '35.158.30.212':
                list_of_files = glob.glob('C:/Users/anna.poimenova/Downloads/*')
            if ip == '35.158.90.50':
                list_of_files = glob.glob('C:/Users/Administrator/Downloads/*')

            latest_file = max(list_of_files, key=os.path.getctime)
            path_to_latest_file = "%s" % latest_file
            count = 0
            with open(path_to_latest_file) as f_obj:
                reader = csv.reader(f_obj, delimiter=',')
                for line in reader:
                    if lead_first_name and lead_email in line:
                        count = count + 1

            assert count >= 1



    def export_full_list(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL)
        LeadsModule(self.driver).click_search_button_leads_module()
        LeadsModule(self.driver).click_check_box_all_leads()
        LeadsModule(self.driver).click_export_leads()
        LeadsModule(self.driver).click_export_pop_ups()
        i = 1
        for i in range(1, 20):
            lead_first_name = LeadsModule(self.driver).get_first_name_lead(i)
            lead_email = LeadsModule(self.driver).get_email_lead(i)

            sleep(10)
            ip = get('https://api.ipify.org').text
            if ip == '35.158.30.212':
                list_of_files = glob.glob('C:/Users/anna.poimenova/Downloads/*')
            if ip == '35.158.90.50':
                list_of_files = glob.glob('C:/Users/Administrator/Downloads/*')

            latest_file = max(list_of_files, key=os.path.getctime)
            path_to_latest_file = "%s" % latest_file
            count = 0
            with open(path_to_latest_file) as f_obj:
                reader = csv.reader(f_obj, delimiter=',')
                for line in reader:
                    if lead_first_name and lead_email in line:
                        count = count + 1

            assert count >= 1


    def mass_edit_leads(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL)
        LeadsModule(self.driver).click_search_button_leads_module()
        sleep(40)
        LeadsModule(self.driver).click_check_box_all_leads()
        LeadsModule(self.driver).mass_edit_leads()
        if global_var.current_brand_name == "itrader" or global_var.current_brand_name == "otcapital" or global_var.current_brand_name == "gmo" or global_var.current_brand_name == "rimarkets" or global_var.current_brand_name == "itrader_global" or global_var.current_brand_name == "fm-fx":
            LeadsModule(self.driver).edit_status(CRMConstants.STATUS_EDIT_ITRADER)
        elif global_var.current_brand_name == "stoxmarket":
            LeadsModule(self.driver).edit_status(CRMConstants.STATUS_EDIT_STOX)
        else:
             LeadsModule(self.driver).edit_status(CRMConstants.STATUS_EDIT)
        LeadsModule(self.driver).edit_source(CRMConstants.SOURCE_EDIT)
        LeadsModule(self.driver).edit_country(CRMConstants.COUNTRY_EDIT)
        LeadsModule(self.driver).click_save_mass_edit()
        sleep(40)
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL)
        LeadsModule(self.driver).click_search_button_leads_module()
        i = 1
        for i in range(1, 3):
            status = LeadsModule(self.driver).check_status_leads(i)
            if global_var.current_brand_name == "itrader" or global_var.current_brand_name == "otcapital" or global_var.current_brand_name == "gmo" or global_var.current_brand_name == "rimarkets" or global_var.current_brand_name == "itrader_global" or global_var.current_brand_name == "fm-fx":
                assert status == CRMConstants.STATUS_EDIT_ITRADER
            elif global_var.current_brand_name == "stoxmarket":
                assert status == CRMConstants.STATUS_EDIT_STOX
            else:
                assert status == CRMConstants.STATUS_EDIT
            country = LeadsModule(self.driver).check_country_leads(i)
            assert country == CRMConstants.COUNTRY_EDIT
            # source = LeadsModule(self.driver).check_source_leads(i)
            # assert source == CRMConstants.SOURCE_EDIT


    def mass_assign_leads(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL)
        LeadsModule(self.driver).click_search_button_leads_module()
        LeadsModule(self.driver).click_check_box_all_leads()
        LeadsModule(self.driver).click_mass_assign()
        if global_var.current_brand_name == "capitalmarketsbanc":
            LeadsModule(self.driver).input_mass_assign(CRMConstants.PANDAQA_ASSIGN)
        else:
            LeadsModule(self.driver).input_mass_assign(CRMConstants.PANDAQA_ASSIGN)
        LeadsModule(self.driver).select_user_assign()
        LeadsModule(self.driver).click_status()

        if global_var.current_brand_name == "otcapital" or global_var.current_brand_name == "gmo" or \
                global_var.current_brand_name == "itrader" or global_var.current_brand_name == "itrader_global" or \
                global_var.current_brand_name == "rimarkets" or global_var.current_brand_name == "fm-fx":
            LeadsModule(self.driver).select_status(CRMConstants.STATUS_EDIT_ITRADER)
        elif global_var.current_brand_name == "fxpmarkets" or global_var.current_brand_name == "stoxmarket" or \
                global_var.current_brand_name == "forex_staging":
            LeadsModule(self.driver).select_status(CRMConstants.STATUS_EDIT_STOX)
        else:
            LeadsModule(self.driver).select_status(CRMConstants.STATUS_ASSIGN)
        LeadsModule(self.driver).click_assign()
        LeadsModule(self.driver).mass_assign_result()
        i = 1
        for i in range(1,3):
            status = LeadsModule(self.driver).check_status_leads(i)
            if global_var.current_brand_name == "otcapital" or global_var.current_brand_name == "gmo" or global_var.current_brand_name == "itrader" or global_var.current_brand_name == "itrader_global" or global_var.current_brand_name == "rimarkets" or global_var.current_brand_name == "fm-fx":
                assert status == CRMConstants.STATUS_EDIT_ITRADER
            elif global_var.current_brand_name == "fxpmarkets" or global_var.current_brand_name == "stoxmarket" or \
                    global_var.current_brand_name == "forex_staging":
                assert status == CRMConstants.STATUS_EDIT_STOX
            else:
                assert status == CRMConstants.STATUS_ASSIGN
            assign_leads = LeadsModule(self.driver).check_assign_leads(i)
            if global_var.current_brand_name == "capitalmarketsbanc":
                assert assign_leads == CRMConstants.PANDAQA_ASSIGN
            elif global_var.current_brand_name == "brokerxp":
                return self
            else:
                assert assign_leads == CRMConstants.PANDAQA_ASSIGN



    def sorting_leads(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module()
        LeadsModule(self.driver).select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
        sleep(10)
        LeadsModule(self.driver).enter_email(CRMConstants.SHORT_EMAIL)
        sleep(5)
        LeadsModule(self.driver).click_search_button_leads_module()
        sleep(15)
        LeadsModule(self.driver).sorting_lead_by_leads_no()
        lead_no = LeadsModule(self.driver).check_first_line_leads_no()
        LeadsModule(self.driver).sorting_lead_by_email()
        email = LeadsModule(self.driver).check_first_line_email()
        LeadsModule(self.driver).sorting_lead_by_exist()
        exist = LeadsModule(self.driver).check_first_line_exist()

        assert lead_no <= CRMConstants.SORTING_LEAD_NO
        assert email < CRMConstants.SORTING_EMAIL
        try:
            assert exist == CRMConstants.SORTING_EXIST_NO
        except:
            assert exist == CRMConstants.SORTING_EXIST_YES

    def create_lead(self, lead):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_lead_module() \
                                .open_create_lead_module()\


        if global_var.current_brand_name == "safemarkets" or global_var.current_brand_name == "itrader_global" or \
                global_var.current_brand_name == "itrader" or global_var.current_brand_name == "gmo" or \
                global_var.current_brand_name == "fm-fx" or global_var.current_brand_name == "forex_staging":
            CreateLeadsProfilePage(self.driver).perform_create_lead(
            lead[LeadsModuleConstants.FIRST_NAME],
            lead[LeadsModuleConstants.FIRST_LAST_NAME],
            lead[LeadsModuleConstants.FIRST_MOBILE],
            lead[LeadsModuleConstants.FAX],
            lead[LeadsModuleConstants.EMAIL],
            lead[LeadsModuleConstants.SECONDARY_EMAIL],
            lead[LeadsModuleConstants.FIRST_LANGUAGE],
            lead[LeadsModuleConstants.PANDA_PARTNER],
            lead[LeadsModuleConstants.FIRST_REFERRAL],
            lead[LeadsModuleConstants.STREET],
            lead[LeadsModuleConstants.POSTAL_CODE],
            lead[LeadsModuleConstants.FIRST_COUNTRY],
            lead[LeadsModuleConstants.FIRST_DESCRIPTION],
            lead[LeadsModuleConstants.PHONE],
            lead[LeadsModuleConstants.FIRST_TITTLE],
            lead[LeadsModuleConstants.FIRST_LEAD_SOURCE],
            lead[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW],
            lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
            lead[LeadsModuleConstants.FIRST_SOURCE_NAME],
            lead[LeadsModuleConstants.BRAND],
            lead[LeadsModuleConstants.PO_BOX],
            lead[LeadsModuleConstants.CITY],
            lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

        elif global_var.current_brand_name == "fxpmarkets":
            CreateLeadsProfilePage(self.driver).perform_create_lead(
                lead[LeadsModuleConstants.FIRST_NAME],
                lead[LeadsModuleConstants.FIRST_LAST_NAME],
                lead[LeadsModuleConstants.FIRST_MOBILE],
                lead[LeadsModuleConstants.FAX],
                lead[LeadsModuleConstants.EMAIL],
                lead[LeadsModuleConstants.SECONDARY_EMAIL],
                lead[LeadsModuleConstants.FIRST_LANGUAGE],
                lead[LeadsModuleConstants.PANDA_PARTNER],
                lead[LeadsModuleConstants.FIRST_REFERRAL],
                lead[LeadsModuleConstants.STREET],
                lead[LeadsModuleConstants.POSTAL_CODE],
                lead[LeadsModuleConstants.FIRST_COUNTRY],
                lead[LeadsModuleConstants.FIRST_DESCRIPTION],
                lead[LeadsModuleConstants.PHONE],
                lead[LeadsModuleConstants.FIRST_TITTLE],
                lead[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                lead[LeadsModuleConstants.FIRST_LEAD_STATUS_C_NEW],
                lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                lead[LeadsModuleConstants.FIRST_SOURCE_NAME],
                lead[LeadsModuleConstants.BRAND],
                lead[LeadsModuleConstants.PO_BOX],
                lead[LeadsModuleConstants.CITY],
                lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

        elif (global_var.current_brand_name == "ogtrade"):
            CreateLeadsProfilePage(self.driver).perform_create_lead_ogtrade(
                lead[LeadsModuleConstants.FIRST_NAME],
                lead[LeadsModuleConstants.FIRST_LAST_NAME],
                lead[LeadsModuleConstants.FIRST_MOBILE],
                lead[LeadsModuleConstants.FAX],
                lead[LeadsModuleConstants.EMAIL],
                lead[LeadsModuleConstants.SECONDARY_EMAIL],
                lead[LeadsModuleConstants.STREET],
                lead[LeadsModuleConstants.POSTAL_CODE],
                lead[LeadsModuleConstants.FIRST_DESCRIPTION],
                lead[LeadsModuleConstants.PHONE],
                lead[LeadsModuleConstants.FIRST_TITTLE],
                lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                lead[LeadsModuleConstants.PO_BOX],
                lead[LeadsModuleConstants.CITY],
                lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

        else:

            CreateLeadsProfilePage(self.driver).perform_create_lead(
            lead[LeadsModuleConstants.FIRST_NAME],
            lead[LeadsModuleConstants.FIRST_LAST_NAME],
            lead[LeadsModuleConstants.FIRST_MOBILE],
            lead[LeadsModuleConstants.FAX],
            lead[LeadsModuleConstants.EMAIL],
            lead[LeadsModuleConstants.SECONDARY_EMAIL],
            lead[LeadsModuleConstants.FIRST_LANGUAGE],
            lead[LeadsModuleConstants.PANDA_PARTNER],
            lead[LeadsModuleConstants.FIRST_REFERRAL],
            lead[LeadsModuleConstants.STREET],
            lead[LeadsModuleConstants.POSTAL_CODE],
            lead[LeadsModuleConstants.FIRST_COUNTRY],
            lead[LeadsModuleConstants.FIRST_DESCRIPTION],
            lead[LeadsModuleConstants.PHONE],
            lead[LeadsModuleConstants.FIRST_TITTLE],
            lead[LeadsModuleConstants.FIRST_LEAD_SOURCE],
            lead[LeadsModuleConstants.FIRST_LEAD_STATUS],
            lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
            lead[LeadsModuleConstants.FIRST_SOURCE_NAME],
            lead[LeadsModuleConstants.BRAND],
            lead[LeadsModuleConstants.PO_BOX],
            lead[LeadsModuleConstants.CITY],
            lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

    def create_three_leads(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        home_page = CRMHomePage()
        home_page.open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FAX),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.STREET),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_DESCRIPTION),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PHONE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_SOURCE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_STATUS),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_ASSIGNED_TO),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_SOURCE_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.BRAND),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.CITY),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        home_page.refresh_page() \
            .open_client_module()

        CRMHomePage().open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.SECOND_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FAX),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.STREET),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_DESCRIPTION),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PHONE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_SOURCE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_STATUS),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_ASSIGNED_TO),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_SOURCE_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.BRAND),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.CITY),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        home_page.refresh_page() \
            .open_client_module()

        CRMHomePage().open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.THIRD_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FAX),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.STREET),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_DESCRIPTION),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PHONE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_SOURCE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_STATUS),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_ASSIGNED_TO),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_SOURCE_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.BRAND),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.CITY),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        return LeadPrecondition(self.driver, self.config)

    def edit_lead_profile(self, new_lead_data):

        if global_var.current_brand_name == "safemarkets":
            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.FIRST_LANGUAGE],
                new_lead_data[LeadsModuleConstants.PANDA_PARTNER],
                new_lead_data[LeadsModuleConstants.FIRST_REFERRAL],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_COUNTRY],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME],
                new_lead_data[LeadsModuleConstants.BRAND],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])

        elif global_var.current_brand_name == "ogtrade":
            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead_ogtrade(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])

        elif (global_var.current_brand_name == "gmo-dev")\
                 or (global_var.current_brand_name == "urf"):

            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead_without_reff(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.FIRST_LANGUAGE],
                new_lead_data[LeadsModuleConstants.PANDA_PARTNER],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_COUNTRY],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME],
                new_lead_data[LeadsModuleConstants.BRAND],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])

        elif (global_var.current_brand_name == "rimarkets") or (global_var.current_brand_name == "oinvestsa") or \
                (global_var.current_brand_name == "gmo") or (global_var.current_brand_name == "otcapital") or \
                (global_var.current_brand_name == "fm-fx"):

            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead_without_reff(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.FIRST_LANGUAGE],
                new_lead_data[LeadsModuleConstants.PANDA_PARTNER],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_COUNTRY],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_TEST],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME],
                new_lead_data[LeadsModuleConstants.BRAND],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])

        elif (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "itrader_global"):

            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead_without_reff_and_sourse(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.FIRST_LANGUAGE],
                new_lead_data[LeadsModuleConstants.PANDA_PARTNER],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_COUNTRY],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NO_INTRS],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME],
                new_lead_data[LeadsModuleConstants.BRAND],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])
        else:
            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.FIRST_LANGUAGE],
                new_lead_data[LeadsModuleConstants.PANDA_PARTNER],
                new_lead_data[LeadsModuleConstants.FIRST_REFERRAL],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_COUNTRY],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME],
                new_lead_data[LeadsModuleConstants.BRAND],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])

        return LeadPrecondition(self.driver, self.config)
