__author__ = 'v.chernov'
import unittest
import time


class BasePageObject(unittest.TestCase):
    def wait_for_element_displayed_by_id(self, driver, locator, timeout=60, msg="[error] element is not found"):
        for i in range(timeout):
            try:
                if driver.find_element_by_id(locator).is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)