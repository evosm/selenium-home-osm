import unittest, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class test_two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart/"

    def test_login(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            product_list = driver.find_elements_by_css_selector('li.product')
            if len(product_list) == 0:
                self.fail(r'no elements')
            else:
                for id in range(len(product_list)):
                    sticker = product_list[id].find_elements_by_css_selector("div.sticker")
                    if len(sticker) == 0 or len(sticker) > 1:
                        self.fail('error')
        except NoSuchElementException as e:
            print('error:', e)
            self.fail(r'element error')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_two)
    unittest.TextTestRunner(verbosity=2).run(suite)
