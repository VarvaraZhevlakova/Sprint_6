from selenium.webdriver.common.by import By


class ManePageLocator:
    scroll = (By.XPATH, "//div[@class='faq-section']")  # Локатор для прокрутки

    # Локаторы вопросов
    questions = [
        (By.XPATH, "//div[@id='accordion__heading-0' and text()='Сколько это стоит? И как оплатить?']"),
        (By.XPATH, "//div[@id='accordion__heading-1' and text()='Хочу сразу несколько самокатов! Так можно?']"),
        (By.XPATH, "//div[@id='accordion__heading-2' and text()='Как рассчитывается время аренды?']"),
        (By.XPATH, "//div[@id='accordion__heading-3' and text()='Можно ли заказать самокат прямо на сегодня?']"),
        (By.XPATH, "//div[@id='accordion__heading-4' and text()='Можно ли продлить заказ или вернуть самокат раньше?']"),
        (By.XPATH, "//div[@id='accordion__heading-5' and text()='Вы привозите зарядку вместе с самокатом?']"),
        (By.XPATH, "//div[@id='accordion__heading-6' and text()='Можно ли отменить заказ?']"),
        (By.XPATH, "//div[@id='accordion__heading-7' and text()='Я жизу за МКАДом, привезёте?']"),
    ]

    # Локаторы ответов
    answers = [
        (By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"),
        (By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"),
        (By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"),
        (By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"),
        (By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"),
        (By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"),
        (By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"),
        (By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"),
    ]

    scroll = (By.XPATH, "//div[@class='Home_SubHeader__zwi_E' and text()='Вопросы о важном']")

    cookie_confirm_button = (By.XPATH, "//button[text()='да все привыкли']")
    input_name = (By.XPATH, "//input[@type='text' and contains(@class, 'Input_Input__1iN_Z') and @placeholder='* Имя']")
    input_lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    input_address = (By.XPATH, "//input[@type='text' and contains(@class, 'Input_Input__1iN_Z') and @placeholder='* Адрес: куда привезти заказ']")
    metro_station_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
    all_stations = (By.XPATH, "//div[@class='select-search']//div[contains(@class, 'select-search__row')]")

    input_number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Далее']")
    bottom_order_button = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    top_order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    calendar_data = (By.XPATH, "//input[@type='text' and @placeholder='* Когда привезти самокат']")

    rental_period_locator = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    choice_period = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    scooter_color_grey = (By.ID, "grey")
    scooter_color_black = (By.ID, "black")
    comment_field = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='Комментарий для курьера']")
    yes_button = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]//button[text()='Да']")
    view_status_button = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]//button[text()='Посмотреть статус']")
    order_confirm_button = (By.XPATH, "//button[text()='Подтвердить заказ']")
    order_success_title = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    success_modal = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(),'Заказ оформлен')]")
    logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    yandex_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")
    yandex_close = ('svg[viewBox="0 0 14 14"][width="18"][height="18"]')