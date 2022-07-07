from sre_constants import SUCCESS
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_NAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REG_NAME = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_REP_PASSWORD = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CHART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, '.alertinner')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.ID, "content_inner")
    BASKET_PRODUCTS = (By.ID, "basket_formset")