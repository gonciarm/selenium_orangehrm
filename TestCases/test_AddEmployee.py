import HtmlTestRunner
import unittest
from PageObjects.loginPage import LoginPage
from PageObjects.commonObjects import MainMenu
from PageObjects.commonObjects import PimMenu
from PageObjects.AddEmployeePage import AddEmployee
from PageObjects.ViewEmployeePage import ViewEmployee
from selenium import webdriver
from Utilities.readProperties import ReadConfig
from Utilities.timeStamp import TimeStamp
from Utilities.randomData import StringGenerator
from Utilities.randomData import NumberGenerator
import time


class OrangeHRMaddEmployee(unittest.TestCase):
    chrome_driver_path = ReadConfig.getChromeDriverPath()
    url = ReadConfig.getUrl()
    username = ReadConfig.getUsername()  # correct username
    password = ReadConfig.getPassword()  # correct password
    time_stamp = TimeStamp.dateTime()  # current date and time

    first_name = StringGenerator.generateString(6)
    middle_name = StringGenerator.generateString(6)
    last_name = StringGenerator.generateString(6)
    employee_id = NumberGenerator.generateNumber(5)

    def setUp(self):
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get(self.url)

    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()

    def test_add_employee(self):
        # Login action
        login_page = LoginPage(self.driver)
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.click_login_btn()

        # Click on PIM link in main menu
        main_menu = MainMenu(self.driver)
        main_menu.click_pim()
        time.sleep(0.5)  # need to use sleep due to issue on the web page

        # Click on Add Employee element in submenu
        pim_menu = PimMenu(self.driver)
        pim_menu.click_add_employee()

        # Add Employee h1 verification
        add_employee_page = AddEmployee(self.driver)
        self.assertEqual('Add Employee', add_employee_page.is_header_visible())

        # Adding employee
        add_employee_page.set_first_name(self.first_name)
        add_employee_page.set_middle_name(self.middle_name)
        add_employee_page.set_last_name(self.last_name)
        add_employee_page.set_employee_id(self.employee_id)
        add_employee_page.click_save()
        time.sleep(2)

        # Check on employee details if user h1 is equal to full name (in this case to combined: first name, middle name, last name)
        view_employee_page = ViewEmployee(self.driver)
        self.assertEqual(f'{self.first_name} {self.middle_name} {self.last_name}', view_employee_page.user_header_visible())


if __name__=='__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
    unittest.main()
