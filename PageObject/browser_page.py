#!/usr/bin/env python3
# coding:utf-8

from selenium.webdriver.common.by import By
from PageObject import basepage
from Common import mydriver
import time


class BrowserPage(basepage.BasePage):
    """浏览器首页，定义页面通用属性和方法"""

    welcome_page_confirm_button = (By.ID, "com.android.browser:id/button1")
    input_url = (By.ID, "com.android.browser:id/text_url")
    input_adress = (By.ID, "com.android.browser:id/input_address")
    url_forword = (By.ID, "com.android.browser:id/browser_inputtitlebar_done")
    not_share_button = (By.ID, "com.android.browser:id/not_share_button")
    share_button = (By.ID, "com.android.browser:id/share_button")

    def skip_welcome_page(self):
        """
        跳过欢迎页
        :return:
        """
        self.click(self.welcome_page_confirm_button)

    def visit_url(self, url):
        """
        访问url网址
        :return:
        """
        self.click(self.input_url)
        self.send_keys(self.input_adress, url)
        self.click(self.url_forword)

    def url_title(self):
        """
        获取当前网址url文本
        :return: 当前url title
        """
        return self.get_text(self.input_url)

    def location_share(self, share=False):
        """
        是否共享位置
        :return:
        """
        if share:
            self.click(self.share_button)
        else:
            self.click(self.not_share_button)


if __name__ == '__main__':
    driver = mydriver.remote()
    browser = BrowserPage(driver)
    browser.skip_welcome_page()
    time.sleep(2)
    browser.visit_url('https://www.baidu.com')
    time.sleep(5)
    browser.location_share()
    time.sleep(2)
    url_title = browser.url_title()
    print(url_title)
    driver.quit()

