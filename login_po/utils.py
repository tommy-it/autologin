from appium import webdriver


def init_driver():
    """初始化获取驱动对象"""
    capabilities = {
        "platformName": "Android",
        "platformVersion": "10.0.0",
        "deviceName": "你的设备名称",
        "appPackage": "com.weaver.emobile7",
        "appActivity": "weaver.fw.com.WelcomeActivity",
        "noReset": True
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver
