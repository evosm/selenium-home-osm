import unittest, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class test_one(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart/admin/"

    def test_login(self):
        driver = self.driver
        try:
            driver.get(self.base_url)
            time.sleep(5)
            user_name_elem = driver.find_element_by_xpath("//*[@type='text']")
            user_name_elem.send_keys('admin')
            user_pass_elem = driver.find_element_by_name('password')
            user_pass_elem.send_keys('admin')
            driver.find_element_by_xpath("//*[@type='submit']").click()
            time.sleep(3)
            menu = driver.find_element_by_xpath("//*[@class='list-vertical']")
            elements_menu = menu.find_elements_by_tag_name("li")
            for id in range(len(elements_menu)):
                print(elements_menu[id].text)
                elements_menu[id].click()
                time.sleep(3)
                driver.find_elements_by_tag_name('h1')
                try:
                    docs = driver.find_element_by_xpath("//*[@class='docs']")
                    list_docs = docs.find_elements_by_tag_name('li')
                    for idx in range(len(list_docs)):
                        print(list_docs[idx].text)
                        list_docs[idx].click()
                        time.sleep(3)
                        driver.find_elements_by_tag_name('h1')
                        docs = driver.find_element_by_xpath("//*[@class='docs']")
                        list_docs = docs.find_elements_by_tag_name('li')
                except NoSuchElementException as e:
                    print('no sub,error:',e)
                menu = driver.find_element_by_xpath("//*[@class='list-vertical']")
                elements_menu = menu.find_elements_by_css_selector("#app-")
        except NoSuchElementException as e:
            print('error:', e)
            self.fail(r'element error')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_one)
    unittest.TextTestRunner(verbosity=2).run(suite)
