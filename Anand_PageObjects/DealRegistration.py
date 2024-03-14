from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

class dealregistration:
    button_dealtab_xpath="//span[normalize-space()='Deal registration']"
    button_click_newdeal_xpath="//button[normalize-space()='Deal']"
    select_network_company_xpath="//input[@id='highlights-demo']"
    text_company_name_xpath="//input[@id='companyName']"
    text_address_xpath="//input[@id='address']"
    dropdown_country_xpath="//div[contains(@class,'flexCol respdngVSM mrgnTXS')]//button[@id='rfs-btn']"
    select_country_xpath="//li[@id='rfs-IN']"
    dropdown_state_xpath="//div[contains(@class,'flexCol mobpdngLXS onthirdLocationCol false')]//div[@id='state']"
    select_state_xpath="//li[normalize-space()='Andhra Pradesh']"
    dropdown_city_xpath="//div[contains(@class,'flexCol respdngVSM mrgnTXS')]//div[@id='city']"
    select_city_xpath="//li[normalize-space()='Akasahebpet']"
    text_departmentname_xpath="//input[@id='departmentName']"
    text_contactname_xpath="//input[@id='contactName']"
    text_contactemail_xpath="//input[@id='contactEmail']"
    text_contactnumber_xpath="//label[@id=':re:-label']"
    radiobutton_enterprise_xpath="//label[@id='Enterprise']//span[@class='css-hyxlzm']"
    select_accountmanager_xpath="//input[@id='networkCompany']"
    select_relationmanager_xpath="//li[@class='flexRow alignCntr pointer']"
    text_enteropportunity_xpath="//textarea[@id='reqMessage']"
    dropdown_currency_xpath="//div[@id='dealCurrency']"
    text_dealvalue_xpath="//input[@id='dealCurrencyValue']"
    button_savedeal_xpath="//button[normalize-space()='save deal']"
    button_clickonokay_xpath="//span[@class='pdngXS']"
    button_networkdeals_xpath="//button[normalize-space()='Network deals']"
    button_pendingdeals_xpath="//div[contains(@class,'flexRow brdrRadiusXSM')]//div[2]"
    button_clickdealcompany_xpath="//span[@class='subHeadingSM capitalTxt ellipsisTxt']"
    button_createddealselecttwo_xpath="//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/span[1]"
    button_createddealselect_xpath="//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/span[1]"
    dropdown_statusofdeal_xpath="//span[@id='status']"
    button_approved_xpath="//div[normalize-space()='Approve']"
    button_confirmapprove_xpath="//button[normalize-space()='Approve']"
    button_rejectdeals_xpath="//div[@id='fade-menu']//li[2]"
    text_enterreason_xpath="//textarea[contains(@placeholder,'write reason for rejection...')]"
    button_clickonreject_xpath="//button[normalize-space()='Reject']"
    button_click_notification_xpath="//span[@aria-label='Notifications']"
    button_clickhere_xpath="//span[@class='primaryTxt pointer']"
    button_editrelation_xpath="//div[@class='primaryTxt pointer']"
    button_search_account_manager_xpath="//input[@id='networkCompany']"
    click_account_manager_xpath="//span[normalize-space()='persona']"
    remove_account_manager_xpath="//body//div[@id='root']//div[@class='flexCol']//div[@class='flexCol']//div[1]//div[3]"
    button_edit_approve_deal_xpath="//span[normalize-space()='APPROVE']"
    button_update_xpath="//button[normalize-space()='Update']"
    click_ok_deal_xpath="//b[normalize-space()='OK']"
    click_active_deals_xpath="//div[@class='flexInline alignCntr justifyCntr primaryTxt primaryLightBg pdngHVSM brdrRadiusXSM minWidthdeal']"
    search_my_deal_company="//input[@placeholder='Search...']"
    click_my_deals_company_xpath="//span[contains(@class,'subHeadingSM capitalTxt ellipsisTxt')]"
    click_my_pending_deals_xpath="//div[contains(@class,'secondaryTxt pdngHVSM brdrRadiusXSM minWidthdeal')]"
    click_my_reject_deals_xpath="//div[contains(@class,'flexInline alignCntr justifyCntr minWidthdeal textDanger dangerLightBg pdngHVSM brdrRadiusXSM')]"
    click_my_expire_deals_xpath="//div[@class='flexInline alignCntr justifyCntr grayTxt grayLight pdngHVSM brdrRadiusXSM minWidthdeal']"
    back_to_deals_list_xpath="//span[contains(@class,'breadCrumbTxt pointer headingSM')][normalize-space()='Instavc Technologies']"














    
    def __init__(self, driver):
        self.driver = driver

    def clickdealtab(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.button_dealtab_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_dealtab_xpath)))
        element.click()

    def clickonnewdeal(self):
        self.driver.find_element(By.XPATH,self.button_click_newdeal_xpath).click()

    def networkcomapnyselect(self,companyname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_network_company_xpath)))
        element.send_keys(companyname)
        time.sleep(2)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def companydetails(self,nameofcompany):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_company_name_xpath)))
        element.send_keys(nameofcompany)

    def adreesdetails(self,address):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_address_xpath)))
        element.send_keys(address)

    def countrydropdown(self):
        element = self.driver.find_element(By.XPATH, self.dropdown_country_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        element.click()
        # self.driver.find_element(By.XPATH,self.dropdown_country_xpath).click()

    def selectcountry(self):
        preview = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.select_country_xpath))
        )

        # Scroll to the element using Actions class
        actions = ActionChains(self.driver)
        actions.move_to_element(preview).perform()
        preview.click()
        # self.driver.find_element(By.XPATH,self.select_country_xpath).click()

    def statedropdown(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_state_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.dropdown_state_xpath).click()

    def selectstate(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.select_state_xpath)))
        element.click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,self.select_state_xpath).click()

    def citydropdown(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_city_xpath)))
        element.click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,self.dropdown_city_xpath).click()

    def selectcity(self):
        self.driver.find_element(By.XPATH,self.select_city_xpath).click()
        time.sleep(2)

    def departmentname(self,department):
        element = self.driver.find_element(By.XPATH, self.text_departmentname_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)
        element.send_keys(department)

    def contactname(self,contname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_contactname_xpath)))
        element.send_keys(contname)

    def contactemail(self,contemail):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_contactemail_xpath)))
        element.send_keys(contemail)


    def contactnumber(self,contnumber):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_contactnumber_xpath)))
        element.send_keys(contnumber)

    def selectenterprise(self):
        self.driver.find_element(By.XPATH,self.radiobutton_enterprise_xpath).click()

    def accountmanager(self,nameofmanager):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_accountmanager_xpath)))
        element.send_keys(nameofmanager)

    def relationmanager(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_relationmanager_xpath)))
        element.click()

    def enteropportunity(self,oppdetails):
        element = self.driver.find_element(By.XPATH, self.text_enteropportunity_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)
        element.send_keys(oppdetails)
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_enteropportunity_xpath)))
        # element.send_keys(oppdetails)

    def currency(self,currencydetails):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_currency_xpath)))
        element.send_keys(currencydetails)
        element.send_keys(Keys.ENTER)

    def dealvalue(self,valueofdeal):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_dealvalue_xpath)))
        element.send_keys(valueofdeal)

    def savedeal(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_savedeal_xpath)))
        element.click()
        time.sleep(5)
    def okaybutton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_clickonokay_xpath)))
        element.click()


    def networkdeals(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_networkdeals_xpath)))
        element.click()

    def pendingdeals(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_pendingdeals_xpath)))
        element.click()

    def dealcompany(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_clickdealcompany_xpath)))
        element.click()
        time.sleep(3)

    def selectnewdeal(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_createddealselect_xpath)))
        element.click()
        time.sleep(2)

    def selectnewdealtwo(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_createddealselecttwo_xpath)))
        element.click()

    def statusdropdown(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_statusofdeal_xpath)))
        element.click()

    def approved(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_approved_xpath)))
        element.click()

    def confirmtoapprove(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_confirmapprove_xpath)))
        element.click()

    def clickreject(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_rejectdeals_xpath)))
        element.click()

    def reasontoreject(self,reason):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_enterreason_xpath)))
        element.send_keys(reason)

    def clickonreject(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_clickonreject_xpath)))
        element.click()

    def clickonnotification(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_click_notification_xpath)))
        element.click()
        time.sleep(5)

    def clickhere(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_clickhere_xpath)))
        element.click()

    def dealdetailspage(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_editrelation_xpath)))
        element.click()

    def searchaccountmanager(self,accountmanager):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_search_account_manager_xpath)))
        element.send_keys(accountmanager)

    def clickselectedaccmanager(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_account_manager_xpath)))
        element.click()

    def removeexistaccountmanager(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.remove_account_manager_xpath)))
        element.click()

    def approveediteddeal(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_edit_approve_deal_xpath)))
        element.click()

    def confirmupdatedeal(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_update_xpath)))
        element.click()

    def closeapprovedtab(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_ok_deal_xpath)))
        element.click()
    def clickonactivedeals(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_active_deals_xpath)))
        element.click()

    def searchmydealcompany(self,search):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.search_my_deal_company)))
        element.send_keys(search)

    def mydealscompany(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_my_deals_company_xpath)))
        element.click()

    def mypendingdeals(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_my_pending_deals_xpath)))
        element.click()

    def myrejectdeals(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_my_reject_deals_xpath)))
        element.click()

    def myexpiredeals(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_my_expire_deals_xpath)))
        element.click()

    def backdealspage(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.back_to_deals_list_xpath)))
        element.click()




















