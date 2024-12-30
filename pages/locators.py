from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")#Кнопка "Войти или зарегистрироваться"

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