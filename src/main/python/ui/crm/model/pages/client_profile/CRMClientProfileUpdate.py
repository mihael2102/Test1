from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


class CRMClientProfileUpdate(CRMBasePage):
    def __init__(self):
        super().__init__()

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
        return CRMClientProfileUpdate()

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
        return CRMClientProfileUpdate()

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
        return CRMClientProfileUpdate()

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
        return CRMClientProfileUpdate()

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
        return CRMClientProfileUpdate()

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
        return CRMClientProfileUpdate()

    def edit_city_by_pencil(self, phone_number_update):
        self.driver.refresh()
        element_field = super().wait_load_element(
            "//td[contains(text(),'City')]//following-sibling::td[1]")

        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(element_field).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//input[@name='city']")
        edited_field_element.clear()
        edited_field_element.send_keys(phone_number_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='editarea_City']//span[1]")
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
        return CRMClientProfileUpdate()

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
        return CRMClientProfileUpdate()

    def perform_scroll(self, parameter):
        super().perform_scroll(parameter)
        return CRMClientProfileUpdate()
