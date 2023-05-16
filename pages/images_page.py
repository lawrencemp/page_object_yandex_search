from pages.base_page import BasePage
from pages.locators import ImagesPageLocators


class ImagesPage(BasePage):
    def get_category_text(self):
        return self._get_element(*ImagesPageLocators.FIRST_IMAGE_CATEGORY).get_attribute("data-grid-text")

    def should_be_expected_url(self, expected_url):
        assert self._is_url_correct(expected_url), "Открыта не та страница"

    def click_first_category(self):
        self._get_element(*ImagesPageLocators.FIRST_IMAGE_CATEGORY).click()

    def should_search_text_be_like_category_text(self, category_text):
        search_text = self._get_element(*ImagesPageLocators.SEARCH_FIELD).get_attribute("value")
        assert search_text == category_text, "В поле поиска отображается не название категории"

    def click_on_image_preview(self):
        self._get_element(*ImagesPageLocators.FIRST_IMAGE_PREVIEW).click()

    def get_opened_image_link(self):
        return self._get_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute("src")

    def should_return_on_same_image(self, old_link):
        new_link = self.get_opened_image_link()
        assert new_link == old_link, "Вернулись не на ту же картинку"

    def should_image_change(self, old_link):
        new_link = self.get_opened_image_link()
        assert new_link != old_link, "Картинка не изменилась"

    def should_be_open_image_modal(self):
        assert self._is_element_present(*ImagesPageLocators.MODAL_WITH_IMAGE), "Картинка не открылась на весь экран"

    def go_to_next_image(self):
        self._get_element(*ImagesPageLocators.NEXT_IMAGE_BUTTON).click()

    def go_to_prev_image(self):
        self._get_element(*ImagesPageLocators.PREV_IMAGE_BUTTON).click()
