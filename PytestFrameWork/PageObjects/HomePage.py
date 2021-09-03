from selenium.webdriver.common.by import By
from PageObjects.CheckOutPage import CheckoutPage


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radiobutton = (By.XPATH, "//input[@id='inlineRadio1']")
    birt_date = (By.NAME, "bday")
    submit_button = (By.XPATH, '//input[@class="btn btn-success"]')
    alert_text = (By.CSS_SELECTOR, '[class*="alert-success "]')

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_radiobutton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def get_birthday(self):
        return self.driver.find_element(*HomePage.birt_date)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_alert_text(self):
        return self.driver.find_element(*HomePage.alert_text)
