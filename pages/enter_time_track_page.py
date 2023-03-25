from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class EnterTimeTrackPage:
    __logout = (By.ID, "logoutLink")

    def __init__(self, driver):
        self.driver = driver

    def verify_home_page_is_displayed(self, wait: WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__logout))
            print("Home Page is Displayed")
            return True
        except:
            print("Home Page is Not Displayed")
            return False
