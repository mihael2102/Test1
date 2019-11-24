from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class ClientProfileUpdate(CRMBasePage):

    def edit_first_name_by_pencil(self, first_name_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'First Name')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//input[@name='firstname']")
        edited_field_element.clear()
        edited_field_element.send_keys(first_name_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_First Name']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The first name was edited on the " + first_name_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_last_name_by_pencil(self, last_name_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'Last Name')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//input[@name='lastname']")
        edited_field_element.clear()
        edited_field_element.send_keys(last_name_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_Last Name']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The last name was edited on the " + last_name_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_phone_by_pencil(self, phone_number_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'Phone')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//input[@name='phone']")
        edited_field_element.clear()
        edited_field_element.send_keys(phone_number_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_Phone']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The phone was edited on the " + phone_number_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_citizen_ship_by_pencil(self, parameter_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'Citizen')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()

        edit_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='citizenships']")))

        select = Select(edit_field)
        select.select_by_visible_text(parameter_update)

        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_Citizenship']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The citizen ship was edited on the " + parameter_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_address_by_pencil(self, parameter_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'Address')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//textarea[@name='address']")
        edited_field_element.clear()
        edited_field_element.send_keys(parameter_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_Address']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The address was edited on the " + parameter_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_post_code_by_pencil(self, phone_number_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'Code')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//input[@name='post_code']")
        edited_field_element.clear()
        edited_field_element.send_keys(phone_number_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_Code']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The post code was edited on the " + phone_number_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_city_by_pencil(self, city_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'City')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//input[@name='city']")
        edited_field_element.clear()
        edited_field_element.send_keys(city_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_City']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The city  was edited on the " + city_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_country_by_pencil(self, parameter_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'Country')]//following-sibling::td[1]")
        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()

        edit_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='countries']")))

        select = Select(edit_field)
        select.select_by_visible_text(parameter_update)

        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_Country']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The country was edited on the " + parameter_update + " from client profile page")
        return ClientProfileUpdate(self.driver)

    def edit_assign_to_by_pencil(self, user):
        self.driver.refresh()
        element_field = super().wait_load_element("//td[text()='Assigned To']//following-sibling::td[1]")
        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()

        edit_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='assigned_user_id']")))

        select = Select(edit_field)
        select.select_by_visible_text(user)

        save_button = self.driver.find_element(By.XPATH,
                                               "//div[@id='editarea_Assigned To']//span[@class='glyphicons ok_2']")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        Logging().reportDebugStep(self,
                                  "The Assign To was updated to " + user)
        return ClientProfileUpdate(self.driver)

    def perform_scroll(self, parameter):
        super().perform_scroll(parameter)
        Logging().reportDebugStep(self,
                                  "The scroll  was performed on the ")
        return ClientProfileUpdate(self.driver)

    def click_edit_client_button(self):
        sleep(1)
        edit_lead = super().wait_load_element("//input[@name='Edit']", timeout=35)
        edit_lead.click()
        Logging().reportDebugStep(self, "Click Edit button")
        return ClientProfileUpdate(self.driver)

    def click_show_phone_edit_page(self):
        sleep(0.1)
        try:
            show_phone_btn = super().wait_load_element("//a[@id='show-phone-eye']/span[@title='Show Phone Number']")
            self.driver.execute_script("arguments[0].click();", show_phone_btn)
            Logging().reportDebugStep(self, "Click Show Phone Number button")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "There are no 'Show Phone Number' button")
        return ClientProfileUpdate(self.driver)

    def get_phone_edit_page(self):
        sleep(1)
        phone = super().wait_load_element("//*[@id='phone']").get_attribute("value")
        Logging().reportDebugStep(self, "Get phone from Edit page: " + phone)
        return phone

    def set_phone(self, phone):
        phone_field = super().wait_load_element("//div[@id='popupcontent']//input[@name='phone']")
        phone_field.clear()
        phone_field.send_keys(phone)
        Logging().reportDebugStep(self, "The phone number was set: " + phone)
        return ClientProfileUpdate(self.driver)

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH, "//input[@value='Save']")
        self.perform_scroll_up()
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked: ")
        return ClientProfileUpdate(self.driver)

    def edit_first_name(self, fname):
        first_name_field = super().wait_load_element("//*[@id='first_name']")
        first_name_field.clear()
        first_name_field.send_keys(fname)
        Logging().reportDebugStep(self, "Set First Name: " + fname)
        return ClientProfileUpdate(self.driver)

    def edit_city(self, city):
        city_field = super().wait_load_element("//*[@id='city']")
        city_field.clear()
        city_field.send_keys(city)
        Logging().reportDebugStep(self, "Set City: " + city)
        return ClientProfileUpdate(self.driver)

    def edit_country(self, country):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='countries']")))
        country_field = Select(self.driver.find_element(By.XPATH, "//*[@id='countries']"))
        country_field.select_by_visible_text(country)
        Logging().reportDebugStep(self, "Set Country: " + country)
        return ClientProfileUpdate(self.driver)
