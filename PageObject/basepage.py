#!/usr/bin/env python3
# coding:utf-8

import os


class BasePage(object):
    """所有页面的基类，定义页面相关通用方法"""

    def __init__(self, driver):
        """
        初始化获取driver
        """
        self.driver = driver

    def find_element(self, *loc):
        """
        查找一个元素
        :return: 定位的元素
        """
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        查找一组元素
        :return: 定位的元素组
        """
        return self.driver.find_elements(*loc)

    def launch_app(self):
        """
        启动app
        :return:
        """
        self.driver.launch_app()

    def close_app(self):
        """
        关闭app
        :return:
        """
        self.driver.close_app()

    def get_back(self):
        """
        系统返回键
        :return:
        """
        self.driver.keyevent(4)

    def get_home(self):
        """
        系统home键
        :return:
        """
        self.driver.keyevent(3)

    def click(self, loc):
        """
        点击某个元素
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except AttributeError:
            print("未找到%s" % loc)

    def get_text(self, loc):
        """
        获取某个元素的文本值
        :return:
        """
        try:
            return self.driver.find_element(*loc).text
        except AttributeError:
            print("未找到%s" % loc)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        """
        输入框输入字符
        :return:
        """
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("未找到%s" % loc)

    def script(self, js):
        """
        执行js脚本
        :return:
        """
        self.driver.execute_script(js)

    def screen_size(self):
        """
        获取当前屏幕分辨率
        :return: 屏幕分辨率x*y
        """
        return self.driver.get_window_size()

    def swipe_up(self):
        """
        屏幕向上滑动
        :return:
        """
        screen_size = self.screen_size()
        width = screen_size.get('width')
        height = screen_size.get('height')
        self.driver.swipe(width/2, height*3/4, width/2, height/4)

    def swipe_down(self):
        """
        屏幕向下滑动
        :return:
        """
        screen_size = self.screen_size()
        width = screen_size.get('width')
        height = screen_size.get('height')
        self.driver.swipe(width/2, height/4, width/2, height*3/4)

    def swipe_left(self):
        """
        屏幕向左滑动
        :return:
        """
        screen_size = self.screen_size()
        width = screen_size.get('width')
        height = screen_size.get('height')
        self.driver.swipe(width*3/4, height/2, width/4, height/2)

    def swipe_right(self):
        """
        屏幕向右滑动
        :return:
        """
        screen_size = self.screen_size()
        width = screen_size.get('width')
        height = screen_size.get('height')
        self.driver.swipe(width/4, height/2, width*3/4, height/2)

    def screenshot(self, picture_name):
        """
        页面截图
        :return:
        """
        current_path = os.path.dirname(os.path.realpath(__file__))
        screenshot_path = os.path.join(os.path.dirname(current_path), r'Report\Screenshot')
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)

        picture_path = os.path.join(screenshot_path, picture_name)
        self.driver.get_screenshot_as_file(picture_path)

