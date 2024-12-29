import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_have_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    buttonBasket = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form>button")
    assert len(buttonBasket) > 0, "Кнопка добавления в корзину не найдена..."


