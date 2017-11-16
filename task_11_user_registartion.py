import unittest, time, random

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

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
            driver.find_element_by_css_selector('#box-account-login > div > form > table > tbody > tr:nth-child(5) > td > a').click()
            user_firstname_elem = driver.find_element_by_name('firstname')
            user_firstname_elem.send_keys('test_username_'+ str(random.randint(0,10)))
            user_lastname_elem = driver.find_element_by_name('lastname')
            user_lastname_elem.send_keys('test_lastname_' + str(random.randint(0, 10)))
            user_address_elem = driver.find_element_by_name('address1')
            user_address_elem.send_keys('address' + str(random.randint(0, 10)))
            user_postcode_elem = driver.find_element_by_name('postcode')
            user_postcode_elem.send_keys(str(random.randint(10000, 100000)))
            user_city_elem = driver.find_element_by_name('city')
            user_city_elem.send_keys('city' + str(random.randint(0, 10)))
            driver.find_element_by_xpath("//*[@class='select2-selection__arrow']").click()
            country =  driver.find_element_by_xpath("//*[@class='select2-results']")
            for elem  in country.find_elements_by_tag_name('li'):
                if elem.text == 'United States':
                    elem.click()
                    zones_country = driver.find_element_by_css_selector('#create-account > div > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
                    zone_list = zones_country.find_elements_by_tag_name('option')
                    cur_zone = zone_list[random.randint(0,len(zone_list) - 1)]
                    cur_zone.click()
                    break
            user_email_elem = driver.find_element_by_name('email')
            email = 'test' + str(random.randint(1000, 10000)) +'@test.ru'
            user_email_elem.send_keys(email)
            user_phone_elem = driver.find_element_by_name('phone')
            user_phone_elem.send_keys('+' + str(random.randint(0, 10)))
            user_pass_elem = driver.find_element_by_name('password')
            user_pass_elem.send_keys('passWord')
            user_confirmed_pass_elem = driver.find_element_by_name('confirmed_password')
            user_confirmed_pass_elem.send_keys('passWord')
            driver.find_element_by_name('create_account').click()
            driver.find_element_by_css_selector('#box-account > div > ul > li:nth-child(4) > a').click()
            login = driver.find_element_by_name('email')
            login.send_keys(email)
            password = driver.find_element_by_name('password')
            password.send_keys('passWord')
            driver.find_element_by_name('login').click()
            driver.find_element_by_css_selector('#box-account > div > ul > li:nth-child(4) > a').click()
        except NoSuchElementException as e:
            print('error:', e)
            self.fail(r'element error')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print('\nНачинаем тест\n')
    suite = unittest.TestLoader().loadTestsFromTestCase(test_two)
    unittest.TextTestRunner(verbosity=2).run(suite)
