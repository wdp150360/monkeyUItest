import unittest
from bankcomm.actions import Actions
from bankcomm.page_elements_parse import WebPageParseList
from bankcomm.random_num import RandomSeed
from bankcomm.base import ConnectDevice
from bankcomm.__init__ import rs
from bankcomm.config import project_config, seed

"""测试主入口"""


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = ConnectDevice().connect_device()
        cls.rs = rs
        cls.random_seed = RandomSeed(seed)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_one_page_random(self):
        source_str = self.driver.source
        elements_list = WebPageParseList(source_str).parse_source_list()
        elements_list_random = self.random_seed.shuffle(elements_list)
        for element in elements_list_random:
            if element.get('enabled', None):
                bounds = element.get('bounds', None)
                point = self.random_seed.rect_center_point(bounds)
                Actions(self.driver).touch_action(point)

                pass

            if element.get('scrollable', None):
                bounds = element.get('bounds', None)
                points = self.random_seed.slide_points(bounds)
                Actions(self.driver).slide_action(points)

                pass

    def test_many_pages_random(self):
        # depth = project_config['depth']
        pass

    def test_limited_pages_random(self, limited_pages):
        pass

    def test_all_pages_random(self):
        pass
