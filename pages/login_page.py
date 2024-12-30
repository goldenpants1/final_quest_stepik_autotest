from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/" in self.browser.current_url, "кнопка 'войти' увела не туда"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_elemnt_present(*LoginPageLocators.LOGIN_FORM), "форма логина не найдена"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_elemnt_present(*LoginPageLocators.REGISTRATION_FORM), "форма регистрации не найдена"
        # реализуйте проверку, что есть форма регистрации на странице