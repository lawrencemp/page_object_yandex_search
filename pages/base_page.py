from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        if not self._is_url_correct(url):
            self._open()

    def _open(self):
        self.browser.get(self.url)

    def _get_element(self, by_elem, locator, timeout=6):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by_elem, locator)))

    def _is_url_correct(self, expected_url):
        return self.browser.current_url.__contains__(expected_url)

    def _is_element_present(self, by_elem, locator, timeout=6):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by_elem, locator)))
        except TimeoutException:
            return False
        return True

    def _switch_to_new_window(self):
        new_window = self.browser.window_handles[-1]
        self.browser.switch_to.window(new_window)
