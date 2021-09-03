from PageObjects.HomePage import HomePage
from utilities.BaseClass import BassClass


class TestOne(BassClass):
    def test_e2e(self):

        log = self.get_logger()
        log.info('Clicking Shop')
        homepage = HomePage(self.driver)
        checkout_page = homepage.shop_items()

        log.info("Selecting Item")
        checkout_page.get_add_button().click()
        checkout_page.get_checkout_button().click()
        log.info("clicking Checkout")
        confirm_page = checkout_page.get_checkout_success()

        log.info("Entering Country name")
        confirm_page.get_country().send_keys('Ind')
        self.verify_link('India')
        confirm_page.get_click_country().click()
        confirm_page.get_checkbox().click()
        confirm_page.get_purchase_button().click()
        log.info("Capturing Success message")
        success_text = confirm_page.get_success_alert().text
        log.info(f"Text from after purchasing {success_text}")

        assert "Success! Thank you!" in success_text
