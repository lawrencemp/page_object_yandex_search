from selenium.webdriver import Keys

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.search_field = self._get_element(*MainPageLocators.SEARCH_FIELD)

    def should_be_expected_url(self, expected_url):
        assert self.should_be_expected_url(expected_url), "Открыта не та страница"

    def should_be_search_field(self):
        assert self._is_element_present(*MainPageLocators.SEARCH_FIELD)

    def should_be_suggest_list(self):
        assert self._is_element_present(*MainPageLocators.SUGGEST_LIST)

    def should_be_all_services_button(self):
        self.search_field.click()
        assert self._is_element_present(*MainPageLocators.ALL_SERVICES_BUTTON)

    def input_in_search_field(self, input_data):
        self.search_field.send_keys(input_data)

    def press_enter_to_search(self):
        self.search_field.send_keys(Keys.ENTER)

    def open_all_services_popup(self):
        self.search_field.click()
        self._get_element(*MainPageLocators.ALL_SERVICES_BUTTON).click()

    def open_images_page(self):
        self.open_all_services_popup()
        self._get_element(*MainPageLocators.IMAGES_BUTTON).click()
        self._switch_to_new_window()
