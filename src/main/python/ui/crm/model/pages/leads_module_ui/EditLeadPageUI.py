from src.main.python.ui.crm.model.constants_ui.leads_ui.EditLeadConstantsUI import EditLeadConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class EditLeadPageUI(CRMBasePage):

    def edit_lead(self, field1=None, fname=None, field2=None, lname=None, field3=None, mobile=None, field4=None,
                  phone=None, field5=None, email=None, field6=None, s_mail=None, field7=None, title=None, list1=None,
                  l_source=None, list2=None, l_status=None, list3=None, assigned_to=None, field8=None, language=None,
                  field9=None, source_name=None, field10=None, fax=None, field11=None, referral=None, field12=None,
                  address=None, field13=None, p_code=None, field14=None, city=None, list4=None, country=None,
                  field15=None, state=None, field16=None, po_box=None, field17=None, description=None, final_btn=None):
        self.click_edit_lead_btn()
        if field1 and fname:
            self.set_text(field1, fname)
        if field2 and lname:
            self.set_text(field2, lname)
        if field3 and mobile:
            self.set_text(field3, mobile)
        if field4 and phone:
            self.set_text(field4, phone)
        if field5 and email:
            self.set_text(field5, email)
        if field6 and s_mail:
            self.set_text(field6, s_mail)
        if field7 and title:
            self.set_text(field7, title)
        if list1 and l_source:
            self.select_from_list(list1, l_source)
        if list2 and l_status:
            self.get_item_from_list_by_number(list2, l_status)
            self.select_pick_list_item_by_number(list2, l_status)
        if list3 and assigned_to:
            self.select_from_list(list3, assigned_to)
        if field8 and language:
            self.set_text(field8, language)
        if field9 and source_name:
            self.set_text(field9, source_name)
        if field10 and fax:
            self.set_text(field10, fax)
        if field11 and referral:
            self.set_text(field11, referral)
        if field12 and address:
            self.set_text(field12, address)
        if field13 and p_code:
            self.set_text(field13, p_code)
        if field14 and city:
            self.set_text(field14, city)
        if list4 and country:
            self.select_from_list(list4, country)
        if field15 and state:
            self.set_text(field15, state)
        if field16 and po_box:
            self.set_text(field16, po_box)
        if field17 and description:
            self.set_text(field17, description)
        self.click_update_lead_btn(final_btn)
        return EditLeadPageUI(self.driver)

    def click_edit_lead_btn(self):
        sleep(0.1)
        GlobalDetailsPageUI(self.driver)\
            .click_edit_btn()
        Logging().reportDebugStep(self, "'Edit Lead' button was clicked")
        return EditLeadPageUI(self.driver)

    def select_from_list(self, pick_list, item):
        GlobalPopupPageUI(self.driver)\
            .select_pick_list_item(pick_list, item)
        return EditLeadPageUI(self.driver)

    def select_pick_list_item_by_number(self, pick_list, number):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item_by_number(pick_list, number)
        return EditLeadPageUI(self.driver)

    def get_item_from_list_by_number(self, pick_list, number):
        item = GlobalPopupPageUI(self.driver) \
            .get_item_from_list_by_number(pick_list, number)
        EditLeadConstantsUI.STATUS = item
        return item

    def set_text(self, field, text):
        GlobalPopupPageUI(self.driver)\
            .set_text_field(field, text)
        return EditLeadPageUI(self.driver)

    def is_button_update_lead_active(self):
        sleep(0.1)
        flag = super().wait_element_to_be_clickable("//button[span=' Update lead ']").get_property("disabled")
        return not flag

    def click_update_lead_btn(self, final_btn):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(final_btn)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return EditLeadPageUI(self.driver)
