from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    Add_button = (By.XPATH, '//a[text()="Blackberry"]/parent::h4/parent::div/parent::div//button[@class="btn btn-info"]')
    Checkout_button = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')
    Checkout_success = (By.XPATH, '//button[@class="btn btn-success"]')

    def __init__(self, driver):
        self.driver = driver

    def get_add_button(self):
        return self.driver.find_element(*CheckoutPage.Add_button)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.Checkout_button)

    def get_checkout_success(self):
        self.driver.find_element(*CheckoutPage.Checkout_success).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
