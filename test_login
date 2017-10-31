from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class loggin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:801/litecart/admin/"

    def test_login(self):
        driver = self.driver
        try:
            driver.get(self.base_url)
            time.sleep(3)
            user_name_elem = driver.find_element_by_xpath("//*[@type='text']")
            user_name_elem.send_keys('admin')
            user_pass_elem = driver.find_element_by_name('password')
            user_pass_elem.send_keys('admin')
            driver.find_element_by_xpath("//*[@type='submit']").click()
        except NoSuchElementException as e:
            self.fail(r'element error')
            print('Возникла ошибка в тесте на логин')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(loggin.test_login)
