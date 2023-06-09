from selenium.webdriver import Keys

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def input_in_search_field(self, input_data):
        self._send_keys_on_element(*MainPageLocators.SEARCH_FIELD, input_data)

    def press_enter_to_search(self):
        self._send_keys_on_element(*MainPageLocators.SEARCH_FIELD, Keys.ENTER)

    def open_all_services_popup(self):
        self._click_on_element(*MainPageLocators.SEARCH_FIELD)
        self._click_on_element(*MainPageLocators.ALL_SERVICES_BUTTON)

    def open_images_page(self):
        self.open_all_services_popup()
        self._click_on_element(*MainPageLocators.IMAGES_BUTTON)
        self._switch_to_new_window()

    def should_be_expected_url(self, expected_url):
        assert self._is_open_expected_page(expected_url), "Открыта не та страница"

    def should_be_search_field(self):
        assert self._is_element_present(*MainPageLocators.SEARCH_FIELD)

    def should_be_suggest_list(self):
        assert self._is_element_present(*MainPageLocators.SUGGEST_LIST)

    def should_be_all_services_button(self):
        self._click_on_element(*MainPageLocators.SEARCH_FIELD)
        assert self._is_element_present(*MainPageLocators.ALL_SERVICES_BUTTON)
