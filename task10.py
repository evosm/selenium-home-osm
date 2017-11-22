import unittest, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class test_two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart"

    def test_10_a(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            campaings = driver.find_element_by_id('box-campaigns')
            product = campaings.find_element_by_css_selector('a.link')
            main_page_product_text = product.get_attribute('title')
            product.click()
            page_product_text = driver.find_element_by_tag_name('h1').text
            if page_product_text == main_page_product_text:
                print('a yes')
            else:print('a no')
        except NoSuchElementException as e:
            print('error:', e)

    def test_10_b(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            campaings = driver.find_element_by_id('box-campaigns')
            product = campaings.find_element_by_css_selector('a.link')
            main_page_product_regular_price = product.find_element_by_css_selector('s.regular-price').text
            main_page_product_sale_price = product.find_element_by_css_selector('strong.campaign-price').text
            product.click()
            page_product_regular = driver.find_element_by_css_selector('s.regular-price').text
            page_product_sale = driver.find_element_by_css_selector('strong.campaign-price').text
            if page_product_regular == main_page_product_regular_price and page_product_sale == main_page_product_sale_price:
                print('b yes')
            else:print('b no')
        except NoSuchElementException as e:
            print('error:', e)

    def test_10_c(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            campaings = driver.find_element_by_id('box-campaigns')
            product = campaings.find_element_by_css_selector('a.link')
            main_page_product_regular_color = product.find_element_by_css_selector('s.regular-price').value_of_css_property('color')
            main_page_product_regular_color = main_page_product_regular_color.replace('rgba(','')
            main_page_product_regular_color = main_page_product_regular_color.replace(', 1)','')
            main_page_product_regular_color = main_page_product_regular_color.replace(' ','').split(',')
            main_page_product_regular_line = product.find_element_by_css_selector('s.regular-price').value_of_css_property('text-decoration')
            product.click()
            page_product_regular_color = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('color')
            page_product_regular_color = page_product_regular_color.replace('rgba(', '')
            page_product_regular_color = page_product_regular_color.replace(', 1)', '')
            page_product_regular_color = page_product_regular_color.replace(' ', '').split(',')
            page_product_regular_line = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('text-decoration')
            if len(set(main_page_product_regular_color)) == 1 and \
                    ('line' in main_page_product_regular_line) and \
                    len(set(page_product_regular_color)) == 1 and \
                    ('line' in page_product_regular_line):
                print('yes price color  = grey and contains line. tested at all page')
            else:print('c fail')
        except NoSuchElementException as e:
            print('error:', e)

    def test_10_d(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            campaings = driver.find_element_by_id('box-campaigns')
            product = campaings.find_element_by_css_selector('a.link')
            main_page_product_price_color = product.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')
            main_page_product_price_color = main_page_product_price_color.replace('rgba(','')
            main_page_product_price_color = main_page_product_price_color.replace(', 1)','')
            main_page_product_price_color = main_page_product_price_color.replace(' ','').split(',')
            main_page_product_price_bold = product.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight')
            product.click()
            page_product_price_color = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')
            page_product_price_color = page_product_price_color.replace('rgba(', '')
            page_product_price_color = page_product_price_color.replace(', 1)', '')
            page_product_price_color = page_product_price_color.replace(' ', '').split(',')
            page_product_price_bold = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight')
            if (main_page_product_price_color[1] == '0' and
                main_page_product_price_color[2] == '0' and
                int(main_page_product_price_bold) >= 700 and
                page_product_price_color[1] == '0' and
                page_product_price_color[2] == '0' and
                int(page_product_price_bold) >= 700 ):
                print('d yes price color =  RED  and price text is bold. tested at all page')
            else:print('d fail ')
        except NoSuchElementException as e:
            print('error:', e)

    def test_10_e(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            campaings = driver.find_element_by_id('box-campaigns')
            product = campaings.find_element_by_css_selector('a.link')
            main_page_product_regular_size = product.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size').replace('px', '')
            main_page_product_sale_size = product.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size').replace('px','')
            product.click()
            page_product_regular_size = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size').replace('px', '')
            page_product_sale_size = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size').replace('px','')
            if (float(main_page_product_regular_size) < float(main_page_product_sale_size) and
                float(page_product_regular_size) < float(page_product_sale_size)):
                print('sale price text size bigger')
            else:print('e fail ')
        except NoSuchElementException as e:
            print('error:', e)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_two)
    unittest.TextTestRunner(verbosity=2).run(suite)
