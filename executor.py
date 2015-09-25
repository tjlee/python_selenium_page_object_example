import unittest
from pageobjects import selenium_driver
from pageobjects.login import LoginPageObject


class AboutPageTests(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_login(self):
        lpo = LoginPageObject(self.driver, self.base_url)

        lpo.username = "mail@mail.info"
        lpo.password = "pwdpwd123"
        lpo.submit()


if __name__ == "__main__":
    unittest.main()