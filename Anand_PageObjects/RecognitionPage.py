import time
# from telnetlib import EC

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Recognitions:

    button_recognition_xpath="//body/div[@id='root']/div[@class='baseBlockCntnr']/div[@class='flexCol fullHeight']/div[contains(@class,'flexCol resSideNav')]/ul[@class='flexMinHeightCol resSideNavGroup pdngVSM scrollXHidden scrollbarSideNav']/div[1]/div[1]/div[2]"
    button_newrecognition_xpath="//div[@class='flexAutoRow pointer pdngLSM webSearch']"
    button_selecttemplate_xpath="//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]"
    button_selectbadge_xpath="//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]"
    button_clickonnext_xpath="//button[normalize-space()='Next']"
    textbox_addemployee_xpath="//input[@id='employee']"
    button_clickonemployee_xpath="//div[contains(@class,'flexMinWidthCol pdngHMD')]"
    textbox_addtitle_xpath="//input[@id='title']"
    text_adddescription_xpath="//textarea[@id='description']"
    button_preview_xpath="//button[normalize-space()='Preview']"
    button_publish_xapth="//button[normalize-space()='Publish']"
    button_closepopup_xpath="//div[contains(@role,'dialog')]//div[contains(@class,'pdngXS')]//div[contains(@class,'flexAutoRow')]"
    button_clickonsave_xpath="//button[normalize-space()='Save']"
    button_clickunpublishedtab_xpath="//button[normalize-space()='Unpublished']"
    button_threedots_xpath = "//*[@data-testid='MoreVertIcon']"
    button_publish_xpath="//div[@id='account-menu']//li[1]"
    button_confirmpublish_xpath="//button[normalize-space()='Publish']"
    button_clickedit_xapth="//div[@id='account-menu']//li[3]"
    button_clickback_xpath="//button[normalize-space()='Back']"
    button_selecttemplatetwo_xpath="//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]"
    button_selectbadgetwo_xpath="//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div[1]/div[2]"

    click_my_profile_xpath="//body/div[@id='root']/div[contains(@class,'baseBlockCntnr')]/div[contains(@class,'flexCol fullHeight')]/div[contains(@class,'flexCol resSideNav')]/ul[contains(@class,'flexMinHeightCol resSideNavGroup pdngVSM scrollXHidden scrollY')]/div[contains(@class,'flexCol pdngTLG mrgnTLG')]/div[1]"
    click_my_Recognition_xpath="//div[contains(@class,'flexCol whiteBg pdngSM brdrBlackSM brdrRadiusSM newsfeedShadow')]//div[1]//div[1]//div[1]//div[1]//div[2]//div[3]//span[2]"
    click_back_recognition_xpath="//button[@class='flexInline slideBtns slideCloseBtn alignCntr justifyCntr']"
    click_download_recognition_xpath="//body/div[@id='root']/div[@class='baseBlockCntnr']/div[@class='flexCol fullHeight']/div[@class=' innerMainCntnr sideNav']/div[@class='flexCol positionRelative']/div[@class='flexCol positionAbs profileDetailsBody alignCntr justifyCntr']/div[@class='flexCol profileChildCntr']/div[@class='flexCol mrgnVXS']/div[@class='flexCol pdngXS']/div[@class='flexCol whiteBg pdngSM brdrBlackSM brdrRadiusSM newsfeedShadow']/div[@class='flexWrap mrgnTSM']/div[1]/div[2]/div[2]/span[1]"
    select_type_to_download_xpath="//div[@id='account-menu']//li[1]"






    def __init__(self, driver):
        self.driver = driver

    def clickrecognition(self):

        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN)  # Scroll down one page
        # actions.perform()
        element = self.driver.find_element(By.XPATH, self.button_recognition_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_recognition_xpath)))
        element.click()

    def clicknewrecognition(self):
        self.driver.find_element(By.XPATH, self.button_newrecognition_xpath).click()

    def selecttemplate(self):
        self.driver.find_element(By.XPATH,self.button_selecttemplate_xpath).click()

    def selectbadge(self):
        element = self.driver.find_element(By.XPATH, self.button_selectbadge_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(1)
        element.click()

    def clicknext(self):
        self.driver.find_element(By.XPATH,self.button_clickonnext_xpath).click()

    def setaddemployee(self,addemployee):
        self.driver.find_element(By.XPATH,self.textbox_addemployee_xpath).send_keys(addemployee)
        time.sleep(3)

    def clickemployee(self):
        self.driver.find_element(By.XPATH,self.button_clickonemployee_xpath).click()

    def setaddtitle(self,addtitle):
        self.driver.find_element(By.XPATH,self.textbox_addtitle_xpath).send_keys(addtitle)

    def setadddescription(self,adddescription):
        self.driver.find_element(By.XPATH,self.text_adddescription_xpath).send_keys(adddescription)

    def clickonpreview(self):
        preview = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.button_preview_xpath))
        )

        # Scroll to the element using Actions class
        actions = ActionChains(self.driver)
        actions.move_to_element(preview).perform()

        # Wait for the element to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_preview_xpath))
        )

        # Click on the element
        preview.click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.button_preview_xpath).click()

    def clickpublish(self):
        self.driver.find_element(By.XPATH,self.button_publish_xapth).click()

    def closepopup(self):
        self.driver.find_element(By.XPATH,self.button_closepopup_xpath).click()

    def savetemplate(self):
        self.driver.find_element(By.XPATH,self.button_clickonsave_xpath).click()

    def unpublishedtab(self):
        self.driver.find_element(By.XPATH,self.button_clickunpublishedtab_xpath).click()

    def clickonthreedots(self):
        self.driver.find_element(By.XPATH,self.button_threedots_xpath).click()

    def clickonpublish(self):
        self.driver.find_element(By.XPATH,self.button_publish_xpath).click()

    def publishconfirm(self):
        self.driver.find_element(By.XPATH,self.button_confirmpublish_xpath).click()

    def clickonedit(self):
        self.driver.find_element(By.XPATH,self.button_clickedit_xapth).click()

    def clcikonback(self):
        element = self.driver.find_element(By.XPATH, self.button_clickback_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(1)
        element.click()

    def selecttemplatetwo(self):
        self.driver.find_element(By.XPATH,self.button_selecttemplatetwo_xpath).click()

    def selectbannertwo(self):
        element = self.driver.find_element(By.XPATH, self.button_selectbadgetwo_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        time.sleep(1)
        element.click()

    def clickmyprofiletab(self):
        element = self.driver.find_element(By.XPATH, self.click_my_profile_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_recognition_xpath)))
        element.click()

    def clickmyrecognition(self):
        element = self.driver.find_element(By.XPATH, self.click_my_Recognition_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(2)
        # Wait for a short while to ensure the element is clickable
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_recognition_xpath)))
        element.click()

    def clickbackrecog(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.click_back_recognition_xpath)))
        element.click()

    def clickdownloadrecog(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.click_download_recognition_xpath)))
        element.click()

    def selectdownloadtype(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.select_type_to_download_xpath)))
        element.click()



