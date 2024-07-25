import time

import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.CartPage import Cartpagedetails
from Utilities.logger import logclass

@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_001(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        cp = Cartpagedetails(self.driver)
        time.sleep(5)
        lg.Click_Login()
        log.info("TEST CASE 001")
        log.info("test case starting")
        time.sleep(5)
        lg.input_username("Aditya0927")
        log.info("entered username")
        lg.input_Password("0927")
        log.info("entered Password")
        lg.Click_on_login_btn()
        log.info("Click on Login Button")
        time.sleep(5)
        lg.Click_on_Catagories()
        log.info("Verify Catagories")
        time.sleep(5)
        lg.Click_nxt()
        log.info("Click on Next Button")
        time.sleep(5)
        lg.Click_last_product()
        log.info("Select last product")
        time.sleep(3)
        lg.Click_On_add_tocart()
        log.info("click on add product to the cart")
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(4)
        cp.click_cart_option()
        time.sleep(5)
        if 'MacBook Pro' in self.driver.find_element(By.XPATH, "//td[normalize-space()='MacBook Pro']").text:
            assert True
            print("Product Successfully added to cart")
            log.info("Product added Successfully to the cart")
        else:
            print("Product not added to cart")
            assert False
        time.sleep(5)
        cp.Click_On_Logout_btn()
        log.info("Click on Logout Button")
        time.sleep(3)
