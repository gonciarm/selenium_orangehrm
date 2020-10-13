from PageObjects.basePage import BasePage
from ElementsLocators.locators import AddEmployeePage


class AddEmployee(BasePage):

    def is_header_visible(self):
        add_employee_h1 = self.wait.until(self.EC.presence_of_element_located(AddEmployeePage.add_employee_header))
        return add_employee_h1.text

    def set_first_name(self, value):
        first_name = self.driver.find_element(*AddEmployeePage.firstname_input)
        first_name.clear()
        first_name.send_keys(value)

    def set_middle_name(self, value):
        middle_name = self.driver.find_element(*AddEmployeePage.middle_name_input)
        middle_name.clear()
        middle_name.send_keys(value)

    def set_last_name(self, value):
        last_name = self.driver.find_element(*AddEmployeePage.last_name_input)
        last_name.clear()
        last_name.send_keys(value)

    def set_employee_id(self, value):
        employee_id = self.driver.find_element(*AddEmployeePage.employee_id_input)
        employee_id.clear()
        employee_id.send_keys(value)

    def click_save(self):
        employee_id = self.driver.find_element(*AddEmployeePage.save_btn)
        employee_id.click()
