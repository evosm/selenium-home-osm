import unittest
import time

from selenium import webdriver
class test_one(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_login(self):
        driver = self.driver
        driver.get("http://google.com")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_one)
    unittest.TextTestRunner(verbosity=2).run(suite)