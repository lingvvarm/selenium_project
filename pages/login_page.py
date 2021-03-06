from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_NAME), "Login name is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_NAME), "Registration name is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), "Registration password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_REP_PASSWORD), "Registration repeat password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Registration button is not presented"

    def register_new_user(self, email, password):
        email_web = self.browser.find_element(*LoginPageLocators.REG_NAME)
        password_web = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        rep_password_web = self.browser.find_element(*LoginPageLocators.REG_REP_PASSWORD)
        button_web = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        email_web.send_keys(email)
        password_web.send_keys(password)
        rep_password_web.send_keys(password)
        button_web.click()
        