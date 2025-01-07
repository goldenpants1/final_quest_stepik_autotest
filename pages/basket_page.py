from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

    def empty_basket(self):
        empty = self.is_elemnt_present(*BasketLocators.ITEM_BASKET)
        assert empty == False, "корзина не пуста"

    def message_empty_basket(self):
        empty = self.is_elemnt_present(*BasketLocators.EMPTY_BASKET)
        assert empty == True, "надпись о пустоте корзины отсутствует"