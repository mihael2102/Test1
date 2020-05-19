from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI


class MassEditPageUI(CRMBasePage):

    def mass_edit(self, field_to_edit1=None, field_to_edit2=None, language=None, field_to_edit3=None, country=None,
                  field_to_edit4=None, assign_to=None, field_to_edit5=None, event_type=None, field_to_edit6=None,
                  priority=None, final_btn=None):
        if field_to_edit1:
            self.select_field_to_edit(field_to_edit1)
            status = self.get_item_from_list_by_number(field_to_edit1, '2')
            self.select_from_list(field_to_edit1, status)
        if field_to_edit2 and language:
            self.select_field_to_edit(field_to_edit2)
            self.set_text_field(field_to_edit2, language)
        if field_to_edit3 and country:
            self.select_field_to_edit(field_to_edit3)
            self.select_from_list(field_to_edit3, country)
        if field_to_edit4 and assign_to:
            self.select_field_to_edit(field_to_edit4)
            self.select_from_list(field_to_edit4, assign_to)
        if field_to_edit5 and event_type:
            self.select_field_to_edit(field_to_edit5)
            self.select_from_list(field_to_edit5, event_type)
        if field_to_edit6 and priority:
            self.select_field_to_edit(field_to_edit6)
            self.select_from_list(field_to_edit6, priority)
        self.click_save_changes_btn(final_btn)
        return MassEditPageUI(self.driver)

    def click_mass_action_btn(self, btn):
        GlobalModulePageUI(self.driver) \
            .click_mass_action_btn(btn)
        return MassEditPageUI(self.driver)

    def select_field_to_edit(self, field):
        sleep(0.1)
        item = super().wait_element_to_be_clickable(
            "//div[h3=' Choose fields to edit: ']//span[contains(text(),'%s')]" % field)
        self.driver.execute_script("arguments[0].click();", item)
        sleep(0.5)
        Logging().reportDebugStep(self, "Select '" + field + "' check box")
        return MassEditPageUI(self.driver)

    def set_text_field(self, field, text):
        GlobalPopupPageUI(self.driver)\
            .set_text_field(field, text)
        return MassEditPageUI(self.driver)

    def select_from_list(self, pick_list, item):
        GlobalPopupPageUI(self.driver)\
            .select_pick_list_item(pick_list, item)
        return MassEditPageUI(self.driver)

    def get_item_from_list_by_number(self, pick_list, number):
        item = GlobalPopupPageUI(self.driver)\
            .get_item_from_list_by_number(pick_list, number)
        MassActionsConstantsUI.STATUS = item
        return item

    def click_save_changes_btn(self, final_btn):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(final_btn)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return MassEditPageUI(self.driver)
