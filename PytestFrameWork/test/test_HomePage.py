import pytest


from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BassClass


class TestHomePage(BassClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        # log.info("First name is "+get_data["firstname"])

        homepage = HomePage(self.driver)
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys(get_data["email"])
        homepage.get_password().send_keys(get_data["password"])
        homepage.get_checkbox().click()
        self.select_option(homepage.get_dropdown(), get_data["gender"])
        homepage.get_radiobutton().click()
        homepage.get_birthday().send_keys(get_data["Birth Date"])
        homepage.get_submit_button().click()
        alert_text = homepage.get_alert_text().text

        assert " The Form has been submitted successfully!." in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("TestCase1", "TestCase2"))
    def get_data(self, request):
        return request.param
