import pytest
import time
from .pages.product_page import ProductPage
from .pages.locators import ShopPageLocators
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.usertest
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        self.password = "testing_password_1234"
        self.email = str(time.time()) + "@fakemail.org"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        self.page.register_new_user(email=self.email, password=self.password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        price_product = page.browser.find_element(*ShopPageLocators.PRICE).text
        name_product = page.browser.find_element(*ShopPageLocators.NAME_PRODUCT).text
        page.add_to_basket()
        page.price(price_product=price_product)
        page.product_name(name_product=name_product)

    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ShopPageLocators.SUCCESS_MESSAGE)
        page.should_not_be_success_message()

#@pytest.mark.skip
@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", "8", "9", pytest.param("7", marks=pytest.mark.xfail)                                         ])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    price_product = page.browser.find_element(*ShopPageLocators.PRICE).text
    name_product = page.browser.find_element(*ShopPageLocators.NAME_PRODUCT).text
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.price(price_product=price_product)
    page.product_name(name_product=name_product)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_not_element_present(*ShopPageLocators.SUCCESS_MESSAGE)
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ShopPageLocators.SUCCESS_MESSAGE)
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_disappeared(*ShopPageLocators.SUCCESS_MESSAGE)
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/cataloge/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/cataloge/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
@pytest.mark.need_review  #pytest -s -m "need_review" test_product_page.py
@pytest.mark.basket    #pytest -s -m "basket" test_product_page.py
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket()
    basket_page.message_empty_basket()
