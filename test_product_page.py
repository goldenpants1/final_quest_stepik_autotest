import pytest
from .pages.product_page import ProductPage
from .pages.locators import ShopPage

@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", "8", "9", pytest.param("7", marks=pytest.mark.xfail)                                         ])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    price_product = page.browser.find_element(*ShopPage.PRICE).text
    name_product = page.browser.find_element(*ShopPage.NAME_PRODUCT).text
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.price(price_product=price_product)
    page.product_name(name_product=name_product)

