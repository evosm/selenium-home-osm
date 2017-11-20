import unittest, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class test_two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Safari()
        self.base_url = "http://localhost/litecart/admin/"

    def test_9_1(self):
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
            table = driver.find_element_by_id('content')
            rows_list = table.find_elements_by_css_selector('tr.row')
            country_list = []
            sorted_country_list =[]
            country_zones = {}
            for row in rows_list:
                country = row.find_element_by_xpath("./td[5]").text
                zones = row.find_element_by_xpath("./td[6]").text
                country_list.append(country)
                sorted_country_list.append(country)
                if int(zones) != 0:
                    country_zones[country] = int(zones)
            sorted_country_list.sort()
            if country_list == sorted_country_list:
                print('True! Country list true')
            else:
                print('False! Country list false')
            for row in rows_list:
                country = row.find_element_by_xpath("./td[5]")
                if country.text in country_zones:
                    zones_link = row.find_element_by_css_selector('td:nth-child(5) > a')
                    zones_link.send_keys(Keys.COMMAND + Keys.RETURN)
                    windows = driver.window_handles
                    driver.switch_to_window(windows[1])
                    country_zones_list = []
                    sorted_zones_country_list = []
                    zones_table = driver.find_element_by_id('table-zones')
                    rows_zones_list = zones_table.find_elements_by_tag_name('tr')
                    for row_zone in rows_zones_list:
                        zones_text_list = row_zone.find_elements_by_tag_name('td')
                        if len(zones_text_list) !=0 and zones_text_list[2].text != '' :
                            country_zones_list.append(zones_text_list[2].text)
                            sorted_zones_country_list.append(zones_text_list[2].text)
                    sorted_zones_country_list.sort()
                    if sorted_zones_country_list == country_zones_list:
                        print('True! Zones Country list true')
                    else:
                        print('False! Zones Country list false')
                    driver.close()
                    driver.switch_to_window(windows[0])

        except NoSuchElementException as e:
            print('error:', e)
            self.fail(r'element error')

    def test_9_2(self):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            driver.get(self.base_url)
            user_name_elem = driver.find_element_by_xpath("//*[@type='text']")
            user_name_elem.send_keys('admin')
            user_pass_elem = driver.find_element_by_name('password')
            user_pass_elem.send_keys('admin')
            driver.find_element_by_xpath("//*[@type='submit']").click()
            driver.find_element_by_xpath("//*[@href='http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones']").click()
            table = driver.find_element_by_css_selector('#content > form > table')
            rows_list = table.find_elements_by_css_selector('tr.row')
            for row in rows_list:
                country = row.find_element_by_css_selector('td:nth-child(3) > a')
                country.send_keys(Keys.COMMAND + Keys.RETURN)
                windows = driver.window_handles
                driver.switch_to_window(windows[1])
                zones_table = driver.find_element_by_id('table-zones')
                zones_rows = zones_table.find_elements_by_css_selector('tr')
                list_of_zones = []
                sorted_list_of_zones = []
                for zone_row in zones_rows:
                    zone = zone_row.find_elements_by_tag_name('td')
                    if len(zone) >= 2:
                        tmp = zone[2].find_element_by_tag_name('select')
                        select = Select(tmp)
                        selected_option = select.first_selected_option
                        if selected_option.text !='':
                            list_of_zones.append(selected_option.text)
                            sorted_list_of_zones.append(selected_option.text)
                sorted_list_of_zones.sort()
                if sorted_list_of_zones == list_of_zones:
                    print('YES')
                else:
                    print('NO')
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
