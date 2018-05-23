from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.utils.config import Config

from src.main.python.utils.waitting_utils.WaitingUtils import WaitingUtils


class CRMBasePage(object):

    def __init__(self):
        self.driver = Config.browser

    def open_second_tab_page(self, url):
        self.driver.execute_script("window.open()")
        Config.window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(Config.window_after)
        self.driver.get(url)

    def open_first_tab_page(self, url):
        self.driver.get(url)
        Config.window_before = self.driver.window_handles[0]

    def wait_load_element(self, element):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element)))

    def refreshing_wait(self, account):
        return WaitingUtils().wait_until_element_present_ca(account, self.driver)

    def switch_first_tab_page(self):
        self.driver.switch_to_window(Config.window_before)

    def switch_second_tab_page(self):
        self.driver.switch_to_window(Config.window_after)

    def came_back_on_previous_page(self):
        self.driver.back()

    def open_deposit_page(self):
        self.wait_load_element("//div[@class='button-pandats']")

    def wait_until_element_present(self, element, total_amount_crm):
        return WaitingUtils().wait_until_element_present_crm(element, total_amount_crm, self.driver)

    def edit_client_profile_by_pencil(self, first_name_update, first_name_element, edited_field, save_button_element):
        first_name_field_element = self.driver.find_element(By.XPATH,
                                                            "//td[contains(text(),'%s')]//following-sibling::td[1]" % first_name_element)
        self.wait_load_element(first_name_field_element)
        element_to_move_pencil = self.driver.find_element(By.XPATH, "//span[@class='glyphicons pencil cntrl']")
        hoverer = ActionChains(self.driver).move_to_element(first_name_field_element).click(element_to_move_pencil)
        hoverer.perform()
        edited_field_element = self.driver.find_element(By.XPATH, "//input[@name='%s']" % edited_field)
        edited_field_element.clear()
        edited_field_element.send_keys(first_name_update)
        save_button = self.driver.find_element(By.XPATH, "//div[@id='%s']//span[1]" % save_button_element)
        hoverer = ActionChains(self.driver).move_to_element(save_button).click(save_button)
        hoverer.perform()
