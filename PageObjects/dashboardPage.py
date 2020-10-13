from PageObjects.basePage import BasePage
from ElementsLocators.locators import DashboardPageLocators


class DashboardPage(BasePage):

    def check_header(self):
        dashboard_header = self.driver.find_element(*DashboardPageLocators.dashboard_header)
        return dashboard_header.text
