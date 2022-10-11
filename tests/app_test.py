import pytest
from hamcrest import assert_that, equal_to_ignoring_case

from tests.testdata import data

pytestmark = pytest.mark.usefixtures("setup")


def test_add_claim(auth):
    main_page, header = auth
    claim_title = data["title"]

    claim_lst_page = main_page \
        .all_claims_view() \
        .click_add_claim_button() \
        .set_claim_title(claim_title) \
        .set_date(data["date"]) \
        .set_time(data["time"]) \
        .set_description(data["description"]) \
        .click_save_button()

    claim = claim_lst_page.find_element(("xpath", f"//android.widget.TextView[@text='{claim_title}']"))
    assert_that(claim.is_displayed())


def test_claim_in_progress(auth):
    main_page, header = auth
    claim_page = header \
        .click_main_menu() \
        .click_claims_line() \
        .click_filter_button() \
        .select_in_progress(False) \
        .click_filtering_ok() \
        .open_first_claim() \
        .click_change_status_button() \
        .click_take_to_work()

    assert_that(claim_page.claim_label.get_attribute("text"), equal_to_ignoring_case("In progress"))
    assert_that(claim_page.claim_label.is_displayed())


def test_filter_claims(auth):
    main_page, header = auth
    claim_page = header \
        .click_main_menu() \
        .click_claims_line() \
        .click_filter_button() \
        .select_open(False) \
        .select_in_progress(False) \
        .select_executed(True) \
        .click_filtering_ok() \
        .open_first_claim()

    assert_that(claim_page.claim_label.get_attribute("text"), equal_to_ignoring_case("Executed"))
    assert_that(claim_page.claim_label.is_displayed())


def test_view_news(auth):
    main_page, header = auth
    news_page = main_page \
        .all_news_view() \
        .click_first_news()

    news_description = news_page.find_element(("id", "ru.iteco.fmhandroid:id/news_item_description_text_view"))
    assert_that(news_description.is_displayed())


def test_add_news(auth):
    main_page, header = auth
    news_title = data["title"]

    ctrl_panel = main_page \
        .all_news_view() \
        .open_control_panel() \
        .click_add_news_button() \
        .set_category(data["category"]) \
        .set_title(news_title) \
        .set_date() \
        .set_time(data["time"]) \
        .set_description(data["description"]) \
        .click_save_button() \

    news = ctrl_panel.find_element(("xpath", f"//android.widget.TextView[@text='{news_title}']"))
    assert_that(news.get_attribute("text"), equal_to_ignoring_case(news_title))
    assert_that(news.is_displayed())
