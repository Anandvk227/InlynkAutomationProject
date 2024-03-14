import time
import unittest
import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.randomGen import randomGen
from pageObjects.ConfigurationPage import ConfigurationPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass
class TestConfiguration(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    DeptName = "QA"
    first_name = randomGen.random_first_name()
    first_name2 = randomGen.random_first_name()
    DeptDescription = "Software Testing"
    EditDeptDescription = "Software Testing test data"
    DivisionName = "Manual Testing"
    DivisionDescription = "Functional and Non Functional"
    EditDivisionDescription = "Functional and Non Functional test data"
    DesignationName = "Associate Test Engineer"
    DesignationDescription = "All testing activities"
    EditDesignationDescription = "All testing activities test data"

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger = LogGen.loggen()

    @pytest.mark.regression
    # @pytest.mark.test

    @pytest.mark.flaky(rerun=3, reun_delay=2)
    @pytest.mark.run(order=7)
    def test_createDept(self):
        self.logger.info("****Started Login Test****")
        # self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.cp = ConfigurationPage(self.driver)
        self.cp.clickModuleConfiguration()
        self.cp.clickDepartments()
        self.logger.info(" Started TC_01 : Verify create NEW Department ")
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DeptName + " " + self.first_name)
        self.cp.setEnterDescription(self.DeptDescription)
        self.cp.clickCreateBtn()

        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DeptCreatedSuccessful()
        )

        if act_Text == "Department created successfully":
            assert True
            self.logger.info("********* TC_01 : Verify create NEW Department Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createDept.png")
            self.logger.error("********* TC_01 : Verify create NEW Department Test is Failed ***********")
            assert False
        time.sleep(3)
        self.logger.info(" Started TC_04 : Verify Search Department ")
        self.cp.setsearchField(self.DeptName + " " + self.first_name)
        self.cp.clickopenDept()
        self.logger.info(" Started TC_06 : Verify create NEW Division ")
        self.cp.clickDivisionsTab()
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DivisionName)
        self.cp.setEnterDescription(self.DivisionDescription)
        self.cp.clickCreateBtn()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DivisionCreatedSuccessful()
        )

        if act_Text == "Division created successfully":
            assert True
            self.logger.info("********* TC_06 : Verify create NEW Division Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createDivision.png")
            self.logger.error("********* Create Division Test is Failed ***********")
            assert False

        self.cp.clickDesignationsTab()
        self.logger.info(" Started TC_10 : Verify Create NEW Designation ")
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DesignationName)
        self.cp.setEnterDescription(self.DesignationDescription)
        self.cp.clickCreateBtn()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DesignationCreatedSuccessful()
        )

        if act_Text == "Designation created successfully":
            assert True
            self.logger.info("********* Create Designation Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "TC_10_test_createDesignation.png")
            self.logger.error("********* TC_10 : Verify Create NEW Designation Test is Failed ***********")
            assert False

    @pytest.mark.regression
    # @pytest.mark.test
    @pytest.mark.run(order=8)
    def test_EditDept(self):
        self.logger.info("****TC_02	Verify Edit Department****")
        # self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.cp = ConfigurationPage(self.driver)
        self.cp.clickModuleConfiguration()
        self.cp.clickDepartments()
        self.cp.clickDepartments()
        # time.sleep(3)
        self.cp.setsearchField(self.DeptName + " " + self.first_name)
        time.sleep(2)
        self.cp.clickEditDepartment()
        self.cp.setEnterDescription(self.EditDeptDescription)
        time.sleep(1)
        self.cp.clickUpdateBtn()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DeptUpdatedSuccessful()
        )

        if act_Text == "Department updated successfully":
            assert True
            self.logger.info("********* updated Department Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_updateDept.png")
            self.logger.error("********* updated Department Test is Failed ***********")
            assert False

        # self.cp.setsearchField(self.DeptName + " " + self.first_name)
        self.cp.clickopenDept()
        self.cp.clickDivisionsTab()
        self.cp.setsearchField(self.DivisionName)
        self.logger.info("********* TC_07	Verify Edit the Division ***********")
        time.sleep(2)
        self.cp.clickEditDivision()
        self.cp.setEnterDescription(self.EditDivisionDescription)
        self.cp.clickUpdateBtn()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DivisionUpdatedSuccessful()
        )

        if act_Text == "Division updated successfully":
            assert True
            self.logger.info("********* updated Division Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UpdateDivision.png")
            self.logger.error("********* updated Division Test is Failed ***********")
            assert False

        self.cp.clickDesignationsTab()
        self.logger.info(" Started TC_01 : Verify create NEW Department ")
        self.cp.setsearchField(self.DesignationName)
        self.cp.clickEditDivision()
        time.sleep(2)
        self.logger.info("********* TC_13	Verify Search Designation***********")
        self.cp.setEnterDescription(self.EditDesignationDescription)
        self.cp.clickUpdateBtn()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DesignationUpdatedSuccessful()
        )

        if act_Text == "Designation updated successfully":
            assert True
            self.logger.info("********* updated Designation Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UpdateDesignation.png")
            self.logger.error("********* updated Designation Test is Failed ***********")

            assert False

    @pytest.mark.regression
    # @pytest.mark.test
    @pytest.mark.run(order=9)
    def test_DeleteDept(self):
        self.logger.info("****Started Login Test****")
        # self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.cp = ConfigurationPage(self.driver)
        self.cp.clickModuleConfiguration()
        self.cp.clickDepartments()
        time.sleep(3)
        self.cp.setsearchField(self.DeptName + " " + self.first_name)
        time.sleep(2)
        self.logger.info("****TC_03	Verify Delete Department****")
        self.cp.clickDeleteDepartment()
        self.cp.clickDeleteDepartmentDelete()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DeleteError()
        )

        if act_Text == "Some Division Under This Department":
            assert True
            self.logger.info("********* Delete Error Designation Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_DevisionError.png")
            self.logger.error("********* Delete Error Designation Test is Failed ***********")

            assert False

        self.cp.clickDeleteDepartmentCancel()
        self.cp.clickopenDept()
        self.logger.info("****TC_05	Verify by clicking on created Department****")
        self.cp.clickDivisionsTab()
        self.logger.info("****TC_09	Verify Search Division****")
        self.cp.setsearchField(self.DivisionName)
        time.sleep(2)
        self.logger.info("****TC_08	Verify Delete the Division****")
        self.cp.clickDeleteDivision()
        self.cp.clickDeleteDepartmentDelete()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DivisionDeletedSuccessfully()
        )

        if act_Text == "Division deleted successfully":
            assert True
            self.logger.info("********* Delete Division Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_DeleteDivision.png")
            self.logger.error("********* Delete Division Test is Failed ***********")

            assert False

        self.cp.clickDesignationsTab()
        self.cp.setsearchField(self.DesignationName)
        # time.sleep(4)
        self.cp.clickDeleteDivision()
        self.cp.clickDeleteDepartmentDelete()
        self.logger.info("*********TC_12	Verify Delete the Designation***********")
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DesignationDeletedSuccessfully()
        )

        if act_Text == "Designation deleted successfully":
            assert True
            self.logger.info("********* Delete Designation Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_DeleteDesignation.png")
            self.logger.error("********* Delete Designation Test is Failed ***********")
            assert False

        # Use the browser's back button to navigate back
        self.cp.clickConfigurationtextLink()

        # Wait for a few seconds (for demonstration purposes)
        time.sleep(3)

        self.cp.setsearchField(self.DeptName + " " + self.first_name)
        time.sleep(2)
        self.logger.info("*********TC_03	Verify Delete Department***********")
        self.cp.clickDeleteDepartment()
        self.cp.clickDeleteDepartmentDelete()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DepartmentDeletedSuccessfully()
        )

        if act_Text == "Department deleted successfully":
            assert True
            self.logger.info("********* Delete Department Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_DeleteDept.png")
            self.logger.error("********* Delete Department Test is Failed ***********")
            assert False

    @pytest.mark.regression
    @pytest.mark.flaky(rerun=3, reun_delay=2)
    @pytest.mark.run(order=10)
    def test_CreateConfDept(self):
        self.logger.info("****Started Login Test****")
        # self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.cp = ConfigurationPage(self.driver)
        self.cp.clickModuleConfiguration()
        self.cp.clickDepartments()
        self.logger.info(" Started TC_01 : Verify create NEW Department ")
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DeptName + " " + self.first_name2)
        self.cp.setEnterDescription(self.DeptDescription)
        self.cp.clickCreateBtn()

        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DeptCreatedSuccessful()
        )

        if act_Text == "Department created successfully":
            assert True
            self.logger.info("********* TC_01 : Verify create NEW Department Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createDept.png")
            self.logger.error("********* TC_01 : Verify create NEW Department Test is Failed ***********")

            assert False

        self.logger.info(" Started TC_04 : Verify Search Department ")
        self.cp.setsearchField(self.DeptName + " " + self.first_name2)
        self.cp.clickopenDept()
        self.logger.info(" Started TC_06 : Verify create NEW Division ")
        self.cp.clickDivisionsTab()
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DivisionName)
        self.cp.setEnterDescription(self.DivisionDescription)
        self.cp.clickCreateBtn()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DivisionCreatedSuccessful()
        )

        if act_Text == "Division created successfully":
            assert True
            self.logger.info("********* TC_06 : Verify create NEW Division Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_createDivision.png")
            self.logger.error("********* Create Division Test is Failed ***********")
            assert False

        self.cp.clickDesignationsTab()
        self.logger.info(" Started TC_10 : Verify Create NEW Designation ")
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DesignationName)
        self.cp.setEnterDescription(self.DesignationDescription)
        self.cp.clickCreateBtn()
        act_Text = WebDriverWait(self.driver, 10).until(
            lambda driver: self.cp.Text_DesignationCreatedSuccessful()
        )

        if act_Text == "Designation created successfully":
            assert True
            self.logger.info("********* Create Designation Test is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "TC_10_test_createDesignation.png")
            self.logger.error("********* TC_10 : Verify Create NEW Designation Test is Failed ***********")
            assert False

    if __name__ == '__main__':
        unittest.main(verbosity=2)
