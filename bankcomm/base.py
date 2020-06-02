from macaca import WebDriver
from retrying import retry
import os
import warnings
from bankcomm.config import hostname, port, target_platform_name, target_package


class ConnectDevice(object):

    def __init__(self):
        self.platform_name = target_platform_name
        self.package = target_package
        self.driver = None

    @warnings.simplefilter('ignore', ResourceWarning)
    @retry(stop_max_attempt_number=3)
    def connect_device(self):
        server_url = {
            'hostname': hostname,
            'port': port
        }
        platform_name = self.target_platform_name.capitalize()
        if platform_name == 'Android':
            package = self.package
            desired_caps = get_device_info(platform_name, package)
        elif platform_name == 'Ios':
            package = self.package
            desired_caps = get_device_info(platform_name.swapcase(), package)
        else:
            pass
        self.driver = WebDriver(desired_caps, server_url)
        print("retry connecting server ...")
        # warnings.simplefilter('ignore', ResourceWarning)
        wd = self.driver.init()
        return wd


def get_device_info(platform_name, package):

    desired_caps = {'platformName': platform_name, 'package': package, 'reuse': 3}
    device_name = os.popen('adb shell getprop ro.product.model').read()
    if device_name:
        desired_caps['deviceName'] = device_name.rstrip("\n")

    return desired_caps


if __name__ == '__main__':
    driver = ConnectDevice()
    driver.connect_device()





