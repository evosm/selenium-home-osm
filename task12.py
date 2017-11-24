import unittest, time,random,os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class test_two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart/admin/"

    def test_12(self):
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
            driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
            driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product']").click()
            driver.find_element_by_css_selector('#tab-general > table > tbody > tr:nth-child(1) > td > label:nth-child(3) > input[type="radio"]').click()
            name = 'test' + str(random.randint(0,10))
            driver.find_element_by_name('name[en]').send_keys(name)
            driver.find_element_by_name('code').send_keys(str(random.randint(0, 10)))
            driver.find_element_by_css_selector('#tab-general > table > tbody > tr:nth-child(7) > td > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > input[type="checkbox"]').click()
            quantity = driver.find_element_by_name('quantity')
            quantity.clear()
            quantity.send_keys(str(random.randint(0, 10)))
            driver.find_element_by_name('date_valid_from').send_keys('24.11.2017')
            driver.find_element_by_name('date_valid_to').send_keys('30.11.2017')
            driver.find_element_by_name('new_images[]').send_keys(os.getcwd() + '/3.jpg')
            driver.find_element_by_xpath("//*[@href='#tab-information']").click()
            select = Select(driver.find_element_by_name('manufacturer_id'))
            select.select_by_index(1)
            driver.find_element_by_name('keywords').send_keys('key')
            driver.find_element_by_name('short_description[en]').send_keys('short_des')
            driver.find_element_by_css_selector('div.trumbowyg-editor').send_keys('loool')
            driver.find_element_by_name('head_title[en]').send_keys('head')
            driver.find_element_by_name('meta_description[en]').send_keys('meta_des')
            driver.find_element_by_xpath("//*[@href='#tab-prices']").click()
            driver.find_element_by_name('purchase_price').clear()
            driver.find_element_by_name('purchase_price').send_keys('100')
            select = Select(driver.find_element_by_name('purchase_price_currency_code'))
            select.select_by_index(1)
            driver.find_element_by_name('prices[USD]').send_keys('10')
            driver.find_element_by_name('prices[EUR]').send_keys('1')
            driver.find_element_by_name('save').click()
            test_adding = driver.find_element_by_partial_link_text(name).text
            if  test_adding == name:
                print('added')
            else:print('error')
        except NoSuchElementException as e:
            print('error:', e)

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_two)
    unittest.TextTestRunner(verbosity=2).run(suite)
