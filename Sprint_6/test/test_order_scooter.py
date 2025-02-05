from page_objects.main_page import MainPage
from urls import base_url_scooter, yandex_url
import allure
import pytest


class TestOrderScooter:

    @pytest.mark.parametrize(
        "order_button_position, rental_period, scooter_color",
        [
            ("bottom", "двое суток", "grey"),
            ("bottom", "четверо суток", "black"),
            ("top", "двое суток", "grey"),
            ("top", "четверо суток", "black")
        ]
    )
    @allure.title('Проверяем успешность оформление заказа скутера с разным набором данных')
    @allure.description('После нажатия на кнопки "Заказ" в разных местах, заполняем формы и выполняем сам заказ')
    def test_order_scooter_success(self, driver, order_button_position, rental_period, scooter_color):
        driver.get(base_url_scooter)

        main_page = MainPage(driver)
        main_page.click_cookie_confirm_button()

        if order_button_position == "top":
            main_page.click_on_top_order_button()
        else:
            main_page.click_bottom_order_button()

        main_page.send_to_input(main_page.locators.input_name)
        main_page.send_lastname_to_input(main_page.locators.input_lastname)
        main_page.send_address_to_input(main_page.locators.input_address)
        main_page.send_number_to_input(main_page.locators.input_number)

        main_page.select_random_station()
        main_page.click_next_button()
        main_page.send_date_to_input(main_page.locators.calendar_data)
        main_page.select_rental_period(main_page.locators.rental_period_locator, rental_period)

        scooter_color_locator = (
            main_page.locators.scooter_color_grey if scooter_color == "grey"
            else main_page.locators.scooter_color_black
        )
        main_page.select_scooter_color(scooter_color_locator)

        main_page.skip_comment_field(main_page.locators.comment_field)
        main_page.click_order_button()
        main_page.click_confirm_yes_button()

        assert main_page.wait_visibility_of_element(
            main_page.locators.success_modal
        ), "Окно с сообщением об успешном заказе не появилось."
        main_page.click_view_status_button()

    @pytest.mark.parametrize(
        "order_button_position, rental_period, scooter_color",
        [
            ("bottom", "двое суток", "grey"),
            ("bottom", "четверо суток", "black"),
            ("top", "двое суток", "grey"),
            ("top", "четверо суток", "black")
        ]
    )
    @allure.title('Проверяем попадаение на главную страницу, после нажатия на лого "Самоката"')
    @allure.description('После успешного оформления заказа, нажимаем на лого "Самоката" и проверяем переход на главную страницу')
    def test_redirect_to_homepage(self, driver, order_button_position, rental_period, scooter_color):
        self.test_order_scooter_success(driver, order_button_position, rental_period, scooter_color)

        main_page = MainPage(driver)
        main_page.click_logo()
        main_page.verify_redirect_to_homepage()

        assert driver.current_url == base_url_scooter, "Переход на главную страницу не произошел."

        main_page.close_driver()

    @pytest.mark.parametrize(
        "order_button_position, rental_period, scooter_color, expected_url",
        [
            ("bottom", "двое суток", "grey", yandex_url),
            ("bottom", "четверо суток", "black", yandex_url),
            ("top", "двое суток", "grey", yandex_url),
            ("top", "четверо суток", "black", yandex_url)
        ]
    )
    @allure.title('Проверяем редирект на Дзен после нажатия на лого Яндекса')
    @allure.description('После успешного оформления заказа, нажимаем на лого "Яндекса" и проверяем редирект на страницу Дзен')
    def test_redirect_to_yandex(self, driver, order_button_position, rental_period, scooter_color, expected_url):
        self.test_order_scooter_success(driver, order_button_position, rental_period, scooter_color)

        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.verify_url_contains(yandex_url)

        assert driver.current_url == expected_url, f"Переход на страницу Яндекса не произошел. Ожидался URL: {expected_url}"

        main_page.close_driver()



