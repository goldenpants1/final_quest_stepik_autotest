import math
from .locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def is_elemnt_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except(NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            return False
        return True

    def is_not_element_present(self, method, css_selector, timeout=4): #упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, css_selector, timeout=4): #будет ждать до тех пор, пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
    def should_be_login_link(self):
        assert self.is_elemnt_present(*BasePageLocators.LOGIN_LINK), "login link is not presented"
        #Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.

    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_authorized_user(self):
        assert self.is_elemnt_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"