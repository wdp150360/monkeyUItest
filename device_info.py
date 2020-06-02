import os
import unittest
from macaca import WebDriver
from retrying import retry
import warnings
import json

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'MI 8 Lite',
    'package': 'com.bankcomm',
    # 'noReset': "True",
    # 'autoAcceptAlerts': "True",
    'reuse': 3

}
server_url = {
    'hostname': 'localhost',
    'port': 3456
}


def device_info():
    name = os.popen('adb shell getprop ro.product.model').read()
    # udids = os.system('adb devices')
    # udid = os.popen('adb devices').read()
    # print(udids >> 8)
    print(name == '')
    print(type(name))
    # print(udid)

    # driver = WebDriver(desired_caps, server_url)
    # driver = driver.init()
    # context = driver.context
    # print(context)


class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @classmethod
    @retry(stop_max_attempt_number=3)
    def initDriver(self):
        print("retry connecting server ...")
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver.init()

    def test_currentContext(self):
        context_source = self.driver.source
        print(type(context_source))
        context_source_json = json.loads(context_source)
        context_active = self.driver.get_window_size()
        print(context_active)
        print(context_source)
        print(type(context_source_json))
        print(context_source_json)

    @unittest.skip
    def test_pass(self):
        a = 1
        b = 1


if '__main__' == __name__:
    # unittest.main()
    device_info()
