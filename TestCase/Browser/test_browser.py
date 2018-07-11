# !/usr/bin/env python3
# coding:utf-8

import unittest
import time
from parameterized import parameterized
from Common import mydriver
from Common.mylog import MyLog
from TestData import testdata
from PageObject.browser_page import BrowserPage

mylog = MyLog().mylog()
test_data = testdata.read_data('test_browser.xlsx', '访问网址')[1:]  # 测试数据，去除首行字段行


def testcase_name(testcase_func, param_num, param):
    """
    设置测试用例名称，便于在测试报告中展示
    注：修改了parameterized的源代码，测试用例名称中可以用中文

    :param testcase_func: 测试方法名称
    :param param_num: 参数序号
    :param param: 传入参数
    :return: 格式化后的用例名称
    """
    return "%s_%s" % (
        testcase_func.__name__,
        parameterized.to_safe_name(str(param_num) + '_' + str(param.args[0])),
    )


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = mydriver.remote()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    @parameterized.expand(test_data, testcase_func_name=testcase_name)  # 调用数据的传参必须和数据一一对应
    def test_visit_url(self, case_name, url, url_title, generate_data, token):
        mylog.info('Run test case:{}'.format(self._testMethodName))
        print('\n【Step】')

        browser = BrowserPage(self.driver)
        print('* 跳过欢迎页')
        mylog.info('* 跳过欢迎页')
        browser.skip_welcome_page()

        print('* 访问网址:{}'.format(url))
        mylog.info('* 访问网址:{}'.format(url))
        browser.visit_url(url)
        self.driver.implicitly_wait(30)

        print('* 拒绝位置共享')
        mylog.info('* 拒绝位置共享')
        browser.location_share(share=False)

        picture_name = self._testMethodName + '.png'
        print('* 页面截图:', picture_name)
        mylog.info('* 页面截图:{}'.format(picture_name))
        browser.screenshot(picture_name)

        print('【Expect】')

        print('* url_title包含:', url_title)
        mylog.info('* 期望url_title:{},实际url_title:{}。'.format(url_title, browser.url_title()))
        self.assertRegex(browser.url_title(), url_title)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Pycharm执行时注意：鼠标需要放在unittest.main(verbosity=2)代码块的位置，否则会报错
