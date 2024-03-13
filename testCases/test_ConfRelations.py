import time

import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ConfigurationPage import ConfigurationPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_016_ConfRelations:
    baseURL = ReadConfig.getApplicationURL()

    RelationName = "Test Dealer"
    RelationDescription = "Test Dealer Software Testing"
    EditRelationDescription = " Edited Description for relation"


    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_createRelations(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.cp = ConfigurationPage(self.driver)
        self.cp.clickModuleConfiguration()
        self.cp.clickRelations()

        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.RelationName)
        self.cp.setEnterDescription(self.RelationDescription)
        self.cp.clickCreateBtn()
        time.sleep(3)
        act_Text = self.cp.Text_RelationCreatedSuccessfully()
        if act_Text == "Relation created successfully":
            assert True
            self.logger.info("********* Create Relation Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createRelations.png")
            self.logger.error("********* Create Relation Test is Failed ***********")
            self.driver.close()
            assert False


        self.cp.setRelationsearchField(self.RelationName)
        # Edit relation description
        self.cp.clickEditDivision()
        self.cp.setDepartmentName(self.RelationName)
        self.cp.setEnterDescription(self.EditRelationDescription)
        self.cp.clickUpdateBtn()
        time.sleep(3)

        act_Text = self.cp.Text_RelationUpdatedSuccessfully()
        if act_Text == "Relation updated successfully":
            assert True
            self.logger.info("********* update Relation Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createRelations.png")
            self.logger.error("********* update Relation Test is Failed ***********")
            self.driver.close()
            assert False

        self.cp.setRelationsearchField(self.RelationName)

        time.sleep(2)
        self.cp.clickDeleteDivision()
        self.cp.clickDeleteDepartmentDelete()
        time.sleep(2)
        act_Text = self.cp.Text_RelationDeletedSuccessfully()
        if act_Text == "Relation deleted successfully":
            assert True
            self.logger.info("********* Delete Relation Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createRelations.png")
            self.logger.error("********* Delete Relation Test is Failed ***********")
            self.driver.close()
            assert False


