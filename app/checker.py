import settings
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#
class Checker():

    def __init__(self, name):
        self.name = name
        if settings.DEBUG:
            self.driver = webdriver.Chrome(
                executable_path='/home/carlos/Documents/registro-entrada/auto-checker/app/drivers/chromedriver'
            )
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--window-size=1920x1080')
            self.driver = webdriver.Chrome(options=options)
    
    def _wait_until(self, query, by=By.CSS_SELECTOR, until=EC.element_to_be_clickable):
        """generic wait until class with default csss selector and
        element to be clickable"""
        element = WebDriverWait(self.driver, 30).until(
            until((by, query))
        )
        return element

    def _login(self):
        EMAIL = settings.USERS[self.name][0]
        PASSWORD = settings.USERS[self.name][1]
        self.driver.get('https://onesofttek.sharepoint.com/sites/home/SitePages/Menu.aspx')
        email_input  = self._wait_until("input[type='email']")
        email_input.clear()
        email_input.send_keys(EMAIL)
        next_button = self.driver.find_element_by_css_selector("input[type='submit']#idSIButton9")
        next_button.click()
        password_input = self._wait_until('#i0118')
        password_input.clear()
        password_input.send_keys(PASSWORD)
        # We find it again because it raises an ElementNotAttached exception
        next_button = self.driver.find_element_by_css_selector("input[type='submit']#idSIButton9")
        next_button.click()
        no_keep_session_buttonn = self._wait_until('#idBtn_Back')
        no_keep_session_buttonn.click()
        pass

    def _click_on_checkin_out_button(self):
        clock_check_io_button = self._wait_until('button.checkButton.leave')
        clock_check_io_button.click()

    def check_in(self):
        """Method for check in"""
        self._login()
        self._click_on_checkin_out_button()
        arrival_button = self._wait_until('button.checkButton.arrival')
        time.sleep(3)
        arrival_button.click()
        time.sleep(2)
        self.driver.quit()

    def check_out(self):
        """Method for leaving"""
        self._login()
        self._click_on_checkin_out_button()
        check_out_button = self._wait_until('button.leave')
        time.sleep(3)
        check_out_button.click()
        self._click_on_checkin_out_button()
        self.driver.quit()


if __name__ == '__main__':
    try:
        name = str(sys.argv[2])
        checking_type = str(sys.argv[1])
    except:
        name = 'mochis'
        checking_type = 'check_in'

    checker = Checker(name=name)
    if checking_type == 'check_in':
        checker.check_in()
    elif checking_type == 'check_out':
        checker.check_out()
