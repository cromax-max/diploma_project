from pages.base import BasePage
from pages.claim import ClaimListPage
from pages.news import NewsListPage


class MainPage(BasePage):
    _news_section_title = ("xpath", "//android.widget.TextView[@text='News']")
    _claims_section_title = ("xpath", "//android.widget.TextView[@text='Claims']")
    _all_news_view = ("id", "ru.iteco.fmhandroid:id/all_news_text_view")
    _all_claims_view = ("id", "ru.iteco.fmhandroid:id/all_claims_text_view")

    @property
    def claims_section_title(self):
        return self.find_element(MainPage._claims_section_title)

    @property
    def news_section_title(self):
        return self.find_element(MainPage._news_section_title)

    def all_news_view(self):
        self.find_element(MainPage._all_news_view).click()
        return NewsListPage(self.driver)

    def all_claims_view(self):
        self.find_element(MainPage._all_claims_view).click()
        return ClaimListPage(self.driver)
