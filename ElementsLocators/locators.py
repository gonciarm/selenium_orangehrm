from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    user_name = (By.ID, 'txtUsername')
    password = (By.ID, 'txtPassword')
    login_btn = (By.ID, 'btnLogin')
    invalid_message = (By.ID, 'spanMessage')


class DashboardPageLocators(object):
    dashboard_header = (By.TAG_NAME, 'h1')


class MenuMain(object):
    admin = (By.ID, 'menu_admin_viewAdminModule')
    pim = (By.ID, 'menu_pim_viewPimModule')
    leve = (By.ID, 'menu_leave_viewLeaveModule')
    time = (By.ID, 'menu_time_viewTimeModule')
    recruitment = (By.ID, 'menu_recruitment_viewRecruitmentModule')
    my_info = (By.ID, 'menu_pim_viewMyDetails')
    performance = (By.ID, 'menu__Performance')
    dashboard = (By.ID, 'menu_dashboard_index')
    directory = (By.ID, 'menu_directory_viewDirectory')
    maintenance = (By.ID, 'menu_maintenance_purgeEmployee')
    buzz = (By.ID, 'menu_buzz_viewBuzz')


class MenuPim(object):
    employee_list = (By.ID, 'menu_pim_viewEmployeeList')
    add_employee = (By.ID, 'menu_pim_addEmployee')


class AddEmployeePage(object):
    add_employee_header = (By.XPATH, '//h1[contains(text(),\'Add Employee\')]')
    firstname_input = (By.ID, 'firstName')
    middle_name_input = (By.ID, 'middleName')
    last_name_input = (By.ID, 'lastName')
    employee_id_input = (By.ID, 'employeeId')
    create_login_details_radio = (By.XPATH, '//input[@id=\'chkLogin\']')
    save_btn = (By.ID, 'btnSave')


class ViewEmployeePage(object):
    user_header = (By.XPATH, '/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/h1[1]')
