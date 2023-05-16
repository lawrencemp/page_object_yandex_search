from pages.base_page import BasePage
from pages.locators import ImagesPageLocators


class ImagesPage(BasePage):
    def get_first_category_text(self):
        return self._get_element_attribute(*ImagesPageLocators.FIRST_IMAGE_CATEGORY, "data-grid-text")

    def click_first_category(self):
        self._click_on_element(*ImagesPageLocators.FIRST_IMAGE_CATEGORY)

    def go_to_next_image(self):
        self._click_on_element(*ImagesPageLocators.NEXT_IMAGE_BUTTON)

    def go_to_prev_image(self):
        self._click_on_element(*ImagesPageLocators.PREV_IMAGE_BUTTON)

    def click_on_first_image_preview(self):
        self._click_on_element(*ImagesPageLocators.FIRST_IMAGE_PREVIEW)

    def get_opened_image_link(self):
        return self._get_element_attribute(*ImagesPageLocators.OPENED_IMAGE, "src")

    def should_search_text_be_like_category_text(self, category_text):
        search_text = self._get_element_attribute(*ImagesPageLocators.SEARCH_FIELD, "value")
        assert search_text == category_text, "В поле поиска отображается не название категории"

    def should_be_expected_url(self, expected_url):
        assert self._is_open_expected_page(expected_url), "Открыта не та страница"

    def should_be_opened_same_image(self, old_link):
        new_link = self.get_opened_image_link()
        assert new_link == old_link, "Вернулись не на ту же картинку"

    def should_be_opened_another_image(self, old_link):
        new_link = self.get_opened_image_link()
        assert new_link != old_link, "Картинка не изменилась"

    def should_be_opened_image_modal(self):
        assert self._is_element_present(*ImagesPageLocators.MODAL_WITH_IMAGE), "Картинка не открылась на весь экран"

