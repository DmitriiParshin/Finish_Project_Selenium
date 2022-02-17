from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_good(self):
        assert self.is_not_element_present(*BasePageLocators.GOOD_NOT), \
            "Success message is presented, but should not be"

    def should_be_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY), \
            "Success message is presented, but should not be"
