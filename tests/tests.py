from pages.images_page import ImagesPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from utils.urls import *


def test_search_tenzor(browser):
    main_page = MainPage(browser, YANDEX_SEARCH_URL)
    main_page.should_be_search_field()
    main_page.input_in_search_field("Тензор")
    main_page.should_be_suggest_list()
    main_page.press_enter_to_search()
    search_results_page = SearchResultsPage(browser, browser.current_url)
    search_results_page.should_be_expected_url(YANDEX_SEARCH_RESULTS_URL)
    search_results_page.should_first_result_have_expected_url(TENZOR_URL)


def test_yandex_images(browser):
    main_page = MainPage(browser, YANDEX_SEARCH_URL)
    main_page.should_be_all_services_button()
    main_page.open_images_page()
    images_page = ImagesPage(browser, browser.current_url)
    images_page.should_be_expected_url(YANDEX_IMAGES_URL)
    category_text = images_page.get_category_text()
    images_page.click_first_category()
    images_page.should_search_text_be_like_category_text(category_text)
    images_page.click_on_image_preview()
    images_page.should_be_open_image_modal()
    first_image_link = images_page.get_opened_image_link()
    images_page.go_to_next_image()
    images_page.should_image_change(first_image_link)
    images_page.go_to_prev_image()
    images_page.should_return_on_same_image(first_image_link)
