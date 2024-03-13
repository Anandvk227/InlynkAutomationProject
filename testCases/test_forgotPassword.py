import time
import unittest

import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.forgotPassword_Page import forgotPasswordPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestForgotPassword(unittest.TestCase):
    baseURL = ReadConfig.getApplicationURL()
    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["I2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger = LogGen.loggen()

    def setUp(self):
        self.logger = LogGen.loggen()
        self.driver = webdriver.Chrome()  # Change to the appropriate driver
        self.driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.regression(order=1)
    def test_forgotPasswordValid(self):

        self.logger.info("***** TS_2	TC_01  Started Verify the Forgot Password Functionality Test*****")
        self.fp = forgotPasswordPage(self.driver)
        self.fp.clickforgotPassword()
        self.fp.setEmail(self.username)
        self.fp.clickSendButton()
        self.logger.info("TS_2 TC_01   Verify that a user can successfully request a password reset email.")
        # Execute JavaScript to open a new tab
        self.driver.execute_script("window.open('about:blank', '_blank');")

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("******** Opening new url in another tab for Email OTP ***********")
        time.sleep(1)
        self.driver.get("https://yopmail.com/")
        time.sleep(1)
        yopmail = self.driver.find_element(By.XPATH, "//input[@id='login']")
        yopmail.send_keys(self.username + Keys.ENTER)
        time.sleep(1)
        iframeElement = self.driver.find_element(By.ID, "ifmail")
        self.driver.switch_to.frame(iframeElement)

        self.logger.info("******** Email Copied ***********")
        time.sleep(1)
        otp = self.driver.find_element(By.XPATH,
                                       "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h1[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", otp)
        time.sleep(0.5)
        getOTP = otp.text
        print(getOTP)
        self.logger.info("******** Switching back and entering the otp ***********")
        self.driver.switch_to.default_content()

        self.driver.switch_to.window(self.driver.window_handles[0])
        # self.fp.clickOtp()
        self.fp.setOtp(getOTP)
        self.logger.info("TS_2  TC_02  Verify that the user can successfully reset their password.")
        self.fp.setNewPass(self.password)
        self.fp.setConPass(self.password)
        self.fp.clickResetPass()

        if "Reset password successful" in self.driver.page_source:
            self.logger.info("********** Verify the Forgot Password Functionality Test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Verify the Forgot Password Functionality Test test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_forgotPasswordValid.png")
            assert False


    @pytest.mark.regression(order=2)
    def test_forgotPasswordInValid(self):
        self.logger.info("****Started invalid Password Login Test****")
        self.fp = forgotPasswordPage(self.driver)
        self.fp.clickforgotPassword()
        self.fp.setEmail(self.username)
        self.fp.clickSendButton()
        self.logger.info("TS_2 TC_03  Verify that the user can successfully reset their password. with invalid OTP")
        # self.fp.clickOtp()
        self.fp.setOtp("123456")
        self.fp.setNewPass(self.password)
        self.fp.setConPass("1234")
        self.fp.clickResetPass()
        self.logger.info("TS_2  TC_04  Verify that the password reset process fails if the new password and confirmation do not match.")
        if "Password did not match" in self.driver.page_source:
            self.logger.info("********** Verify the Forgot Password Functionality Test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Verify the Forgot Password Functionality Test test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_forgotPasswordInValid.png")
            assert False