import time
import unittest

import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass


class TestLogin(BaseClass):
    baseURL = ReadConfig.getApplicationURL()

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active
    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()

    @pytest.mark.run(order=4)
    @pytest.mark.regression
    def test_homePageTitle(self):
        self.logger.info("****Started Home page title test ****")
        act_title=self.driver.title

        if act_title=="InLynk - Business Digital Eco System":
            self.logger.info("**** Home page title test passed ****")
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            assert False

    @pytest.mark.run(order=5)
    @pytest.mark.regression
    def test_login_inValid_Password(self):

        self.logger.info("****Started invalid Password Login Test****")
        self.logger.info("**** TS_01  TC_03 Started invalid Password Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword("InLINK@!@#$")
        self.lp.clickLogin()

        act_Text = self.lp.IncorrectLoginText()

        if act_Text == "Incorrect username or password.":
            assert True
            self.logger.info("********* invalid Login password Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_inValid_Password.png")
            self.logger.error("********* invalid Login password Test is Failed ***********")
            assert False

    @pytest.mark.run(order=6)
    @pytest.mark.regression
    def test_login_inValid_Username(self):

        self.logger.info("****Started invalid Username Login Test****")
        self.logger.info("***** TS_1  TC_04	 verify the login page with invalid user name*****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName("sohel@gmailxyz.com")
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_Text = self.lp.IncorrectLoginText()

        if act_Text == "Incorrect username or password.":
            assert True
            self.logger.info("********* invalid Login Username Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_inValid_Username.png")
            self.logger.error("********* invalid Login Username Test is Failed ***********")
            assert False



    @pytest.mark.run(order=3)
    @pytest.mark.regression
    @pytest.mark.test
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_login_Valid_UsernamePassword(self):

        self.logger.info("****Started Login Test****")
        self.logger.info("****TS_1	TC_01	Verify that a registered user can successfully log in with valid credentials.****")
        self.lp = LoginPage(self.driver)
        self.logger.info(
            "Entering SuperAdmin Credentials for login Username:" + self.username + " and Password:" + self.password)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickcreatePost()
        act_Text = self.lp.newsFeedText()

        if act_Text == "Create News Feed":
            assert True
            self.logger.info("********* Login Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_Valid_UsernamePassword.png")
            self.logger.error("********* Login Test is Failed ***********")
            assert False

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='flexAutoRow alignCntr pdngHXS']"))
        )
        element.click()

    if __name__ == '__main__':
        unittest.main(verbosity=2)