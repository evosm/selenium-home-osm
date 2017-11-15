import unittest, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class test_sticker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart/"

    def test_login(self):
        driver = self.driver
        try:
            driver.get(self.base_url)
            driver.implicitly_wait(5)
            product_list = driver.find_elements_by_css_selector('li.product')
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
    suite = unittest.TestLoader().loadTestsFromTestCase(test_sticker)
    unittest.TextTestRunner(verbosity=2).run(suite)
