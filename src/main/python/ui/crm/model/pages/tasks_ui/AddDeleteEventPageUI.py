from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


class AddDeleteEventPageUI(CRMBasePage):

    def add_edit_event(self, btn_interaction=None, btn_event=None, row=None, list1=None, e_status=None, list2=None,
                       e_type=None, list3=None, duration=None, day=None, month=None, year=None, list4=None,
                       assign_to=None, attached_to=None, field1=None, subject=None, list5=None, priority=None,
                       comments=None, final_btn=None):
        if btn_interaction:
            self.click_add_interaction_btn(btn_interaction)
        if btn_event:
            self.click_add_event_btn()
        if row:
            self.edit_record(row)
        if list1 and e_status:
            self.select_from_list(list1, e_status)
        if list2 and e_type:
            self.select_from_list(list2, e_type)
        if list3 and duration:
            self.select_from_list(list3, duration)
        if day and month and year:
            self.set_date(day, month, year)
        if list4 and assign_to:
            self.select_from_list(list4, assign_to)
        if attached_to:
            self.set_attached_to(attached_to)
        if field1 and subject:
            self.set_text(field1, subject)
        if list5 and priority:
            self.select_from_list(list5, priority)
        if comments:
            self.set_comments(comments)
        if final_btn:
            self.click_save_btn(final_btn)
        return AddDeleteEventPageUI(self.driver)

    def click_add_interaction_btn(self, act_btn):
        GlobalDetailsPageUI(self.driver) \
            .click_action_bar_btn(act_btn)
        return AddDeleteEventPageUI(self.driver)

    def click_add_event_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Add Event' button")
        add_event_btn = super().wait_element_to_be_clickable("//span[text()=' Add Event ']")
        add_event_btn.click()
        return AddDeleteEventPageUI(self.driver)

    def select_from_list(self, pick_list, item):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item(pick_list, item)
        return AddDeleteEventPageUI(self.driver)

    def set_text(self, field, text):
        GlobalPopupPageUI(self.driver) \
            .set_text_field(field, text)
        return AddDeleteEventPageUI(self.driver)

    def set_date(self, day, month, year):
        GlobalPopupPageUI(self.driver) \
            .set_date(day, month, year)
        return AddDeleteEventPageUI(self.driver)

    def set_comments(self, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set Comments: " + text)
        input_field = super().wait_load_element("//*[@id='comments']")
        input_field.clear()
        input_field.send_keys(text)
        return AddDeleteEventPageUI(self.driver)

    def set_attached_to(self, name):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set Attached To: " + name)
        attached_to_field = super().wait_element_to_be_clickable(
            "//span[text()=' Attached To ']//following-sibling::div/span")
        attached_to_field.click()
        search_field = super().wait_load_element("//span[text()=' Attached To ']//following-sibling::div//input")
        search_field.clear()
        search_field.send_keys(name)
        item = super().wait_load_element("(//li/a/span[contains(text(),'%s')])[1]" % name)
        self.driver.execute_script("arguments[0].click();", item)
        return AddDeleteEventPageUI(self.driver)

    def click_save_btn(self, button):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(button)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return AddDeleteEventPageUI(self.driver)

    def click_cancel_btn(self):
        GlobalPopupPageUI(self.driver) \
            .click_cancel_btn()
        return AddDeleteEventPageUI(self.driver)

    """ Click Edit icon in table by row """
    def edit_record(self, row):
        GlobalModulePageUI(self.driver) \
            .open_actions_list(row) \
            .click_edit_icon_list_view(row)
        return AddDeleteEventPageUI(self.driver)

    """ Click Delete icon in table by row """
    def delete_record(self, row):
        GlobalModulePageUI(self.driver) \
            .open_actions_list(row) \
            .click_delete_icon_list_view(row) \
            .approve_deleting() \
            .verify_success_message() \
            .click_ok()
        return AddDeleteEventPageUI(self.driver)
