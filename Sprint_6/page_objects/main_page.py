from selenium.webdriver import Keys
from helpers.element_action import ElementAction
from locators import ManePageLocator
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from urls import base_url_scooter


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ManePageLocator()
        self.element_action = ElementAction(driver)

    def scroll_to_position(self):
        element = self.driver.find_element(*self.locators.scroll)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_and_click_question(self, question_index):
        self.wait_visibility_of_element(self.locators.questions[question_index])
        element = self.driver.find_element(*self.locators.questions[question_index])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def wait_for_answer_to_be_visible(self, question_index):
        self.wait_visibility_of_element(self.locators.answers[question_index])

    def wait_visibility_of_answer(self, question_index):
        answer_locator = self.locators.answers[question_index]
        self.wait_visibility_of_element(answer_locator)

    def get_answer_text(self, question_index):
        answer_locator = self.locators.answers[question_index]
        return self.driver.find_element(*answer_locator).text

    def click_on_question(self, question_index):
        question_locator = self.locators.questions[question_index]
        self.click_on_element(question_locator)

    def get_answer_text(self, question_index):
        answer_locator = self.locators.answers[question_index]
        self.wait_visibility_of_element(answer_locator)
        return self.driver.find_element(*answer_locator).text

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def click_cookie_confirm_button(self):
        self.wait_visibility_of_element(self.locators.cookie_confirm_button)
        self.click_on_element(self.locators.cookie_confirm_button)

    def send_to_input(self, locator):
        name = self.data_generator.generate_first_name()
        self.driver.find_element(*locator).send_keys(name)

    def send_lastname_to_input(self, locator):
        lastname = self.data_generator.generate_last_name()
        self.driver.find_element(*locator).send_keys(lastname)

    def send_address_to_input(self, locator):
        address = self.data_generator.generate_address()
        self.driver.find_element(*locator).send_keys(address)

    def select_random_station(self):
        random_station = self.data_generator.generate_metro_station()
        station_input = self.driver.find_element(*self.locators.metro_station_input)
        station_input.send_keys(random_station)
        station_input.send_keys(Keys.ARROW_DOWN)
        station_input.send_keys(Keys.ENTER)

    def send_number_to_input(self, locator):
        number = self.data_generator.generate_phone_number()
        self.driver.find_element(*locator).send_keys(number)

    def click_on_top_order_button(self):
        self.driver.find_element(*self.locators.top_order_button).click()

    def click_next_button(self):
        self.driver.find_element(*self.locators.next_button).click()

    def send_date_to_input(self, locator):
        date = self.data_generator.get_date_plus_days(5)
        input_field = self.driver.find_element(*locator)
        input_field.send_keys(date)
        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ENTER)

    def select_rental_period(self, rental_period_locator, period):
        self.driver.find_element(*rental_period_locator).click()
        option_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
        self.driver.find_element(*option_locator).click()

    def select_scooter_color(self, color_locator):
        self.driver.find_element(*color_locator).click()

    def click_order_button(self):
        self.driver.find_element(*self.locators.order_button).click()

    def click_confirm_yes_button(self):
        self.driver.find_element(*self.locators.yes_button).click()

    def click_view_status_button(self):
        self.driver.find_element(*self.locators.view_status_button).click()

    def skip_comment_field(self, comment_field_locator):
        comment_field = self.driver.find_element(*comment_field_locator)
        comment_field.clear()

    def click_bottom_order_button(self):
        self.wait_visibility_of_element(self.locators.bottom_order_button)
        self.click_on_element(self.locators.bottom_order_button)

    def click_logo(self):
        self.driver.find_element(*self.locators.logo).click()

    def verify_redirect_to_homepage(self):
        self.click_logo()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(base_url_scooter))

    def click_yandex_logo(self):
        self.driver.find_element(*self.locators.yandex_logo).click()
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)

    def verify_url_contains(self, expected_url_part):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_url_part))

    def close_pop_up_window(self):
        close_button_locator = self.locators.yandex_close
        self.element_action.click_element(close_button_locator)

    def close_driver(self):
        self.driver.quit()


