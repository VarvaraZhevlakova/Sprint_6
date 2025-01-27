import allure
from page_objects.main_page import MainPage
from urls import base_url_scooter
import pytest


class TestQuestionsPage:

    @pytest.mark.parametrize(
        "question_index, expected_text",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
        ],
    )
    @allure.title('Получаем ответы, кликая на вопросы')
    @allure.description('Заходим на страницу, скролим вниз к "Вопрасам о важном", кликаем на вопрос, получаем текст, проверяем, чтот текст соответсвует ожидаемому результату')
    def test_question(self, driver, question_index, expected_text):
        driver.get(base_url_scooter)

        main_page = MainPage(driver)
        main_page.click_cookie_confirm_button()

        main_page.scroll_to_position()
        main_page.scroll_to_and_click_question(question_index)

        dropdown_text = main_page.get_answer_text(question_index)

        assert dropdown_text == expected_text, f"Ожидался текст: '{expected_text}', но получен: '{dropdown_text}'"
