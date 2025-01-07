from .base_page import BasePage
from .locators import Basket

class BasketPage(BasePage):

    def empty_basket(self):
        empty = self.is_elemnt_present(*Basket.ITEM_BASKET)
        assert empty == False, "корзина не пуста"

    def message_empty_basket(self):
        empty = self.is_elemnt_present(*Basket.EMPTY_BASKET)
        assert empty == True, "надпись о пустоте корзины отсутствует"