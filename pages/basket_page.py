from .base_page import BasePage
from .locators import BasketPageLocators

class BasektPage(BasePage):
    def should_be_basket_empty_text(self):
        print(self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text)
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text, "Text about empty basket is not presented"

    def basket_has_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "Basket has some products, but shoud not"
