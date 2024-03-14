import os
import unittest

import pytest
import time

from openpyxl.reader.excel import load_workbook
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from krishnapageObjects.NewsfeedPage import NewsFeed
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass

class TestNewsFeed(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    whats = ReadConfig.getwhats()
    whatso = ReadConfig.getwhatso()
    # usernames = ReadConfig.getuseremails()
    # usernames1 = ReadConfig.getuseremails1()
    # usernames2 = ReadConfig.getuseremails2()
    # usernames3 = ReadConfig.getuseremails3()
    whatson = ReadConfig.getwhatson()
    oneimage = ReadConfig.getoneimage()
    fiveimages = ReadConfig.getfiveimages()

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    usernames = worksheet["B6"].value
    usernames1 = worksheet["I2"].value
    usernames2 = worksheet["I3"].value
    usernames3 = worksheet["D6"].value

    workbook.close()
    # Load the existing workbook
    # wb = load_workbook("TestData/LoginData.xlsx")

    #
    # # Select the active worksheet


    # Select the active worksheet

    # ws = wb.active

    # Update the existing cells with new data
    # ws['A2'] = username
    # ws['B6'] = usernames
    # ws['I2'] = usernames1
    # ws['I3'] = usernames2
    # ws['D6'] = usernames3

    #
    # # Save the workbook


    # Save the workbook

    # wb.save("TestData/LoginData.xlsx")



    relative_one = "Files/one.png"
    absolute_path1 = os.path.abspath(relative_one)
    relative_two = "Files/two.png"
    absolute_path2 = os.path.abspath(relative_two)
    relative_three = "Files/three.png"
    absolute_path3 = os.path.abspath(relative_three)
    relative_four = "Files/four.png"
    absolute_path4 = os.path.abspath(relative_four)
    relative_five = "Files/five.png"
    absolute_path5 = os.path.abspath(relative_five)
    relative_six = "Files/six.jpg"
    absolute_path6 = os.path.abspath(relative_six)
    relative_video1 = "Files/video1.mp4"
    absolute_pathvideo1 = os.path.abspath(relative_video1)
    whatvideo = ReadConfig.getwhatvideo()
    relative_video2 = "Files/video2.mp4"
    absolute_pathvideo2 = os.path.abspath(relative_video2)
    whatvideos = ReadConfig.getwhatvideos()
    whatyoutube = ReadConfig.getwhatyoutube()
    youtubeurl = ReadConfig.getyoutubeurl()
    whatedit = ReadConfig.getwhatedit()
    commenttext = "hiii gud mrng"
    replytext = "gudmorning all"
    commentedittext = "all "
    search = "hii,all employees and relation companies"

    logger = LogGen.loggen()  # Logger


    @pytest.mark.tests
    @pytest.mark.regression
    @pytest.mark.run(order=43)
    # @pytest.mark.flaky(reruns=3,reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforemployees(self):
        self.logger.info("************* Test_001_NewsFeed **********")
        self.logger.info("************** TC_01 Create a feed with text content.  **************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhats(self.whats)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin succesful **********")
        if "Hi,gud mrng employees" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedverification.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=44)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforempndrel(self):
        self.logger.info("************* Test_002_NewsFeed **********")
        self.logger.info("********** TC_20 Create a feed with Public enabled. *******")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatso(self.whatso)
        self.nf.clickonpublic()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforempndrel.png")
            assert False

    @pytest.mark.test
    @pytest.mark.regression
    @pytest.mark.run(order=45)
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforpartners(self):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.logger.info("************* TC_21 Create a feed with Public disabled (default) and Partners checkbox selected.*************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatson(self.whatson)
        self.nf.clickonemp()
        self.nf.clickonpartner()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* partnerLogin succesful **********")
        if "hii,all partners schedule the meeting" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforpartners.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=46)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforarchived(self):
        self.logger.info("************* Test_004_NewsFeed **********")
        self.logger.info("************ TC_22 Create a feed with Status disabled **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhats(self.whats)
        self.nf.clickonstatus()
        self.nf.clickonpost()
        time.sleep(3)
        if "Post created and saved in archived list" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedots()
        self.nf.clickonarchive()
        time.sleep(3)
        if "Hi,gud mrng employees" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforarchived.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=47)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwithimage(self):
        self.logger.info("************* Test_005_NewsFeed **********")
        self.logger.info("*************** Test_06 Create a feed with text and upload 1 image.   **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setoneimage(self.oneimage)
        self.nf.setgallery(self.absolute_path1)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* EmpLogin succesful **********")
        time.sleep(3)
        if "one image upload" in self.driver.page_source:
            self.logger.info("***************Newsfeed test is passed **********")
            # self.driver.close()

        else:
            self.logger.error("************* NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwithimage.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=48)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwith5images(self):
        self.logger.info("************* Test_006_NewsFeed **********")
        self.logger.info("*********** TC_05 Create a feed with text and image uploads (up to 5 images). **************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setfiveimages(self.fiveimages)
        self.nf.setgallery(self.absolute_path1)
        self.nf.setgallery(self.absolute_path2)
        self.nf.setgallery(self.absolute_path3)
        self.nf.setgallery(self.absolute_path4)
        self.nf.setgallery(self.absolute_path5)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* EmpLogin succesful **********")
        self.nf.clickonimage()
        time.sleep(3)
        if "five images upload" in self.driver.page_source:
            self.logger.info("***************Newsfeed test is passed **********")
            # self.driver.close()

        else:
            self.logger.error("************* NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwith5images.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=49)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwith6images(self):
        self.logger.info("************* Test_007_NewsFeed **********")
        self.logger.info("************* Tc_07 Attempt to create a feed with text and upload 6 images.************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setgallery(self.absolute_path1)
        self.nf.setgallery(self.absolute_path2)
        self.nf.setgallery(self.absolute_path3)
        self.nf.setgallery(self.absolute_path4)
        self.nf.setgallery(self.absolute_path5)
        self.nf.setgallery(self.absolute_path6)
        # self.nf.clickonpost()
        time.sleep(3)
        if "Cannot upload more than 5 images" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwith6images.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=50)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwithimages(self):
        self.logger.info("************* Test_008_NewsFeed **********")
        self.logger.info("************* TC_08 Create a feed with only image uploads (no text).")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setfiveimages(self.fiveimages)
        self.nf.setgallery(self.absolute_path1)
        self.nf.setgallery(self.absolute_path2)
        self.nf.setgallery(self.absolute_path3)
        self.nf.setgallery(self.absolute_path4)
        self.nf.setgallery(self.absolute_path5)
        self.nf.clickonpublic()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* EmpLogin succesful **********")
        self.nf.clickonimage()
        time.sleep(3)
        if "five images upload" in self.driver.page_source:
            self.logger.info("***************Newsfeed test is passed **********")
            # self.driver.close()

        else:
            self.logger.error("************* NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwithimages.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=51)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")

    def test_newsfeedforemployeesvideo(self):
        self.logger.info("************* Test_009_NewsFeed **********")
        self.logger.info("************* TC_09 Create a feed with text and upload video. ************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhats(self.whatvideo)
        self.nf.setvideo(self.absolute_pathvideo1)
        time.sleep(3)
        # self.nf.clickonpost()
        if "Cannot upload greater than 20MB" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforemployeesvideo.png")
            assert False

    @pytest.mark.test
    @pytest.mark.regression
    @pytest.mark.run(order=52)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforemployeesvideos(self):
        self.logger.info("************* Test_010_NewsFeed **********")
        self.logger.info("*************** TC_10 Attempt to create a feed with text and upload more than 20mb video. ************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhats(self.whatvideos)
        self.nf.setvideo(self.absolute_pathvideo2)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin succesful **********")
        if "uploading videos" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforemployeesvideos.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=53)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforempndrelvideo(self):
        self.logger.info("************* Test_011_NewsFeed **********")
        self.logger.info("*********** TC_13 Create a feed with text and upload one YouTube URL. ***********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatyoutube(self.whatyoutube)
        self.nf.clickonpublic()
        self.nf.clickonyoutube()
        self.nf.setyoutubeurl(self.youtubeurl)
        self.nf.clickondone()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "uploading youtube videos" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforempndrelvideo.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=54)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_editnewsfeedforemployees(self):
        self.logger.info("************* Test_012_NewsFeed **********")
        self.logger.info("************ TC_23 Edit a feed by changing the text content ************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhats(self.whats)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedot()
        self.nf.clickonedit()
        self.nf.setwhatedit(self.whatedit)
        self.nf.clickonpublic()
        self.nf.clickonupdate()
        time.sleep(3)
        if "News feed updated successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedupdate.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "Hi,gud mrng employeesEditing the feed" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editnewsfeedforemployees.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=55)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_deletenewsfeedforempndrelvideo(self):
        self.logger.info("************* Test_013_NewsFeed **********")
        self.logger.info("*********** TC_29 Delete a feed and select the checkbox for permanent deletion. **************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatyoutube(self.whatyoutube)
        self.nf.clickonpublic()
        self.nf.clickonyoutube()
        self.nf.setyoutubeurl(self.youtubeurl)
        self.nf.clickondone()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedot()
        self.nf.clickondelete()
        self.nf.clickondeletecheckbox()
        self.nf.clickondeletebutton()
        time.sleep(3)
        if "News Feed deleted successfully!" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_deletenewsfeedforempndrelvideo.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=56)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_archivenewsfeedwith5images(self):
        self.logger.info("************* Test_014_NewsFeed **********")
        self.logger.info("************ TC_28 Delete a feed without selecting the checkbox. ***********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setfiveimages(self.fiveimages)
        self.nf.setgallery(self.absolute_path1)
        self.nf.setgallery(self.absolute_path2)
        self.nf.setgallery(self.absolute_path3)
        self.nf.setgallery(self.absolute_path4)
        self.nf.setgallery(self.absolute_path5)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedot()
        self.nf.clickondelete()
        self.nf.clickondeletebutton()
        time.sleep(3)
        if "Feed deleted successfully, saved in archived feed" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedarchieve.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedots()
        self.nf.clickonarchive()
        time.sleep(3)
        if "five images upload" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_archivenewsfeedwith5images.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=57)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_bookmarknewsfeed(self):
        self.logger.info("************* Test_015_NewsFeed **********")
        self.logger.info("************* TC_32 Add a feed to bookmarks. ***********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatso(self.whatso)
        self.nf.clickonpublic()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf = NewsFeed(self.driver)
        self.nf.clickonthreedot()
        self.nf.clickonbookmark()
        self.nf.clickonexplore()
        time.sleep(3)
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedverification.png")
            assert False
        time.sleep(3)
        self.nf.clickonremove()
        self.logger.info("************* TC_33 Remove a feed from bookmarks. **********")
        time.sleep(3)
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.error("********** NewsFeed test is failed *********")
            # Log and take a screenshot
            self.driver.save_screenshot(".\\Screenshots\\" + "test_bookmarknewsfeed.png")
            assert False


        else:
            self.logger.info("************** NewsFeed test is passed **********")
            # self.driver.close()
        time.sleep(3)

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=58)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_selfposts(self):
        self.logger.info("************* Test_016_NewsFeed **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatso(self.whatso)
        self.nf.clickonpublic()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedots()
        self.nf.clickonfilter()
        self.nf.clickonall()
        self.nf.clickonself()
        self.nf.clickonapply()
        time.sleep(3)
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_selfposts.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=59)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_sharenewsfeed(self):
        self.logger.info("************* Test_017_NewsFeed **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatso(self.whatso)
        self.nf.clickonpublic()
        self.nf.clickonpost()
        time.sleep(1)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(1)
        self.nf.clickonshare()
        self.nf.clickonwhatsapp()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(3)

        if "https://web.whatsapp.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedwhatsapp.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        # Switch to the last opened window
        self.driver.switch_to.window(window_handles[0])
        self.nf.clickonshare()
        self.driver.implicitly_wait(5)
        self.nf.clickonfacebook()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[2])
        time.sleep(3)

        if "https://www.facebook.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedfacebook.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        self.nf.clickonshare()
        self.nf.clickontwitter()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[3])
        time.sleep(3)

        if "https://twitter.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedtwitter.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        self.nf.clickonshare()
        self.nf.clickonlinkedin()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[4])
        time.sleep(3)

        if "https://www.linkedin.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedlinkedin.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        self.nf.clickonshare()
        self.nf.clickontelegram()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[5])
        time.sleep(3)

        if "https://telegram.me/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedtelegram.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        self.nf.clickonshare()
        self.nf.clickongmail()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[6])
        time.sleep(3)

        if "https://accounts.google.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")
        elif "https://www.google.com/" in self.driver.current_url:
            # Handle the other condition
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedgoogle.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        # self.nf.clickonshare()
        # time.sleep(2)
        self.nf.clickoninstagram()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[7])
        time.sleep(3)

        if "https://www.instagram.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedinstagram.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.tests
    @pytest.mark.regression
    @pytest.mark.run(order=60)
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_adminfeed(self):
        self.logger.info("************* Test_018_NewsFeed **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.usernames3)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhatso(self.whatso)
        self.nf.clickonpublic()
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_adminfeed.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=61)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_feedcomment(self):
        self.logger.info("************* Test_019_NewsFeed **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhats(self.whats)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickoncomment()
        self.nf.setcommenttext(self.commenttext)
        self.nf.clickonsend()
        self.nf.clickoncancelcmnt()
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.driver.execute_script("window.open('', '_blank');")
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        self.driver.get(self.baseURL)
        self.lp.setUserName(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin succesful **********")
        if "Hi,gud mrng employees" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedverification.png")
            assert False
        time.sleep(3)
        self.nf.clickoncomments()
        self.nf.clickonreplycmnt()
        self.nf.setreplytext(self.replytext)
        self.nf.clickonreplysend()
        self.nf.clickonviewreply()
        time.sleep(3)
        if "gudmorning all" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_feedcomment.png")
            assert False

    @pytest.mark.kri
    @pytest.mark.regression
    @pytest.mark.run(order=62)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_editfeedcomment(self):
        self.logger.info("************* Test_020_NewsFeed **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.setwhats(self.whats)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.clickoncomment()
        self.nf.setcommenttext(self.commenttext)
        self.nf.clickonsend()
        self.nf.clickoncommentthreedot()
        self.nf.clickoncommentedit()
        self.nf.setcommentedittext(self.commentedittext)
        self.nf.clickoncommenteditsend()
        self.nf.clickoncommentthreedot()
        self.nf.clickoncommentdelete()
        self.nf.clickoncommentconfirmdelete()
        time.sleep(3)
        if "all hiii gud mrng" in self.driver.page_source:
            self.logger.error("********** NewsFeed test is failed *********")
            # Log and take a screenshot
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editfeedcomment.png")
            assert False


        else:
            self.logger.info("************** NewsFeed test is passed **********")
            # self.driver.close()

    @pytest.mark.babi
    @pytest.mark.regression
    @pytest.mark.run(order=63)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_adminasemployeefeed(self):
        self.logger.info("************* Test_018_NewsFeed **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.usernames3)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        self.nf.clickOnwhat()
        self.nf.clickonrolechange()
        self.nf.clickonemployeeselect()
        self.nf.setwhatso(self.whatso)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        self.nf.setsearch(self.search)
        self.nf.clickonlike()
        self.logger.info("************ TC_37 Like a feed. **********")
        time.sleep(3)
        if "1 Like" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedlike.png")
            assert False
        time.sleep(3)
        self.nf.clickondislike()
        self.logger.info("************* TC_38 Unlike a feed. ************")

    if __name__ == '__main__':
        unittest.main(verbosity=2)
