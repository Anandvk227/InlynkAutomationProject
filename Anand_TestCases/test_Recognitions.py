import time
import pytest


from openpyxl.reader.excel import load_workbook

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from Anand_PageObjects.RecognitionPage import Recognitions
from GenericLib.BaseClass import BaseClass


class Test_Create_Recognition(BaseClass):
    baseURL = ReadConfig.getApplicationURL()

    addemployee="Anand"
    addtitle="Best Employee of the Year"
    adddescription="The Best Employee of the Year is recognized for exceptional performance, innovation, teamwork, leadership, adaptability, initiative, reliability, positivity, customer focus, and continuous learning."


    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["B14"].value
    username1=worksheet["E14"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()


    @pytest.mark.regression
    @pytest.mark.run(order=81)
    # @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition_Verify_Employee_got_Recognition(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        if "Recognition" in self.driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        self.rcp.clickonpreview()
        self.rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in self.driver.page_source:
            self.logger.info("********** Employee recognition published test is passed *********")
            self.logger.info("********** content creation test is passed *********")
            print(self,'--self')

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition published test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_CreateRecognition_Verify_Employee_got_Recognition.png")
            assert False
        self.lp.clickLogout()
        self.lp.setUserName(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** Employee recognition verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_CreateRecognition_Verify_Employee_got_Recognition.png")
            assert False
        self.rcp.closepopup()
        self.lp.clickLogout()


    @pytest.mark.regression
    @pytest.mark.run(order=82)
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.skip(reason="skipping this Test")
    def test_UnpublishedRecognition_and_Verify_in_Employee_account(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        if "Recognition" in self.driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        time.sleep(2)
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.savetemplate()
        time.sleep(2)
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** Employee recognition unpublished test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition unpublished test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedRecognition_and_Verify_in_Employee_account.png")
            assert False
        time.sleep(1)

        if "Anand" in self.driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")
            self.logger.info("********** content creation test is passed *********")

        else:
        # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedRecognition_and_Verify_in_Employee_account.png")
            assert False
        self.lp.clickLogout()
        self.lp.setUserName(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** Employee Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Employee_login_fail.png")
            assert False
        self.lp.clickLogout()


    @pytest.mark.regression
    @pytest.mark.run(order=83)
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.anand
    def test_UnpublishedtoPunlishRecognition(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        if "Recognition" in self.driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        time.sleep(2)
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.savetemplate()
        time.sleep(2)
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** Employee recognition unpublished test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition unpublished test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(1)

        if "Anand" in self.driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(1)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** Employee Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Employee_login_fail.png")
            assert False
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        time.sleep(2)
        if "Recognition" in self.driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        self.rcp.unpublishedtab()
        time.sleep(2)
        self.rcp.clickonthreedots()
        time.sleep(1)
        self.rcp.clickonpublish()
        self.rcp.publishconfirm()
        time.sleep(2)
        if "Employee Recognition has been published successfully" in self.driver.page_source:
            self.logger.info("********** Employee recognition published test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition published test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(2)
        self.rcp.closepopup()
        time.sleep(1)
        self.lp.clickLogout()
        time.sleep(2)


    @pytest.mark.regression
    @pytest.mark.run(order=84)
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.pspk
    def test_EditRecognition(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        if "Recognition" in self.driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        time.sleep(2)
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.savetemplate()
        time.sleep(2)
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** Employee recognition unpublished test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition unpublished test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(2)

        if "Anand" in self.driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** Employee Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "Employee_login_fail.png")
            assert False
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        time.sleep(2)
        if "Recognition" in self.driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        self.rcp.unpublishedtab()
        time.sleep(2)
        self.rcp.clickonthreedots()
        time.sleep(1)
        self.rcp.clickonedit()
        time.sleep(1)
        self.rcp.clcikonback()
        time.sleep(1)
        self.rcp.selecttemplatetwo()
        self.rcp.selectbannertwo()
        time.sleep(1)
        self.rcp.clicknext()
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in self.driver.page_source:
            self.logger.info("********** Employee recognition published test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition published test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(3)
        self.rcp.closepopup()
        time.sleep(3)
        self.lp.clickLogout()


    @pytest.mark.regression
    @pytest.mark.run(order=85)
    # @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition_Verify_Employee_got_Recognition_download_Recognition(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "News Feed" in self.driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        if "Recognition" in self.driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        self.rcp.clicknewrecognition()
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        self.rcp.clickonpreview()
        self.rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in self.driver.page_source:
            self.logger.info("********** Employee recognition has been successfully published *********")
            print(self, '--self')

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition Created fail **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "employee_recognition.png")
            assert False
        self.lp.clickLogout()
        self.lp.setUserName(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_CreateRecognition_Verify_Employee_got_Recognition_download_Recognition.png")
            assert False
        self.rcp.closepopup()
        self.rcp.clickmyprofiletab()
        time.sleep(1)
        self.rcp.clickmyrecognition()
        self.rcp.clickbackrecog()
        self.rcp.clickdownloadrecog()
        self.rcp.selectdownloadtype()
        time.sleep(6)

    if __name__ == '__main__':
        unittest.main(verbosity=2)