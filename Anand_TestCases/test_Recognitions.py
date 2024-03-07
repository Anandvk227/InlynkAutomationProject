import time
import pytest


from openpyxl.reader.excel import load_workbook

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from Anand_PageObjects.RecognitionPage import Recognitions


class Test_Create_Recognition:
    baseURL = ReadConfig.getApplicationURL()

<<<<<<< HEAD
    addemployee="Anand"
=======
    # RelationName = "Test Dealer"
    # RelationDescription = "Test Dealer Software Testing"
    # EditRelationDescription = " Edited Description for relation"
    addemployee="kris"
>>>>>>> ad87542115e9232134461826ce188a663850c551
    addtitle="Best Employee of the Year"
    adddescription="The Best Employee of the Year is recognized for exceptional performance, innovation, teamwork, leadership, adaptability, initiative, reliability, positivity, customer focus, and continuous learning."


    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

<<<<<<< HEAD
    username = worksheet["B14"].value
    username1=worksheet["E14"].value
=======
    username = worksheet["B7"].value
    username1=worksheet["E7"].value
>>>>>>> ad87542115e9232134461826ce188a663850c551
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()

    # @pytest.mark.anand
<<<<<<< HEAD
    # @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition_Verify_Employee_got_Recognition(self,setup):
=======
    @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition(self,setup):
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
<<<<<<< HEAD
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
=======
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
<<<<<<< HEAD
=======
        time.sleep(2)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
<<<<<<< HEAD
        self.rcp.clickonpreview()
=======
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")
<<<<<<< HEAD
            print(self,'--self')
=======
>>>>>>> ad87542115e9232134461826ce188a663850c551

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
<<<<<<< HEAD
        self.lp.clickLogout()
        self.lp.setUserName(self.username1)
=======
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
<<<<<<< HEAD
        self.rcp.closepopup()
        self.lp.clickLogout()

    # @pytest.mark.skip(reason="skipping this Test")
    def test_UnpublishedRecognition_and_Verify_in_Employee_account(self,setup):
=======
        time.sleep(3)
        self.rcp.closepopup()
        time.sleep(3)
        self.lp.clickLogout()

    @pytest.mark.skip(reason="skipping this Test")
    def test_UnpublishedRecognition(self,setup):
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
<<<<<<< HEAD
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
=======
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

>>>>>>> ad87542115e9232134461826ce188a663850c551
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
<<<<<<< HEAD
        time.sleep(2)
=======
        time.sleep(1)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
<<<<<<< HEAD
        time.sleep(1)

        if "Anand" in self.driver.page_source:
=======
        time.sleep(3)

        if "Krishna" in self.driver.page_source:
>>>>>>> ad87542115e9232134461826ce188a663850c551
            self.logger.info("********** content creation test is passed *********")

        else:
        # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
<<<<<<< HEAD
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

    # @pytest.mark.skip(reason="skipping this Test")
=======
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickLogout()

    @pytest.mark.skip(reason="skipping this Test")
>>>>>>> ad87542115e9232134461826ce188a663850c551
    # @pytest.mark.anand
    def test_UnpublishedtoPunlishRecognition(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
<<<<<<< HEAD
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
=======
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

>>>>>>> ad87542115e9232134461826ce188a663850c551
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
<<<<<<< HEAD
        time.sleep(2)
=======
        time.sleep(1)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
<<<<<<< HEAD
        time.sleep(1)

        if "Anand" in self.driver.page_source:
=======
        time.sleep(3)

        if "Krishna" in self.driver.page_source:
>>>>>>> ad87542115e9232134461826ce188a663850c551
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
<<<<<<< HEAD
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
=======
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
<<<<<<< HEAD
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
=======
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        time.sleep(2)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.rcp.unpublishedtab()
        time.sleep(2)
        self.rcp.clickonthreedots()
        time.sleep(1)
        self.rcp.clickonpublish()
        self.rcp.publishconfirm()
        time.sleep(2)
        if "Employee Recognition has been published successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
<<<<<<< HEAD
        self.lp.setUserName(self.username1)
=======
        self.lp.setUserName1(self.username1)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(2)
        self.rcp.closepopup()
        time.sleep(1)
        self.lp.clickLogout()
        time.sleep(2)

<<<<<<< HEAD
    # @pytest.mark.skip(reason="skipping this Test")
=======

>>>>>>> ad87542115e9232134461826ce188a663850c551
    # @pytest.mark.pspk
    def test_EditRecognition(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
<<<<<<< HEAD
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
=======
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

>>>>>>> ad87542115e9232134461826ce188a663850c551
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
<<<<<<< HEAD
        time.sleep(2)
=======
        time.sleep(1)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
<<<<<<< HEAD
        time.sleep(2)

        if "Anand" in self.driver.page_source:
=======
        time.sleep(3)

        if "Krishna" in self.driver.page_source:
>>>>>>> ad87542115e9232134461826ce188a663850c551
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
<<<<<<< HEAD
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
=======
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
<<<<<<< HEAD
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
=======
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        time.sleep(2)
>>>>>>> ad87542115e9232134461826ce188a663850c551
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
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
<<<<<<< HEAD
        self.lp.setUserName(self.username1)
=======
        self.lp.setUserName1(self.username1)
>>>>>>> ad87542115e9232134461826ce188a663850c551
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.rcp.closepopup()
        time.sleep(3)
        self.lp.clickLogout()

<<<<<<< HEAD
    # @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition_Verify_Employee_got_Recognition_download_Recognition(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
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
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        self.rcp.closepopup()
        self.rcp.clickmyprofiletab()
        time.sleep(1)
        self.rcp.clickmyrecognition()
        self.rcp.clickbackrecog()
        self.rcp.clickdownloadrecog()
        self.rcp.selectdownloadtype()
        time.sleep(6)

=======
>>>>>>> ad87542115e9232134461826ce188a663850c551


