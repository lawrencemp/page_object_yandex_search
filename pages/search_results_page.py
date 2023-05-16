from pages.base_page import BasePage
from pages.locators import SearchResultsPageLocators


class SearchResultsPage(BasePage):
    def _get_search_result_link(self, by_elem, locator):
        return self._get_element_attribute(by_elem, locator, "href")

    def should_first_result_have_expected_url(self, expected_url):
        first_result_link = self._get_search_result_link(*SearchResultsPageLocators.FIRST_RESULT_LINK)
        assert first_result_link == expected_url, "Ожидалась другая ссылка в первом результате поиска"

    def should_be_expected_url(self, expected_url):
        assert self._is_open_expected_page(expected_url), "Открыта не та страница"
