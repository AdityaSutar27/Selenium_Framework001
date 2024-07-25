from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.driver = driver

        self.Click_Login_xpath = "//a[@id='login2']"
        self.textbox_username_xpath = "//input[@id='loginusername']"
        self.textbox_password_xpath = "//input[@id='loginpassword']"
        self.button_login_xpath = "//button[@onclick='logIn()']"
        self.Catagories_xpath = "//a[text()='CATEGORIES']"
        self.Click_on_next_Btn = "//button[text()='Next']"
        self.Click_on_Last_Product = "//a[text()='MacBook Pro']"
        self.Click_on_addtocart = "//a[text()='Add to cart']"

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.Click_Login_xpath).click()

    def input_username(self,Username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(Username)

    def input_Password(self,Password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(Password)

    def Click_on_login_btn(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def Click_on_Catagories(self):
        return self.driver.find_element(By.XPATH, self.Catagories_xpath).click()

    def Click_nxt(self):
        return self.driver.find_element(By.XPATH, self.Click_on_next_Btn).click()

    def Click_last_product(self):
        return self.driver.find_element(By.XPATH, self.Click_on_Last_Product).click()

    def Click_On_add_tocart(self):
        return self.driver.find_element(By.XPATH, self.Click_on_addtocart).click()


