import time
import pytest
from PageObjects.LoginPage import Login
from selenium.webdriver.common.by import By
from Utilities.logger import logclass

@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_001(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        from selenium.webdriver.common.by import By
        time.sleep(5)
        lg.Click_Login()
        log.info("TEST CASE 001")
        log.info("test case staring")
        time.sleep(5)
        lg.input_username("Aditya0927")
        log.info("entered Username")
        lg.input_Password("0927")
        log.info("entered Password")
        lg.Click_on_login_btn()
        log.info("Click on Login button")
        time.sleep(5)
        if 'Welcome Aditya0927' in self.driver.find_element(By.XPATH, "//a[text()='Welcome Aditya0927']").text:
            assert True
            print("Login Successful")
            log.info("Login Successful")
        else:
            print("Login Fail")
            log.info("Login Fail")
            assert False

    def test_002(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        time.sleep(5)
        lg.Click_Login()
        log.info("TEST CASE 002")
        log.info("test case staring")
        time.sleep(5)
        lg.input_username("Aditya0927")
        log.info("entered Username")
        lg.input_Password("1000")
        log.info("entered incorrect Password")
        lg.Click_on_login_btn()
        log.info("Click on Login button")
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        if 'Log in' in self.driver.find_element(By.XPATH, "//button[text()='Log in']").text:
            assert True
            print("Login Fail")
            log.info("Login Fail")
        else:
            print("login Successful")
            log.info("Login Successful")
            assert False

    def test_003(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        time.sleep(5)
        lg.Click_Login()
        log.info("TEST CASE 003")
        log.info("test case staring")
        time.sleep(5)
        lg.input_username("0927")
        log.info("entered incorrect Username")
        lg.input_Password("1000")
        log.info("entered incorrect Password")
        lg.Click_on_login_btn()
        log.info("Click on Login button")
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        if 'Log in' in self.driver.find_element(By.XPATH, "//button[text()='Log in']").text:
            assert True
            print("Login Fail")
            log.info("Login Fail")
        else:
            print("login Successful")
            log.info("Login Successful")
            assert False

