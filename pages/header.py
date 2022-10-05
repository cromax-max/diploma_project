from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage
from pages.claim import ClaimListPage
from pages.main import MainPage
from pages.news import NewsListPage


class Header(BasePage):
    _menu = ("accessibility id", "Main menu")
    _main_line = ("xpath", "//android.widget.TextView[@text='Main']")
    _claims_line = ("xpath", "//android.widget.TextView[@text='Claims']")
    _news_line = ("xpath", "//android.widget.TextView[@text='News']")
    _icon = ("accessibility id", "Authorization")

    @property
    def user_icon(self):
        return self.find_element(Header._icon)

    def click_main_menu(self):
        self.find_element(Header._menu).click()
        return self

    def click_main_line(self):
        self.find_element(Header._main_line).click()

        main_page = MainPage(self.driver)
        assert main_page.claims_section_title.is_displayed()
        return main_page

    def click_claims_line(self) -> ClaimListPage:
        self.wait.until(lambda x: x.find_element(*Header._claims_line).is_displayed())
        self.find_element(Header._claims_line).click()

        claim_lst_page = ClaimListPage(self.driver)
        assert claim_lst_page.title.is_displayed()
        return claim_lst_page

    def click_news_line(self):
        self.find_element(Header._news_line).click()

        news_lst_page = NewsListPage(self.driver)
        assert news_lst_page.title.is_displayed()
        return news_lst_page
