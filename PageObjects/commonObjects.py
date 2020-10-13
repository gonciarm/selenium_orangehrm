from PageObjects.basePage import BasePage
from ElementsLocators.locators import MenuPim
from ElementsLocators.locators import MenuMain


class MainMenu(BasePage):

    def click_pim(self):
        main_menu_pim = self.wait.until(self.EC.presence_of_element_located(MenuMain.pim))
        main_menu_pim.click()


class PimMenu(BasePage):

    def click_add_employee(self):
        pim_menu_add_employee = self.wait.until(self.EC.element_to_be_clickable(MenuPim.add_employee))
        pim_menu_add_employee.click()

    def click_employee_list(self):
        pim_menu_employee_list = self.wait.until(self.EC.element_to_be_clickable(MenuPim.employee_list))
        pim_menu_employee_list.click()
