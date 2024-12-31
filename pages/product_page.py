from .base_page import BasePage
from .locators import ShopPage

class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ShopPage.ADD_TO_BASKET)
        add_to_basket.click()

    def price(self, price_product):
        price_basket = self.browser.find_element(*ShopPage.BASKET_PRICE).text
        assert price_product == price_basket, "цена товара не совпадает с ценой корзины"

    def product_name(self, name_product):
        basket_product_name = self.browser.find_element(*ShopPage.BASKET_NAME_PRODUCT).text
        assert name_product == basket_product_name, "Название товара в корзине не совпадает с добавляемым"