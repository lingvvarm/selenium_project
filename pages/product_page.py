from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CHART), "Add to basket button not presented"

    def should_be_name_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT), "Name of product don't found"

    def should_be_price_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "Product Price not found"

    def should_be_msg_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        print(product_name)
        print(message)
        assert message == f"{product_name} has been added to your basket.", "Product name not found on message"

    def compare_basket_and_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Product price and basket price is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"

    def add_product_to_basket(self):
        self.should_be_name_of_product()
        self.should_be_price_of_product()
        self.should_be_add_to_basket_button()
        self.should_not_be_success_message()
        self.should_disappear_success_message()

        add_to_busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CHART)
        add_to_busket_button.click()

        #self.solve_quiz_and_get_code()
        self.should_be_msg_about_adding()
        self.compare_basket_and_product_price()

    