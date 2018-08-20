from time import sleep

from selenium.common.exceptions import StaleElementReferenceException

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.affiliates.CreateAffiliateModule import CreateAffiliateModule
from src.main.python.ui.crm.model.modules.affiliates.EditAffiliateModule import EditAffiliateModule
from src.main.python.ui.crm.model.pages.affiliates.AffiliateDetailsViewPage import AffiliateDetailsViewPage
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.constants.AffiliatePageConstants import AffiliatePageConstants
from src.main.python.utils.config import Config


class AffiliateListViewPage(CRMBasePage):
    def __init__(self):
        super().__init__()

        """Use appropriate dictionary for creating and editing affiliate info and then use these dictionaries in asserts"""
        self.created_client_initial_info = {
            AffiliatePageConstants.PARTNER_NAME: AffiliatePageConstants.PARTNER_NAME,
            AffiliatePageConstants.BRAND_NEW_FOREX: Config.data.get_data_affliate_info(
                AffiliatePageConstants.BRAND_NEW_FOREX),
            AffiliatePageConstants.ALLOWED_IP: Config.data.get_data_affliate_info(
                AffiliatePageConstants.ALLOWED_IP),
            AffiliatePageConstants.IS_ENABLED: Config.data.get_data_affliate_info(
                AffiliatePageConstants.IS_ENABLED),
            AffiliatePageConstants.FIRST_ALLOWED_METHOD: Config.data.get_data_affliate_info(
                AffiliatePageConstants.FIRST_ALLOWED_METHOD),
            AffiliatePageConstants.SECOND_ALLOWED_METHOD: Config.data.get_data_affliate_info(
                AffiliatePageConstants.SECOND_ALLOWED_METHOD),
            AffiliatePageConstants.THIRD_ALLOWED_METHOD: Config.data.get_data_affliate_info(
                AffiliatePageConstants.THIRD_ALLOWED_METHOD),
            AffiliatePageConstants.FOURTH_ALLOWED_METHOD: Config.data.get_data_affliate_info(
                AffiliatePageConstants.FOURTH_ALLOWED_METHOD),
            AffiliatePageConstants.FIFTH_ALLOWED_METHOD: Config.data.get_data_affliate_info(
                AffiliatePageConstants.FIFTH_ALLOWED_METHOD),
            AffiliatePageConstants.FIRST_COUNTRY: Config.data.get_data_affliate_info(
                AffiliatePageConstants.FIRST_COUNTRY),
            AffiliatePageConstants.SECOND_COUNTRY: Config.data.get_data_affliate_info(
                AffiliatePageConstants.SECOND_COUNTRY),
            AffiliatePageConstants.THIRD_COUNTRY: Config.data.get_data_affliate_info(
                AffiliatePageConstants.THIRD_COUNTRY),
            AffiliatePageConstants.FOURTH_COUNTRY: Config.data.get_data_affliate_info(
                AffiliatePageConstants.FOURTH_COUNTRY),
            AffiliatePageConstants.FIFTH_COUNTRY: Config.data.get_data_affliate_info(
                AffiliatePageConstants.FIFTH_COUNTRY)

            }

        self.edited_client_initial_info = {
            AffiliatePageConstants.PARTNER_NAME_EDITED: AffiliatePageConstants.PARTNER_NAME_EDITED,
            AffiliatePageConstants.BRAND_NEW_FOREX: Config.data.get_data_affliate_info_edited(
                AffiliatePageConstants.BRAND_NEW_FOREX),
            AffiliatePageConstants.ALLOWED_IP: Config.data.get_data_affliate_info_edited(
                AffiliatePageConstants.ALLOWED_IP),
            AffiliatePageConstants.IS_ENABLED: Config.data.get_data_affliate_info_edited(
                AffiliatePageConstants.IS_ENABLED),
            AffiliatePageConstants.EDITED_FIRST_ALLOWED_METHOD: Config.data.get_data_affliate_info_edited(
                AffiliatePageConstants.EDITED_FIRST_ALLOWED_METHOD),
            AffiliatePageConstants.EDITED_FIRST_ALLOWED_METHOD_NAME: Config.data.get_data_affliate_info_edited(
                AffiliatePageConstants.EDITED_FIRST_ALLOWED_METHOD_NAME),
            AffiliatePageConstants.EDITED_COUNTRY_1: Config.data.get_data_affliate_info_edited(
                AffiliatePageConstants.EDITED_COUNTRY_1)}

    def open_create_affiliate_popup(self):
        """
        Open create new affiliate popup
        :return: AffiliateModule()
        """
        add_new_affiliate_button = super().wait_element_to_be_clickable(
            "//button[contains(text(), 'Add new affiliate')]")
        add_new_affiliate_button.click()
        Logging().reportDebugStep(self, "Open 'Add new affiliate' popup")
        return CreateAffiliateModule()

    def open_edit_affiliate_popup(self, partner_name):
        """Open 'Edit' popup twice to avoid bug with allowed methods which are not displayed. After fixing remove first opening step"""

        """Find created client by name and then editing him"""
        self.perform_search_by_partner_name(partner_name)

        """Open and close popup"""
        edit_affiliate_button = super().wait_element_to_be_clickable("//tr[@class='tableRow']//td[10]")
        edit_affiliate_button.click()

        sleep(1)

        close_edit_affiliate_button = self.driver.find_element(By.XPATH, "(//bs-modal-footer/div/button[2])[1]").click()

        """Open popup second time to see allowed methods"""

        edit_affiliate_button = super().wait_element_to_be_clickable("//tr[@class='tableRow']//td[10]")

        sleep(1)

        edit_affiliate_button.click()

        Logging().reportDebugStep(self, "Open 'Edit affiliate' popup")
        return EditAffiliateModule()

    def open_affiliate_details_page(self, existed_partner_name):
        sleep(1)
        partner_name_from_list = self.driver.find_element(By.XPATH,
                                                          "//grid-cell/div/link-spa/a[contains(., '%s')]" % existed_partner_name)
        partner_name_from_list.click()
        Logging().reportDebugStep(self,
                                  "Open details page of required affiliate -> " + existed_partner_name)
        return AffiliateDetailsViewPage()

    def perform_search_by_partner_name(self, partner_name_text):
        partner_name_input_xpath = "(//*[@id='host-element']/input)[2]"
        partner_name_input = super().wait_visible_of_element(partner_name_input_xpath)

        sleep(1)
        try:
            partner_name_input.clear()
        except StaleElementReferenceException:
            partner_name_input = self.driver.find_element(By.XPATH, partner_name_input_xpath).clear()
        partner_name_input = self.driver.find_element(By.XPATH, partner_name_input_xpath)
        partner_name_input.send_keys(partner_name_text)
        sleep(1)
        Logging().reportDebugStep(self, "Searching by partner name: " + partner_name_text)
        return AffiliateListViewPage()

    def get_partner_id(self):
        partner_id_text = self.driver.find_element(By.XPATH, "//td[2]/grid-cell/div/span[2]").text
        return partner_id_text

    def get_is_enabled(self):
        is_enabled_text = self.driver.find_element(By.XPATH, "//td[5]/grid-cell/div/span[2]").text
        return is_enabled_text

    def get_allowed_ip(self):
        allowed_ip_text = self.driver.find_element(By.XPATH, "//td[6]/grid-cell/div/span[2]").text
        return allowed_ip_text

    def get_blocked_countries(self):
        blocked_countries_text = self.driver.find_element(By.XPATH, "//td[7]/grid-cell/div/span[2]").text
        return blocked_countries_text

    def get_allowed_methods(self):
        allowed_methods_text = self.driver.find_element(By.XPATH, "//td[8]/grid-cell/div/span[2]").text
        return allowed_methods_text

    def get_brand_name(self):
        brand_name_text = self.driver.find_element(By.XPATH, "//td[9]/grid-cell/div/span[2]").text
        return brand_name_text

    def check_blocked_countries(self):
        list_of_counties = []
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.FIRST_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.SECOND_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.THIRD_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.FOURTH_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.FIFTH_COUNTRY))

        """ Get country from affiliate list view page and compare them with initial values from JSON"""
        for i in list_of_counties:
            if i in self.get_blocked_countries():
                continue
            else:
                Logging().reportDebugStep(self, "Selected country '%s' is not in the list" % i)
                return False

        Logging().reportDebugStep(self, "Checked. Countries were created successfully.")
        return True

    def check_editing_of_blocked_countries(self):
        list_of_counties = []
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.FIRST_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.SECOND_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.THIRD_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.FOURTH_COUNTRY))
        list_of_counties.append(Config.data.get_data_affliate_info(AffiliatePageConstants.FIFTH_COUNTRY))

        """Remove country from initial list which was unselected during test"""
        for i in list_of_counties:
            if i == Config.data.get_data_affliate_info_edited(AffiliatePageConstants.EDITED_COUNTRY_1):
                list_of_counties.remove(i)

        """ Get country from affiliate list view page and compare them with edited values (based on JSON - one country was deleted)"""
        for i in list_of_counties:
            if i in self.get_blocked_countries():
                continue
            else:
                Logging().reportDebugStep(self, "Selected country '%s' is not in the list" % i)
                return False
        Logging().reportDebugStep(self, "Checked. Countries were edited successfully.")
        return True

    def check_allowed_methods(self):
        list_of_allowed_methods = []
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.FIRST_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.SECOND_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.THIRD_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.FOURTH_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.FIFTH_ALLOWED_METHOD_NAME))

        """ Get methods from affiliate list view page and compare them with initial values from JSON"""
        for i in list_of_allowed_methods:
            if i in self.get_allowed_methods():
                continue
            else:
                Logging().reportDebugStep(self,
                                          "Selected allowed method '%s' is not in the list. We expect one of following methods %s" % (
                                              i, self.get_allowed_methods()))
                return False
        return True

    def check_editing_of_allowed_methods(self, added_method):
        list_of_allowed_methods = []
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.FIRST_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.SECOND_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.THIRD_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.FOURTH_ALLOWED_METHOD_NAME))
        list_of_allowed_methods.append(
            Config.data.get_data_affliate_info(AffiliatePageConstants.FIFTH_ALLOWED_METHOD_NAME))
        """Add to initial list new method which was added after editing"""
        list_of_allowed_methods.append(added_method)

        """ Get methods from affiliate list view page and compare them with edited values (based on JSON)"""
        for i in list_of_allowed_methods:
            if i in self.get_allowed_methods():
                continue
            else:
                Logging().reportDebugStep(self,
                                          "Selected allowed method '%s' is not in the list. We expect one of following methods %s" % (
                                              i, self.get_allowed_methods()))
                return False

        Logging().reportDebugStep(self, "Checked. Allowed methods were edited successfully.")
        return True

    def edit_affiliate(self, partner_name):
        """Open popup with initial name from 'create affil' dictionary, but then change it to name from 'edit affil' dictionary"""
        return self.open_edit_affiliate_popup(self.created_client_initial_info[partner_name]).perform_edit_affiliate(
            self.edited_client_initial_info[AffiliatePageConstants.PARTNER_NAME_EDITED],
            self.edited_client_initial_info[AffiliatePageConstants.BRAND_NEW_FOREX],
            self.edited_client_initial_info[AffiliatePageConstants.ALLOWED_IP],
            self.edited_client_initial_info[AffiliatePageConstants.IS_ENABLED],
            self.edited_client_initial_info[AffiliatePageConstants.EDITED_FIRST_ALLOWED_METHOD],
            self.edited_client_initial_info[AffiliatePageConstants.EDITED_COUNTRY_1])

    def is_affiliate_deleted(self, partner_name):
        self.perform_search_by_partner_name(partner_name)

        """Get text of search of deleted affiliate"""
        search_result = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Data not found')]").text

        if search_result == AffiliatePageConstants.DELETED_AFFILIATE_TEXT:
            return True
        else:
            return False

    def click_delete_icon_and_confirm_deletion(self):
        delete_button = self.driver.find_element(By.XPATH, "//tr[@class='tableRow']//td[12]")
        delete_button.click()

        sleep(1)
        confirm_button = self.driver.find_element(By.XPATH, "//div/bs-modal-footer/div/button[2]")
        confirm_button.click()
        sleep(1)
        return AffiliateListViewPage()
