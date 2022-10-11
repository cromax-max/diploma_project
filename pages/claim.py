from pages.base import BasePage


class ClaimListPage(BasePage):
    _title = ("xpath", "//android.widget.TextView[@text='Claims']")
    _add_claim_button = ("accessibility id", "Add new claim button")
    _filter_button = ("accessibility id", "Filter claim list menu button")

    @property
    def title(self):
        return self.find_element(ClaimListPage._title)

    def click_add_claim_button(self):
        self.find_element(ClaimListPage._add_claim_button).click()

        claim_page = ClaimPage(self.driver)
        assert claim_page.title.is_displayed()
        return claim_page

    def open_claim(self, claim_title):
        el = (
            "xpath", f"//android.widget.TextView[@text='{claim_title}']/following-sibling::android.widget.ImageView[4]")
        self.find_element(el).click()
        return ClaimPage(self.driver)

    def open_first_claim(self):
        self.find_element(("xpath", "//android.widget.ImageView[5]")).click()
        return ClaimPage(self.driver)

    def click_filter_button(self):
        self.find_element(ClaimListPage._filter_button).click()
        return ClaimPage(self.driver)


class ClaimPage(BasePage):
    _title = ("id", "ru.iteco.fmhandroid:id/custom_app_bar_sub_title_text_view")
    _claim_title = ("id", "ru.iteco.fmhandroid:id/title_edit_text")
    _executor = ("id", "ru.iteco.fmhandroid:id/executor_drop_menu_auto_complete_text_view")
    _data = ("id", "ru.iteco.fmhandroid:id/date_in_plan_text_input_edit_text")
    _time = ("id", "ru.iteco.fmhandroid:id/time_in_plan_text_input_edit_text")
    _description = ("id", "ru.iteco.fmhandroid:id/description_edit_text")
    _save_button = ("accessibility id", "Save")
    _cancel_button = ("accessibility id", "Cancel")
    _ok_button = ("id", "android:id/button1")

    _change_status_button = ("accessibility id", "button change status")
    _take_to_work_line = ("xpath", "//android.widget.TextView[@text='take to work']")
    _open_check_box = ("id", "ru.iteco.fmhandroid:id/item_filter_open")
    _in_progress_check_box = ("id", "ru.iteco.fmhandroid:id/item_filter_in_progress")
    _executed_check_box = ("id", "ru.iteco.fmhandroid:id/item_filter_executed")
    _cancelled_check_box = ()
    _filtering_ok_button = ("id", "ru.iteco.fmhandroid:id/claim_list_filter_ok_material_button")
    _claim_label = ("id", "ru.iteco.fmhandroid:id/status_label_text_view")

    def __init__(self, driver):
        super().__init__(driver)
        self.open_check_box = True
        self.in_progress_check_box = True
        self.executed_check_box = False

    @property
    def title(self):
        return self.find_element(ClaimPage._title)

    @property
    def claim_label(self):
        return self.find_element(ClaimPage._claim_label)

    def set_claim_title(self, value):
        self.find_element(ClaimPage._claim_title).clear().send_keys(value)
        return self

    def set_executor(self, value):
        self.find_element(ClaimPage._executor).clear().send_keys(value)
        return self

    def set_date(self, value=None):
        self.find_element(ClaimPage._data).clear().send_keys(value)
        # self.find_element(ClaimPage._data).click()
        # self.find_element(("id", "android:id/button1")).click()
        return self

    def set_time(self, value):
        self.find_element(ClaimPage._time).clear().send_keys(value)
        return self

    def set_description(self, value):
        self.find_element(ClaimPage._description).clear().send_keys(value)
        return self

    def click_save_button(self):
        self.find_element(ClaimPage._save_button).click()

        claim_lst_page = ClaimListPage(self.driver)
        assert claim_lst_page.title.is_displayed()
        return claim_lst_page

    def click_cancel_button(self):
        self.find_element(ClaimPage._cancel_button).click()
        self.find_element(ClaimPage._ok_button).click()

        claim_lst_page = ClaimListPage(self.driver)
        assert claim_lst_page.title.is_displayed()
        return claim_lst_page

    def click_change_status_button(self):
        self.find_element(ClaimPage._change_status_button).click()
        return self

    def click_take_to_work(self):
        self.find_element(ClaimPage._take_to_work_line).click()
        return self

    def select_open(self, value: bool):
        if self.open_check_box == value:
            return
        self.find_element(ClaimPage._open_check_box).click()
        self.open_check_box = value
        return self

    def select_in_progress(self, value: bool):
        if self.in_progress_check_box == value:
            return
        self.find_element(ClaimPage._in_progress_check_box).click()
        self.in_progress_check_box = value
        return self

    def select_executed(self, value: bool):
        if self.executed_check_box == value:
            return
        self.find_element(ClaimPage._executed_check_box).click()
        self.executed_check_box = value
        return self

    def click_filtering_ok(self):
        self.find_element(ClaimPage._filtering_ok_button).click()
        return ClaimListPage(self.driver)
