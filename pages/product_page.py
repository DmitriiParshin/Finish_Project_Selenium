from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET)
        btn.click()

    def examination_name_book(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK).text == \
               self.browser.find_element(By.CSS_SELECTOR, "#messages strong").text, "Bad name"

    def examination_price_book(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == \
               self.browser.find_element(By.CSS_SELECTOR, ".alert-info p strong").text, "Bad price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should disappeared"
