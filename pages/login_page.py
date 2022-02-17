from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login not in url"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*BasePageLocators.USER_EMAIL)
        email_form.send_keys(email)
        password_form1 = self.browser.find_element(*BasePageLocators.USER_PASSWORD1)
        password_form1.send_keys(password)
        password_form2 = self.browser.find_element(*BasePageLocators.USER_PASSWORD2)
        password_form2.send_keys(password)
        reg_btn = self.browser.find_element(*BasePageLocators.REG_BTN)
        reg_btn.click()
