import time

import pytest

from pages.open_page import OpenPage
from pages.page_factory import PageFactory
from utils import init_driver


class TestSetting(object):
    @pytest.fixture(autouse=True)
    def driver_func(self):
        # 实例化对象
        self.driver = init_driver()
        # 将【某个页面的】driver实例化以后可以多次使用
        # self.open_page = OpenPage(self.driver)
        # 引入工厂模式获取对象
        self.page_factory = PageFactory(self.driver)

        yield
        # 等待3秒
        time.sleep(5)
        # 退出驱动对象
        self.driver.quit()

    def test_open(self):
        # self.page_factory.click_cancel()
        self.page_factory.open_page_factory().click_workspace()
        self.page_factory.open_page_factory().click_checkin()
        self.page_factory.open_page_factory().click_login()
