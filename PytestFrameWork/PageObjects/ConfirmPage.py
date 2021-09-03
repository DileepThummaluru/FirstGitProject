from selenium.webdriver.common.by import By


class ConfirmPage:
    country = (By.ID, "country")
    click_country = (By.LINK_TEXT, 'India')
    checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    purchase_button = (By.XPATH, '//input[@class="btn btn-success btn-lg"]')
    success_alert = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def get_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def get_click_country(self):
        return self.driver.find_element(*ConfirmPage.click_country)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_success_alert(self):
        return self.driver.find_element(*ConfirmPage.success_alert)
