import os
from telnetlib import EC

import pytest
import time
from selenium.webdriver import ActionChains, Keys

from openpyxl.reader.excel import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from krishnapageObjects.ResourcesPage import Resources
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.randomGen import randomGen
from GenericLib.BaseClass import BaseClass



class Test_Resources(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    # usernames2 = ReadConfig.getuseremails2()
    # usernames1 = ReadConfig.getuseremails1()
    # usernames = ReadConfig.getuseremails()

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    usernames = worksheet["B6"].value
    usernames1 = worksheet["I2"].value
    usernames2 = worksheet["I3"].value
    companyname  = worksheet["C2"].value



    workbook.close()
    wb = load_workbook("TestData/LoginData.xlsx")

    # Select the active worksheet
    ws = wb.active

    # Update the existing cells with new data
    ws['A2'] = username
    ws['B6'] = usernames
    ws['I2'] = usernames1
    ws['I3'] = usernames2
    ws['C2'] = companyname


    # Save the workbook
    wb.save("TestData/LoginData.xlsx")
    relative_seven = "Files/seven.jpg"
    absolute_path7 = os.path.abspath(relative_seven)
    categorydescription = "This description is Our free tool lets you easily create unique descriptions for your product pages. Just enter the product name and let our Frase AI do its magic."
    relative_eight = "Files/eight.jpg"
    absolute_path8 = os.path.abspath(relative_eight)
    subcategorydescription = "This subcategory description is Our free tool lets you easily create unique descriptions for your product pages. Just enter the product name and let our Frase AI do its magic."
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
    contentdescription = "This content description is Our free tool lets you easily create unique descriptions for your product pages. Just enter the product name and let our Frase AI do its magic."
    contentsectiondescription = "Welcome to our free and intuitive description creation tool! Simplify the process of crafting compelling product page descriptions by leveraging the power of our Frase AI. Just input the product name, and let our innovative tool work its "
    sectionimagedescription = "image preview text description presented here"
    # companyname = "all company"






    logger = LogGen.loggen()  # Logger

    @pytest.mark.sahi
    @pytest.mark.krishna
    @pytest.mark.regression
    @pytest.mark.run(order=64)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_categorycreationforcompany(self):
        self.logger.info("************* Test_001_categorycreation **********")
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        categorytitle = randomGen.random_categorytitle()
        subcategorytitle = randomGen.random_subcategorytitle()
        contenttitle = randomGen.random_contenttitle()
        contentsectionname = randomGen.random_contentsectionname()


        self.logger.info("************** category creation test started ************")
        self.rs = Resources(self.driver)
        self.rs.clickoncontentmanagement()
        self.rs.clickoncategorynew()
        self.rs.setcategoryimage(self.absolute_path7)
        self.rs.clickoncategoryimagesave()
        self.rs.setcategorytitle(categorytitle)
        self.rs.setcategorydescription(self.categorydescription)
        self.rs.clickoncategorypublic()
        self.rs.clickoncategoryenable()
        self.rs.clickoncategorysave()
        time.sleep(3)
        self.logger.info("************** category creation test completed ************")
        # act_Text = self.driver.find_element(By.XPATH,("//div[contains(text(),'Category created successfully')]"))
        #
        # if act_Text == "Category created successfully":
        #     assert True
        #     self.logger.info("********* category creation Test is Passed ***********")
        #
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_resources1.png")
        #     self.logger.error("********* category creation Test is Failed ***********")
        #     self.driver.close()
        #     assert False

        def check_category_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Category created successfully')]"))
                )
                assert "Category created successfully" in success_message_element.text
                self.logger.info("********** Category creation test is passed *********")
            except Exception as e:
                self.logger.error("************** Category creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_category creation.png")
                assert False, f"Category creation failed: {e}"
        time.sleep(2)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickClosetoaster()
        self.rs.clickoncategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path8)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory creation test completed ************")



        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"


        # time.sleep(3)
        self.logger.info("********** content creation test is started *********")
        self.rs.clickonsubcategorynew()
        self.rs.clickoncontentnew()
        self.rs.clickonaddcategory()
        self.rs.clickClosetoaster()
        self.rs.clickoncategoryclose()
        self.rs.setcontentbannerimage(self.absolute_path1)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path2)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path3)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path4)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path5)
        self.rs.clickonbannerimagesave()
        self.rs.setcontenttitle(contenttitle)
        self.rs.setcontentdescription(self.contentdescription)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        # self.rs.scrollpublic()
        self.rs.clickoncontentcanshare()
        self.rs.setcontentsectionname(contentsectionname)
        self.rs.setcontentsectiondescription(self.contentsectiondescription)
        # self.rs.clickonsectionimagepath()
        # self.rs.clickonsectionimageselect()
        # self.rs.setsectionimageselect(self.absolute_path1)
        # self.rs.setsectionimagedescription(self.sectionimagedescription)
        self.rs.clickonsectionsave()
        self.rs.clickoncontentpublish()
        time.sleep(3)
        if "Content created successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_content creation.png")
            assert False
        time.sleep(3)
        self.rs.clickonresources()
        self.rs.setresourcescategorysearch(categorytitle)
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='"+categorytitle+"']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//h4[normalize-space()='"+contenttitle+"']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_contentverificationinmyresources.png")
            assert False
        time.sleep(3)
        self.rs.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        self.lp.setUserName(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* relationcompanyLogin succesful **********")
        self.rs.clickonresources()
        self.rs.clickonnetworkresources()
        self.rs.setsearchcompanyname(self.companyname)
        self.rs.clickoncompanyselect()
        self.rs.clickoncontents()
        self.rs.setsearchcontents(contenttitle)
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")
            self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categorycreationforcompany.png")
            assert False
        time.sleep(3)

    @pytest.mark.sanity
    @pytest.mark.babi
    @pytest.mark.run(order=65)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_categorycreationforemployee(self, setup):
        self.logger.info("************* Test_002_categorycreation **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        categorytitle = randomGen.random_categorytitle()
        subcategorytitle = randomGen.random_subcategorytitle()
        contenttitle = randomGen.random_contenttitle()
        contentsectionname = randomGen.random_contentsectionname()

        self.logger.info("************** category creation test started ************")
        self.rs = Resources(self.driver)
        self.rs.clickoncontentmanagement()
        self.rs.clickoncategorynew()
        self.rs.setcategoryimage(self.absolute_path7)
        self.rs.clickoncategoryimagesave()
        self.rs.setcategorytitle(categorytitle)
        self.rs.setcategorydescription(self.categorydescription)
        self.rs.clickoncategorypublic()
        self.rs.clickoncategoryenable()
        self.rs.clickoncategorysave()
        time.sleep(3)
        self.logger.info("************** category creation test completed ************")

        # act_Text = self.driver.find_element(By.XPATH,("//div[contains(text(),'Category created successfully')]"))
        #
        # if act_Text == "Category created successfully":
        #     assert True
        #     self.logger.info("********* category creation Test is Passed ***********")
        #
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_resources1.png")
        #     self.logger.error("********* category creation Test is Failed ***********")
        #     self.driver.close()
        #     assert False

        def check_category_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(text(),'Category created successfully')]"))
                )
                assert "Category created successfully" in success_message_element.text
                self.logger.info("********** Category creation test is passed *********")
            except Exception as e:
                self.logger.error("************** Category creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_category creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(2)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path8)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        # time.sleep(3)
        self.logger.info("********** content creation test is started *********")
        self.rs.clickonsubcategorynew()
        self.rs.clickoncontentnew()
        self.rs.clickonaddcategory()
        self.rs.clickClosetoaster()
        self.rs.clickoncategoryclose()
        self.rs.setcontentbannerimage(self.absolute_path1)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path2)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path3)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path4)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path5)
        self.rs.clickonbannerimagesave()
        self.rs.setcontenttitle(contenttitle)
        self.rs.setcontentdescription(self.contentdescription)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        # self.rs.scrollpublic()
        self.rs.clickoncontentcanshare()
        self.rs.setcontentsectionname(contentsectionname)
        self.rs.setcontentsectiondescription(self.contentsectiondescription)
        # self.rs.clickonsectionimagepath()
        # self.rs.clickonsectionimageselect()
        # self.rs.setsectionimageselect(self.absolute_path1)
        # self.rs.setsectionimagedescription(self.sectionimagedescription)
        self.rs.clickonsectionsave()
        self.rs.clickoncontentpublish()
        time.sleep(3)
        if "Content created successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_content creation.png")
            assert False
        time.sleep(3)
        self.rs.clickonresources()
        time.sleep(3)
        self.rs.setresourcescategorysearch(categorytitle)
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='" + categorytitle + "']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_contentverificationinmyresources.png")
            assert False
        time.sleep(3)
        self.rs.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserName(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        self.rs.clickonresources()
        time.sleep(3)
        self.rs.setresourcescategorysearch(categorytitle)
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='" + categorytitle + "']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")
            self.driver.close()


        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categorycreationforemployee.png")
            assert False
        time.sleep(3)

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=66)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_categorycreationforhierarchy(self):
        self.logger.info("************* Test_003_categorycreation **********")
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        categorytitle = randomGen.random_categorytitle()
        subcategorytitle = randomGen.random_subcategorytitle()
        subcategorytitle1 = randomGen.random_subcategorytitle1()
        subcategorytitle2 = randomGen.random_subcategorytitle2()
        subcategorytitle3 = randomGen.random_subcategorytitle3()
        subcategorytitle4 = randomGen.random_subcategorytitle4()



        self.logger.info("************** category creation test started ************")
        self.rs = Resources(self.driver)
        self.rs.clickoncontentmanagement()
        self.rs.clickoncategorynew()
        self.rs.setcategoryimage(self.absolute_path7)
        self.rs.clickoncategoryimagesave()
        self.rs.setcategorytitle(categorytitle)
        self.rs.setcategorydescription(self.categorydescription)
        self.rs.clickoncategorypublic()
        self.rs.clickoncategoryenable()
        self.rs.clickoncategorysave()
        time.sleep(3)
        self.logger.info("************** category creation test completed ************")

        # act_Text = self.driver.find_element(By.XPATH,("//div[contains(text(),'Category created successfully')]"))
        #
        # if act_Text == "Category created successfully":
        #     assert True
        #     self.logger.info("********* category creation Test is Passed ***********")
        #
        # else:
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_resources1.png")
        #     self.logger.error("********* category creation Test is Failed ***********")
        #     self.driver.close()
        #     assert False

        def check_category_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(text(),'Category created successfully')]"))
                )
                assert "Category created successfully" in success_message_element.text
                self.logger.info("********** Category creation test is passed *********")
            except Exception as e:
                self.logger.error("************** Category creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_category creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(2)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path8)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"
        time.sleep(3)
        self.logger.info("************** subcategory1 creation test started ************")
        self.rs.setcategorysearch(subcategorytitle)
        time.sleep(3)
        self.rs.clickonsubcategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path6)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle1)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory1 creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory1 creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory1 creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(3)
        self.logger.info("************** subcategory2 creation test started ************")
        self.rs.setcategorysearch(subcategorytitle1)
        time.sleep(3)
        self.rs.clickonsubcategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path5)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle2)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory2 creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory2 creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory2 creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(3)
        self.logger.info("************** subcategory3 creation test started ************")
        self.rs.setcategorysearch(subcategorytitle2)
        time.sleep(3)
        self.rs.clickonsubcategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path4)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle3)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory3 creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory3 creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory3 creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(3)
        self.logger.info("************** subcategory4 creation test started ************")
        self.rs.setcategorysearch(subcategorytitle3)
        time.sleep(3)
        self.rs.clickonsubcategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path3)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle4)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory4 creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory4 creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory4 creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(3)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(subcategorytitle4)
        time.sleep(3)
        self.rs.clickonsubcategoryclick()
        time.sleep(3)
        if "You have reached the last subcategory, cannot go inside" in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")
            self.driver.close()


        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categorycreationforhierarchy.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=67)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_categorycreationforrelationcompany(self):
        self.logger.info("************* Test_004_categorycreation **********")
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        categorytitle = randomGen.random_categorytitle()
        subcategorytitle = randomGen.random_subcategorytitle()
        contenttitle = randomGen.random_contenttitle()
        contentsectionname = randomGen.random_contentsectionname()

        self.logger.info("************** category creation test started ************")
        self.rs = Resources(self.driver)
        self.rs.clickoncontentmanagement()
        self.rs.clickoncategorynew()
        self.rs.setcategoryimage(self.absolute_path7)
        self.rs.clickoncategoryimagesave()
        self.rs.setcategorytitle(categorytitle)
        self.rs.setcategorydescription(self.categorydescription)
        # self.rs.clickoncategorypublic()
        self.rs.clickoncategorypartner()
        self.rs.clickoncategoryenable()
        self.rs.clickoncategorysave()
        time.sleep(3)
        self.logger.info("************** category creation test completed ************")

        # act_Text = self.driver.find_element(By.XPATH,("//div[contains(text(),'Category created successfully')]"))
        #
        # if act_Text == "Category created successfully":
        #     assert True
        #     self.logger.info("********* category creation Test is Passed ***********")
        #
        # else:
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_resources1.png")
        #     self.logger.error("********* category creation Test is Failed ***********")
        #     self.driver.close()
        #     assert False

        def check_category_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(text(),'Category created successfully')]"))
                )
                assert "Category created successfully" in success_message_element.text
                self.logger.info("********** Category creation test is passed *********")
            except Exception as e:
                self.logger.error("************** Category creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_category creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(2)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path8)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        # time.sleep(3)
        self.logger.info("********** content creation test is started *********")
        self.rs.clickonsubcategorynew()
        self.rs.clickoncontentnew()
        self.rs.clickonaddcategory()
        self.rs.clickClosetoaster()
        self.rs.clickoncategoryclose()
        self.rs.setcontentbannerimage(self.absolute_path1)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path2)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path3)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path4)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path5)
        self.rs.clickonbannerimagesave()
        self.rs.setcontenttitle(contenttitle)
        self.rs.setcontentdescription(self.contentdescription)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        # self.rs.scrollpublic()
        self.rs.clickoncontentcanshare()
        self.rs.setcontentsectionname(contentsectionname)
        self.rs.setcontentsectiondescription(self.contentsectiondescription)
        # self.rs.clickonsectionimagepath()
        # self.rs.clickonsectionimageselect()
        # self.rs.setsectionimageselect(self.absolute_path1)
        # self.rs.setsectionimagedescription(self.sectionimagedescription)
        self.rs.clickonsectionsave()
        self.rs.clickoncontentpublish()
        time.sleep(3)
        if "Content created successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_content creation.png")
            assert False
        time.sleep(3)
        self.rs.clickonresources()
        time.sleep(3)
        self.rs.setresourcescategorysearch(categorytitle)
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='" + categorytitle + "']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categoryverificationinmyresources.png")
            assert False
        time.sleep(3)
        self.rs.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserName(self.usernames2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        self.rs.clickonresources()
        time.sleep(3)
        self.rs.clickonnetworkresources()
        time.sleep(3)
        self.rs.setsearchcompanyname(self.companyname)
        time.sleep(3)
        self.rs.clickoncompanyselect()
        time.sleep(3)
        self.rs.clickoncontents()
        time.sleep(3)
        self.rs.setsearchcontents(contenttitle)
        time.sleep(3)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")
            self.driver.close()


        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categorycreationforrelationcompany.png")
            assert False
        time.sleep(3)

    @pytest.mark.sohl
    @pytest.mark.regression
    @pytest.mark.run(order=68)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_categoryshare(self):
        self.logger.info("************* Test_005_categorycreation **********")
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        categorytitle = randomGen.random_categorytitle()
        subcategorytitle = randomGen.random_subcategorytitle()
        contenttitle = randomGen.random_contenttitle()
        contentsectionname = randomGen.random_contentsectionname()

        self.logger.info("************** category creation test started ************")
        self.rs = Resources(self.driver)
        self.rs.clickoncontentmanagement()
        self.rs.clickoncategorynew()
        self.rs.setcategoryimage(self.absolute_path7)
        self.rs.clickoncategoryimagesave()
        self.rs.setcategorytitle(categorytitle)
        self.rs.setcategorydescription(self.categorydescription)
        self.rs.clickoncategorypublic()
        self.rs.clickoncategoryenable()
        self.rs.clickoncategorysave()
        time.sleep(3)
        self.logger.info("************** category creation test completed ************")

        # act_Text = self.driver.find_element(By.XPATH,("//div[contains(text(),'Category created successfully')]"))
        #
        # if act_Text == "Category created successfully":
        #     assert True
        #     self.logger.info("********* category creation Test is Passed ***********")
        #
        # else:
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_resources1.png")
        #     self.logger.error("********* category creation Test is Failed ***********")
        #     self.driver.close()
        #     assert False

        def check_category_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(text(),'Category created successfully')]"))
                )
                assert "Category created successfully" in success_message_element.text
                self.logger.info("********** Category creation test is passed *********")
            except Exception as e:
                self.logger.error("************** Category creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_category creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(2)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path8)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        # time.sleep(3)
        self.logger.info("********** content creation test is started *********")
        self.rs.clickonsubcategorynew()
        self.rs.clickoncontentnew()
        self.rs.clickonaddcategory()
        self.rs.clickClosetoaster()
        self.rs.clickoncategoryclose()
        self.rs.setcontentbannerimage(self.absolute_path1)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path2)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path3)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path4)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path5)
        self.rs.clickonbannerimagesave()
        self.rs.setcontenttitle(contenttitle)
        self.rs.setcontentdescription(self.contentdescription)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        # self.rs.scrollpublic()
        self.rs.clickoncontentcanshare()
        self.rs.setcontentsectionname(contentsectionname)
        self.rs.setcontentsectiondescription(self.contentsectiondescription)
        # self.rs.clickonsectionimagepath()
        # self.rs.clickonsectionimageselect()
        # self.rs.setsectionimageselect(self.absolute_path1)
        # self.rs.setsectionimagedescription(self.sectionimagedescription)
        self.rs.clickonsectionsave()
        self.rs.clickoncontentpublish()
        WebDriverWait(self.driver, 20).until(
            lambda driver: "Content created successfully" in driver.page_source
        )
        if "Content created successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_content creation.png")
            assert False
        # time.sleep(3)
        self.rs.clickonresources()
        time.sleep(3)
        self.rs.setresourcescategorysearch(categorytitle)
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='" + categorytitle + "']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categoryverificationinmyresources.png")
            assert False
        time.sleep(3)
        self.rs.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserName(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        self.rs.clickonresources()
        time.sleep(3)
        self.rs.clickonnetworkresources()
        time.sleep(3)
        self.rs.setsearchcompanyname(self.companyname)
        time.sleep(3)
        self.rs.clickoncompanyselect()
        time.sleep(3)
        self.rs.clickoncontents()
        time.sleep(3)
        self.rs.setsearchcontents(contenttitle)
        time.sleep(3)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categoryforrelationcompany.png")
            assert False
        time.sleep(3)
        self.rs.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")
        self.rs.clickoncontentmanagement()
        time.sleep(3)
        self.rs.setcategorysearch(categorytitle)
        time.sleep(3)
        self.rs.clickoncategoryshare()
        self.rs.clickoncategorysharepublic()
        self.rs.clickoncategoryshareaccessyes()
        self.rs.clickoncategorypartner()
        self.rs.clickoncategoryshareaccessyes()
        time.sleep(3)
        self.rs.clickoncategoryclose()
        self.rs.clickonlogout()
        time.sleep(3)
        self.lp.setUserName(self.usernames2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        self.rs.clickonresources()
        time.sleep(3)
        self.rs.clickonnetworkresources()
        time.sleep(3)
        self.rs.setsearchcompanyname(self.companyname)
        time.sleep(3)
        self.rs.clickoncompanyselect()
        time.sleep(3)
        self.rs.clickoncontents()
        time.sleep(3)
        self.rs.setsearchcontents(contenttitle)
        time.sleep(3)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='" + contenttitle + "']").click()
        time.sleep(3)
        if "This content description is Our free tool lets you easily create unique descriptions for your product pages." in self.driver.page_source:
            self.logger.info("********** content verification test is passed *********")
            self.driver.close()


        else:
            # Log and take a screenshot
            self.logger.error("************** content verification test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categoryforrelationcompany.png")
            assert False

    @pytest.mark.ishq
    @pytest.mark.regression
    @pytest.mark.run(order=69)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_categoryedit(self):
        self.logger.info("************* Test_006_categorycreation **********")
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        categorytitle = randomGen.random_categorytitle()
        subcategorytitle = randomGen.random_subcategorytitle()
        contenttitle = randomGen.random_contenttitle()
        contentsectionname = randomGen.random_contentsectionname()

        self.logger.info("************** category creation test started ************")
        self.rs = Resources(self.driver)
        self.rs.clickoncontentmanagement()
        self.rs.clickoncategorynew()
        self.rs.setcategoryimage(self.absolute_path7)
        self.rs.clickoncategoryimagesave()
        self.rs.setcategorytitle(categorytitle)
        self.rs.setcategorydescription(self.categorydescription)
        self.rs.clickoncategorypublic()
        self.rs.clickoncategoryenable()
        self.rs.clickoncategorysave()
        time.sleep(3)
        self.logger.info("************** category creation test completed ************")

        # act_Text = self.driver.find_element(By.XPATH,("//div[contains(text(),'Category created successfully')]"))
        #
        # if act_Text == "Category created successfully":
        #     assert True
        #     self.logger.info("********* category creation Test is Passed ***********")
        #
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_resources1.png")
        #     self.logger.error("********* category creation Test is Failed ***********")
        #     self.driver.close()
        #     assert False

        def check_category_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(text(),'Category created successfully')]"))
                )
                assert "Category created successfully" in success_message_element.text
                self.logger.info("********** Category creation test is passed *********")
            except Exception as e:
                self.logger.error("************** Category creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_category creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(2)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path8)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        # time.sleep(3)
        self.logger.info("********** content creation test is started *********")
        self.rs.clickonsubcategorynew()
        self.rs.clickoncontentnew()
        self.rs.clickonaddcategory()
        self.rs.clickClosetoaster()
        self.rs.clickoncategoryclose()
        self.rs.setcontentbannerimage(self.absolute_path1)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path2)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path3)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path4)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path5)
        self.rs.clickonbannerimagesave()
        self.rs.setcontenttitle(contenttitle)
        self.rs.setcontentdescription(self.contentdescription)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        # self.rs.scrollpublic()
        self.rs.clickoncontentcanshare()
        self.rs.setcontentsectionname(contentsectionname)
        self.rs.setcontentsectiondescription(self.contentsectiondescription)
        # self.rs.clickonsectionimagepath()
        # self.rs.clickonsectionimageselect()
        # self.rs.setsectionimageselect(self.absolute_path1)
        # self.rs.setsectionimagedescription(self.sectionimagedescription)
        self.rs.clickonsectionsave()
        self.rs.clickoncontentpublish()
        time.sleep(3)
        if "Content created successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_content creation.png")
            assert False
        time.sleep(3)
        self.rs.clickoncontentmanagementbreadcrumb()
        time.sleep(3)
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.clickoncategoryedit()
        self.rs.clickoncategorydisable()
        self.rs.clickoncategoryupdate()
        time.sleep(3)
        if "Category updated successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Category update.png")
            assert False
        # actions = ActionChains(self.driver)
        #
        # # Press the PAGE_DOWN key to scroll down
        # actions.send_keys(Keys.PAGE_DOWN)
        #
        # # Perform the scrolling action
        # actions.perform()
        self.rs.scrollcontent()
        self.rs.clickonsubcategoryedit()
        self.rs.clickonsubcategorydisable()
        self.rs.clickonsubcategoryupdate()
        time.sleep(3)
        if "Subcategory updated successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Subcategory update.png")
            assert False
        self.rs.clickoncontentviewmore()
        self.rs.clickonsectionedit()
        self.rs.setcontentsectionname(contentsectionname)
        self.rs.clickonsectionupdate()
        time.sleep(3)
        if "Section updated successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")
            self.driver.close()


        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Section update.png")
            assert False
        time.sleep(3)

    @pytest.mark.Gang
    @pytest.mark.regression
    @pytest.mark.run(order=70)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_categorydelete(self):
        self.logger.info("************* Test_007_categorycreation **********")
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        categorytitle = randomGen.random_categorytitle()
        subcategorytitle = randomGen.random_subcategorytitle()
        contenttitle = randomGen.random_contenttitle()
        contentsectionname = randomGen.random_contentsectionname()

        self.logger.info("************** category creation test started ************")
        self.rs = Resources(self.driver)
        self.rs.clickoncontentmanagement()
        self.rs.clickoncategorynew()
        self.rs.setcategoryimage(self.absolute_path7)
        self.rs.clickoncategoryimagesave()
        self.rs.setcategorytitle(categorytitle)
        self.rs.setcategorydescription(self.categorydescription)
        self.rs.clickoncategorypublic()
        self.rs.clickoncategoryenable()
        self.rs.clickoncategorysave()
        time.sleep(3)
        self.logger.info("************** category creation test completed ************")

        # act_Text = self.driver.find_element(By.XPATH,("//div[contains(text(),'Category created successfully')]"))
        #
        # if act_Text == "Category created successfully":
        #     assert True
        #     self.logger.info("********* category creation Test is Passed ***********")
        #
        # else:
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_resources1.png")
        #     self.logger.error("********* category creation Test is Failed ***********")
        #     self.driver.close()
        #     assert False

        def check_category_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(text(),'Category created successfully')]"))
                )
                assert "Category created successfully" in success_message_element.text
                self.logger.info("********** Category creation test is passed *********")
            except Exception as e:
                self.logger.error("************** Category creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_category creation.png")
                assert False, f"Category creation failed: {e}"

        time.sleep(2)
        self.logger.info("************** subcategory creation test started ************")
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.clickonsubcategorynew()
        self.rs.clickonsubcategorybutton()
        self.rs.setsubcategoryimage(self.absolute_path8)
        self.rs.clickoncategoryimagesave()
        self.rs.setsubcategorytitle(subcategorytitle)
        self.rs.setcategorydescription(self.subcategorydescription)
        self.rs.clickonsubcategoryenable()
        self.rs.clickonsubcategorysave()
        self.logger.info("************** subcategory creation test completed ************")

        def check_subcategory_creation_status(self):
            try:
                success_message_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "// div[contains(text(), 'Subcategory created successfully')]"))
                )
                assert "Subcategory created successfully" in success_message_element.text
                self.logger.info("********** subcategory creation test is passed *********")
            except Exception as e:
                self.logger.error("************** subcategory creation test is failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategory creation.png")
                assert False, f"Category creation failed: {e}"

        # time.sleep(3)
        self.logger.info("********** content creation test is started *********")
        self.rs.clickonsubcategorynew()
        self.rs.clickoncontentnew()
        self.rs.clickonaddcategory()
        self.rs.clickClosetoaster()
        self.rs.clickoncategoryclose()
        self.rs.setcontentbannerimage(self.absolute_path1)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path2)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path3)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path4)
        self.rs.clickonbannerimagesave()
        self.rs.setcontentbannerimage(self.absolute_path5)
        self.rs.clickonbannerimagesave()
        self.rs.setcontenttitle(contenttitle)
        self.rs.setcontentdescription(self.contentdescription)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        # self.rs.scrollpublic()
        self.rs.clickoncontentcanshare()
        self.rs.setcontentsectionname(contentsectionname)
        self.rs.setcontentsectiondescription(self.contentsectiondescription)
        # self.rs.clickonsectionimagepath()
        # self.rs.clickonsectionimageselect()
        # self.rs.setsectionimageselect(self.absolute_path1)
        # self.rs.setsectionimagedescription(self.sectionimagedescription)
        self.rs.clickonsectionsave()
        self.rs.clickoncontentpublish()
        time.sleep(3)
        if "Content created successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_content creation.png")
            assert False
        time.sleep(3)
        self.rs.clickoncontentmanagementbreadcrumb()
        self.rs.setcategorysearch(categorytitle)
        self.rs.clickoncategoryclick()
        self.rs.scrollcontent()
        self.rs.clickonsubcategorydelete()
        self.rs.clickoncontentconfirmdelete()
        time.sleep(3)
        if "Subcategory deleted successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_subcategorydelete.png")
            assert False
        time.sleep(3)
        self.rs.scrollcontent()
        self.rs.clickoncontentviewmore()
        self.rs.clickoncontentdelete()
        self.rs.clickoncontentconfirmdelete()
        time.sleep(3)
        if "Content and its sections deleted successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_contentdelete.png")
            assert False
        time.sleep(3)
        self.rs.clickonsubcategorydelete()
        self.rs.clickoncontentconfirmdelete()
        WebDriverWait(self.driver, 20).until(
            lambda driver: "Category deleted successfully" in driver.page_source
        )

        if "Category deleted successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")
            self.driver.close()


        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_categorydelete.png")
            assert False


    if __name__ == '__main__':
        unittest.main(verbosity=2)
























