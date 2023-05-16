from pages.images_page import ImagesPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from utils.urls import *
import allure


def test_search_tenzor(browser):
    with allure.step("1) Зайти на https://ya.ru/"):
        main_page = MainPage(browser, YANDEX_SEARCH_URL)
        main_page.open()

    with allure.step("2) Проверить наличия поля поиска"):
        main_page.should_be_search_field()

    with allure.step("3) Ввести в поиск Тензор"):
        main_page.input_in_search_field("Тензор")

    with allure.step("4) Проверить, что появилась таблица с подсказками (suggest)"):
        main_page.should_be_suggest_list()

    with allure.step("5) Нажать enter"):
        main_page.press_enter_to_search()

    with allure.step("6) Проверить, что появилась страница результатов поиска"):
        search_results_page = SearchResultsPage(browser, browser.current_url)
        search_results_page.should_be_expected_url(YANDEX_SEARCH_RESULTS_URL)

    with allure.step("7) Проверить 1 ссылка ведет на сайт tensor.ru"):
        search_results_page.should_first_result_have_expected_url(TENZOR_URL)


def test_yandex_images(browser):
    with allure.step("1) Зайти на ya.ru"):
        main_page = MainPage(browser, YANDEX_SEARCH_URL)
        main_page.open()

    with allure.step("2) Проверить, что кнопка меню присутствует на странице \
    (Появляется после нажатия на поле поиска)"):
        main_page.should_be_all_services_button()

    with allure.step("3) Открыть меню, выбрать “Картинки”"):
        main_page.open_images_page()

    with allure.step("4) Проверить, что перешли на url https://yandex.ru/images/"):
        images_page = ImagesPage(browser, browser.current_url)
        images_page.should_be_expected_url(YANDEX_IMAGES_URL)

    with allure.step("5) Открыть первую категорию"):
        category_text = images_page.get_first_category_text()
        images_page.click_first_category()

    with allure.step("6) Проверить, что название категории отображается в поле поиска"):
        images_page.should_search_text_be_like_category_text(category_text)

    with allure.step("7) Открыть 1 картинку"):
        images_page.click_on_first_image_preview()

    with allure.step("8) Проверить, что картинка открылась"):
        images_page.should_be_opened_image_modal()
        first_image_link = images_page.get_opened_image_link()

    with allure.step("9) Нажать кнопку вперед"):
        images_page.go_to_next_image()

    with allure.step("10. Проверить, что картинка сменилась"):
        images_page.should_be_opened_another_image(first_image_link)

    with allure.step("11. Нажать назад"):
        images_page.go_to_prev_image()

    with allure.step("12. Проверить, что картинка осталась из шага 8"):
        images_page.should_be_opened_same_image(first_image_link)

