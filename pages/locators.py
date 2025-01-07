from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')#сама форма логина
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")# сама форма регистрации
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")# инпут адреса электронной почты для логина
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")# инпут пароля для логина
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")# инпут адреса электронной почты для регистрации
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")# инпут пароля для регистрации
    REG_RETURN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")# инпут "повторите пароль" при регистрации
    ENTER_BUTTON = (By.CSS_SELECTOR, "#login_form>button")# кнопка "Войти"
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form>button")# кнопка "Зарегистрироваться"
    REMEMBER_PASS_BUTTON = (By.CSS_SELECTOR, "#login_form>p>a")# кнопка "Я забыл пароль"

class ShopPage():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form>button")#кнопка "добавить в корзину"
    PRICE = (By.XPATH, "(//p[@class='price_color'])[1]")# цена товара
    BASKET_PRICE = (By.XPATH, "(//div[@class='alertinner ']//strong)[3]") # сумма в корзине
    BASKET_NAME_PRODUCT = (By.XPATH, "(//div[@class='alertinner ']//strong)[1]") # название товара, добавленного в корзину
    NAME_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1[1]")# название товара
    SUCCESS_MESSAGE = (By.XPATH, "(//div[contains(@class,'alert alert-safe')])[1]")# сообщение об успешном добавлении в корзину

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #Кнопка "Войти или зарегистрироваться"
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")  # Кнопка перехода в коризну

class Basket():
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner>p123")#Надпись "ваша корзина пуста"
    ITEM_BASKET = (By.CSS_SELECTOR, ".basket-items")#Блок товара в коризине