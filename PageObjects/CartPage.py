from selenium.webdriver.common.by import By


class Cartpagedetails:
    def __init__(self,driver):
        self.driver = driver
        self.Cart_Page_xpath = "//a[text()='Cart']"
        self.Click_Logout = "//a[text()='Log out']"


    def click_cart_option(self):
        return self.driver.find_element(By.XPATH, self.Cart_Page_xpath).click()


    def Click_On_Logout_btn(self):
        self.driver.find_element(By.XPATH, self.Click_Logout).click()

