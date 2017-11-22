import unittest, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class test_two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart/admin/"

    def test_14_1(self):
        driver = self.driver
        wait = WebDriverWait(driver,5)
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            user_name_elem = driver.find_element_by_xpath("//*[@type='text']")
            user_name_elem.send_keys('admin')
            user_pass_elem = driver.find_element_by_name('password')
            user_pass_elem.send_keys('admin')
            driver.find_element_by_xpath("//*[@type='submit']").click()
            driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?app=countries&doc=countries']").click()
            driver.find_element_by_css_selector('#content > div > a').click()
            out_links = driver.find_elements_by_xpath("//*[@class='fa fa-external-link']")
            main_window = driver.current_window_handle
            for link in out_links:
                windows = driver.window_handles
                link.click()
                if (wait.until(EC.new_window_is_opened(windows))):
                    windows = driver.window_handles
                    new = windows[len(windows)-1]
                    driver.switch_to_window(new)
                    driver.find_element_by_tag_name('title')
                    driver.close()
                    driver.switch_to_window(main_window)
        except NoSuchElementException as e:
            print('error:', e)

    def test_14_2(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            user_name_elem = driver.find_element_by_xpath("//*[@type='text']")
            user_name_elem.send_keys('admin')
            user_pass_elem = driver.find_element_by_name('password')
            user_pass_elem.send_keys('admin')
            driver.find_element_by_xpath("//*[@type='submit']").click()
            driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?app=countries&doc=countries']").click()
            driver.find_element_by_css_selector('#content > div > a').click()
            out_links = driver.find_elements_by_xpath("//*[@class='fa fa-external-link']")
            for link in out_links:
                link.click()
                windows = driver.window_handles
                driver.switch_to_window(windows[1])
                if driver.find_element_by_tag_name('title'):
                    driver.close()
                    driver.switch_to_window(windows[0])
        except NoSuchElementException as e:
            print('error:', e)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_two)
    unittest.TextTestRunner(verbosity=2).run(suite)
