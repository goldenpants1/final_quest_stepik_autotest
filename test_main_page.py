import pytest
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    loginPage = LoginPage(browser, browser.current_url)
    loginPage.should_be_login_page()


def test_quest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.basket #pytest -s -m "basket" test_main_page.py
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket()
    basket_page.message_empty_basket()