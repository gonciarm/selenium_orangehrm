import unittest
from PageObjects.loginPage import LoginPage
from PageObjects.dashboardPage import DashboardPage
from selenium import webdriver
from Utilities.readProperties import ReadConfig
from Utilities.timeStamp import TimeStamp
from Utilities.randomData import StringGenerator


class OrangeHRMLogin(unittest.TestCase):
    chrome_driver_path = ReadConfig.getChromeDriverPath()
    url = ReadConfig.getUrl()
    username = ReadConfig.getUsername()  # correct username
    password = ReadConfig.getPassword()  # correct password
    time_stamp = TimeStamp.dateTime()  # current date and time
    username_length = 8
    password_length = 8

    def setUp(self):
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get(self.url)

    # def test_invalid_username(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.set_username(StringGenerator.generateString(self.username_length))
    #     login_page.set_password(self.password)
    #     login_page.click_login_btn()
    #     self.assertEqual('Invalid credentials', login_page.invalid_credentials())
    #     self.driver.save_screenshot(f'../Screenshots/test_invalid_username{self.time_stamp}.png')
    #
    # def test_invalid_password(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.set_username(self.username)
    #     login_page.set_password(StringGenerator.generateString(self.password_length))
    #     login_page.click_login_btn()
    #     self.assertEqual('Invalid credentials', login_page.invalid_credentials())
    #     self.driver.save_screenshot(f'../Screenshots/test_invalid_password{self.time_stamp}.png')
    #
    # def test_invalid_credentials(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.set_username(StringGenerator.generateString(self.username_length))
    #     login_page.set_password(StringGenerator.generateString(self.password_length))
    #     login_page.click_login_btn()
    #     self.assertEqual('Invalid credentials', login_page.invalid_credentials())
    #     self.driver.save_screenshot(f'../Screenshots/test_invalid_password{self.time_stamp}.png')

    def test_correct_login(self):
        login_page = LoginPage(self.driver)
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.click_login_btn()
        dashboard_page = DashboardPage(self.driver)
        self.assertEqual('Dashboard', dashboard_page.check_header())
        self.driver.save_screenshot(f'../Screenshots/test_correct_login{self.time_stamp}.png')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__=="__main__":
    unittest.main()
