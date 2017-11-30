import unittest,time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost/litecart"
        self.wait = WebDriverWait(self.driver, 5)
        self.main_page = main_page(base_url=self.base_url,driver=self.driver,wait=self.wait)
        self.product_page = product_page(base_url=self.base_url,driver=self.driver,wait=self.wait)
        self.checkout_page = checkout_page(base_url=self.base_url,driver=self.driver,wait=self.wait)

    def test_19(self):
        self.main_page.start()
        for i in range(0,3):
            self.main_page.work_on_page()
            self.product_page.work_on_page()
        self.checkout_page.work_on_page()

    def tearDown(self):
            self.driver.close()

class main_page:
    def __init__(self,**kwargs):
        self.base_url = kwargs['base_url']
        self.driver = kwargs['driver']

    def start(self):
        self.driver.get(self.base_url)

    def work_on_page(self):
        try:
            self.driver.find_element_by_css_selector('li.product.column.shadow.hover-light').click()
        except NoSuchElementException as e:
            print('error:', e)
        except TimeoutError as e:
            print('error', e)

class product_page:
    def __init__(self,**kwargs):
        self.driver = kwargs['driver']
        self.wait = kwargs['wait']
    def work_on_page(self):
        try:
            self.driver.find_element_by_name('options[Size]')
            sel = Select(self.driver.find_element_by_name('options[Size]'))
            sel.select_by_index(1)
        except NoSuchElementException as e:
            print('no select', e)
        try:
            quantity = self.driver.find_element_by_css_selector('span.quantity').text
            s = int(quantity)+1
            self.driver.find_element_by_name('add_cart_product').click()
            if (self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart > a.content > span.quantity'),str(s)))):
                self.driver.find_element_by_css_selector('#breadcrumbs > ul > li:nth-child(1) > a').click()
                print('added')
            else:
                print('adding error')
        except NoSuchElementException as e:
            print('no select', e)
        except TimeoutError as e:
            print('error', e)

class checkout_page:
    def __init__(self,**kwargs):
        self.driver = kwargs['driver']
        self.wait = kwargs['wait']
    def work_on_page(self):
        try:
            self.driver.find_element_by_partial_link_text('Checkout »').click()
            for i in range(0, 3):
                elem_table = self.driver.find_element_by_css_selector(
                    '#order_confirmation-wrapper > table > tbody > tr.footer > td:nth-child(2) > strong')
                self.driver.find_element_by_name('remove_cart_item').click()
                wait_one = self.wait.until(EC.staleness_of(elem_table))
                if i != 2:
                    wait_two = self.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '#order_confirmation-wrapper > table')))
                if (wait_one and wait_two):
                    print('removed')
                else:
                    print('remove error')
            if self.driver.find_element_by_tag_name('em').text == 'There are no items in your cart.':
                print('Completed')
        except NoSuchElementException as e:
            print('no select', e)
        except TimeoutError as e:
            print('error', e)


if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(two)
    unittest.TextTestRunner(verbosity=2).run(suite)
