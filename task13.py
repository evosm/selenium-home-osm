import unittest,time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class test_two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart"

    def test_13(self):
        driver = self.driver
        wait = WebDriverWait(driver,5)
        driver.implicitly_wait(3)
        try:
            driver.get(self.base_url)
            for i in range(0,3):
                driver.find_element_by_css_selector('li.product.column.shadow.hover-light').click()
                try:
                    driver.find_element_by_name('options[Size]')
                    sel = Select(driver.find_element_by_name('options[Size]'))
                    sel.select_by_index(1)
                except NoSuchElementException as e:
                    print('no select')
                driver.find_element_by_name('add_cart_product').click()
                s = str(i+1)
                if (wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#cart > a.content > span.quantity'),s))):
                    driver.find_element_by_css_selector('#breadcrumbs > ul > li:nth-child(1) > a').click()
                    print('added')
                else:print('adding error')
            driver.find_element_by_partial_link_text('Checkout »').click()
            for i in range(0,3):
                driver.find_element_by_name('remove_cart_item').click()
                wait_one = wait.until(EC.staleness_of(driver.find_element_by_css_selector('#order_confirmation-wrapper > table > tbody > tr.footer > td:nth-child(2) > strong')))
                if i != 2:
                    wait_two = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#order_confirmation-wrapper > table')))
                if (wait_one and wait_two):
                    print('removed')
                else:print('remove error')
            if driver.find_element_by_tag_name('em').text == 'There are no items in your cart.':
                print('Completed')
        except NoSuchElementException as e:
            print('error:', e)

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_two)
    unittest.TextTestRunner(verbosity=2).run(suite)
