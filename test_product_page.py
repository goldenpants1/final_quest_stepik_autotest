from .pages.product_page import ProductPage
from .pages.locators import ShopPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    price_product = page.browser.find_element(*ShopPage.PRICE).text
    name_product = page.browser.find_element(*ShopPage.NAME_PRODUCT).text
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.price(price_product=price_product)
    page.product_name(name_product=name_product)

