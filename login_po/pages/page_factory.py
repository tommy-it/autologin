"""页面工厂方法"""
# 封装所有实例方法
from pages.open_page import OpenPage


class PageFactory(object):

    def __init__(self, driver):
        self.driver = driver

    def open_page_factory(self):
        """
        打卡页面
        :return:打卡页面对象OpenPage

        """
        return OpenPage(self.driver)
