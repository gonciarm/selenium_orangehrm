from PageObjects.basePage import BasePage
from ElementsLocators.locators import ViewEmployeePage


class ViewEmployee(BasePage):

    def user_header_visible(self):
        view_employee_user_header = self.wait.until(self.EC.presence_of_element_located(ViewEmployeePage.user_header))
        return view_employee_user_header.text
