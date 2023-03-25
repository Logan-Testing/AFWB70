from selenium.webdriver.common.by import By

class LoginPage:
    __username=(By.ID,"username")
    __password=(By.NAME,"pwd")
    __loginbutton=(By.ID,"loginButton")

    def __init__(self,driver):
        self.__driver=driver

    def set_username(self,un):
        self.__driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        self.__driver.find_element(*self.__password).send_keys(pw)

    def click_loginbutton(self):
        self.__driver.find_element(*self.__loginbutton).click()



