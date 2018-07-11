#!/usr/bin/env python3
# coding:utf-8

import time
from appium import webdriver
from Config.readConfig import ReadConfig

readconfig = ReadConfig()


def remote():
    desired_caps = {
        'platformName': readconfig.desired_caps('platformName'),
        'platformVersion': readconfig.desired_caps('platformVersion'),
        'deviceName': readconfig.desired_caps('deviceName'),
        'appPackage': readconfig.desired_caps('appPackage'),
        'appActivity': readconfig.desired_caps('appActivity'),
        'unicodeKeyboard': readconfig.desired_caps('unicodeKeyboard'),
        'resetKeyboard': readconfig.desired_caps('resetKeyboard')
    }
    driver = webdriver.Remote(readconfig.desired_caps('remote_url'), desired_caps)
    return driver


if __name__ == '__main__':
    dr = remote()
    time.sleep(5)
    dr.quit()



