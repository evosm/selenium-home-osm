import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class test_two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart/admin/"

    def test_17(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            user_name_elem = driver.find_element_by_xpath("//*[@type='text']")
            user_name_elem.send_keys('admin')
            user_pass_elem = driver.find_element_by_name('password')
            user_pass_elem.send_keys('admin')
            driver.find_element_by_xpath("//*[@type='submit']").click()
            driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
            driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1']").click()
            ducks = driver.find_elements_by_partial_link_text('Duck')
            ducks.pop(0)
            for id in range(len(ducks)):
                ducks[id].click()
                for log in driver.get_log('browser'):
                    if log:
                        print('my logs: \n',log)
                    else:print('null log')
                driver.find_element_by_id('doc-catalog').click()
                driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1']").click()
                ducks = driver.find_elements_by_partial_link_text('Duck')
                ducks.pop(0)
        except NoSuchElementException as e:
            print('error:', e)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_two)
    unittest.TextTestRunner(verbosity=2).run(suite)
