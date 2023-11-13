"""
PO基类
"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, locations, timeout=5, poll_time=.5):
        """
        公用元素定位方法
        :param locations:传元素对象
        :param timeout:传超时时间，默认5秒
        :param poll_time:传轮询时间，默认0.5秒
        :return:elements
        """
        # *locations拆包方法
        # 显示等待
        # timeout 传超时时间,默认5, poll_frequency 传轮询时间,默认0.5秒
        elements = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_time) \
            .until(lambda x: x.find_element(*locations))
        return elements

    def click_func(self, elements):
        """
        公用的点击事件
        :param elements:传元素对象,可以调用基类find_element_func方法
        :return:无
        """
        elements.click()

    def input_func(self, elements, text):
        """
        公用的输入方法
        :param elements:传元素对象
        :param text:传字符串
        :return:无
        """
        # 清空，再输入
        elements.clera()
        elements.send_keys(text)

    def get_text_func(self, elements):
        """
        公用获取文本信息
        :param elements:
        :return: elements
        """
        elements = elements.text
        return elements
