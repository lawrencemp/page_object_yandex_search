from pages.base_page import BasePage
from pages.locators import SearchResultsPageLocators


class SearchResultsPage(BasePage):
    def should_first_result_have_expected_url(self, expected_url):
        first_result = self._get_element(*SearchResultsPageLocators.FIRST_RESULT_LINK)
        assert first_result.get_attribute("href") == expected_url, "Ожидалась другая ссылка в первом результате поиска"

    def should_be_expected_url(self, expected_url):
        assert self._is_url_correct(expected_url), "Открыта не та страница"
