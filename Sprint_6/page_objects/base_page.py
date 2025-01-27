from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.gen_input import DataGenerator


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.data_generator = DataGenerator()

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def get_text(self, element_locator):
        return self.driver.find_element(*element_locator).text

    def click_on_button(self, button_locator):
        self.driver.find_element(*button_locator).click()

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def close_driver(self):
        self.driver.quit()


