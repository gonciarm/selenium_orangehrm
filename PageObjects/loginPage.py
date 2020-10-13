from PageObjects.basePage import BasePage
from ElementsLocators.locators import LoginPageLocators


class LoginPage(BasePage):

    def set_username(self, value):
        username = self.driver.find_element(*LoginPageLocators.user_name)
        username.clear()
        username.send_keys(value)

    def set_password(self, value):
        password = self.driver.find_element(*LoginPageLocators.password)
        password.clear()
        password.send_keys(value)

    def click_login_btn(self):
        login = self.driver.find_element(*LoginPageLocators.login_btn)
        login.click()

    def invalid_credentials(self):
        message = self.driver.find_element(*LoginPageLocators.invalid_message)
        return message.text