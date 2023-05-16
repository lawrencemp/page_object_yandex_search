from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@name="text"]')
    ALL_SERVICES_BUTTON = (By.XPATH, '//a[@data-statlog="services_suggest.more"]')
    SUGGEST_LIST = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]')
    IMAGES_BUTTON = (By.XPATH, '//a[@data-statlog="services-more-popup.item.images"]')


class SearchResultsPageLocators:
    FIRST_RESULT_LINK = (By.XPATH, '//a[contains(@class, "OrganicTitle-Link organic__url") ][@accesskey="1"]')


class ImagesPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@name="text"]')
    NEXT_IMAGE_BUTTON = (By.XPATH, '//div[contains(@class, "CircleButton CircleButton_type_next")]')
    FIRST_IMAGE_CATEGORY = (By.XPATH, '//div[contains(@class, "PopularRequestList-Item_pos_0")]')
    FIRST_IMAGE_PREVIEW = (By.XPATH, '//div[contains(@class,"serp-item_pos_0")]')
    PREV_IMAGE_BUTTON = (By.XPATH, '//div[contains(@class, "CircleButton CircleButton_type_prev")]')
    OPENED_IMAGE = (By.XPATH, '//img[@class="MMImage-Origin"]')
    MODAL_WITH_IMAGE = (By.XPATH, '//div[contains(@class, "ImagesViewer-Container")]')
