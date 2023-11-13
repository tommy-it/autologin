"""
打开界面
"""
from selenium.webdriver.common.by import By
import pages
from base.base_page import BasePage


class OpenPage(BasePage):
    """
    点击进入考勤打开页面
    """

    """
    提取所有元素，且属于一个元组tuple
    """
    # # 取消更新按钮元素
    # cancelEle = By.XPATH, "//*[contains(@text,'取消')]"
    # # 点击工作台按钮元素
    # workspaceEle = By.XPATH, "//*[@resource-id='com.weaver.emobile7:id/address_image']"
    # # 点击考勤按钮元素
    # checkin = By.XPATH,"//*[@resource-id='entrance-page']/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[11]/android.view.View/android.widget.Image"
    # # 打卡按钮元素
    # loginEle = By.XPATH, "//*[(@text,'打卡')]"

    """ 获取传过来的driver"""

    # BasePage已使用，注释即可
    # def __init__(self,driver):
    #     self.driver = driver

    def click_cancel(self):
        """
        点击取消更新
        :return:
        """
        # self.driver.find_element_by_xpath("//*[contains(@text,'取消')]").click()
        # self.driver.find_element(self.cancelEle[0],self.cancelEle[1]).click()
        # self.click_func(self.find_element_func(self.cancelEle))
        # 导入impor pages ,元素都抽取到__init__.py文件
        self.click_func(self.find_element_func(pages.cancelEle))

    def click_workspace(self):
        """
        点击工作台
        :return:
        """
        # self.driver.find_element(self.workspaceEle[0],self.workspaceEle[1]).click()
        self.click_func(self.find_element_func(pages.workspaceEle))

    def click_checkin(self):
        """
        点击考勤
        :return:
        """
        # self.driver.find_element(self.loginEle[0],self.loginEle[1]).click()
        self.click_func(self.find_element_func(pages.checkin))

    def click_login(self):
        """
        点击打卡
        :return:
        """
        self.click_func(self.find_element_func(pages.loginEle))
        # self.get_text_func(self.find_element_func(pages.loginEle))

