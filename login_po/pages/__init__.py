from selenium.webdriver.common.by import By

"""
点击进入考勤打开页面
"""

"""
提取所有元素，且属于一个元组tuple
"""
# 取消更新按钮元素
cancelEle = By.XPATH, "//*[contains(@text,'取消')]"
# 点击工作台按钮元素
workspaceEle = By.XPATH, "//*[@resource-id='com.weaver.emobile7:id/address_image']"
# 点击考勤按钮元素
checkin = By.XPATH, "//*[@resource-id='entrance-page']/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[11]/android.view.View/android.widget.Image"
# 打卡按钮元素
loginEle = By.XPATH, "//*[contains(@text,'打卡')]"
