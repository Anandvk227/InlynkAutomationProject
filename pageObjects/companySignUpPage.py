import random
import string
import time
# from telnetlib import EC

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class companySignUpPage:
    link_signUp_xpath = "//button[contains(text(),'sign up')]"
    button_companySignUp_xpath = "(//button[@type='button'])[2]"
    # Individual Sign Up button
    button_IndividualSignUp_xpath = "//b[contains(text(),'INDIVIDUAL SIGNUP')]"
    textbox_companyName_xpath = "//input[@name='companyName']"
    textbox_searchIndustryType_xpath = "//input[@placeholder='Search industries type']"
    list_selectCompany_xpath = "//div[@class='mrgBtm8 industriesFixed']"
    textbox_contactName_xpath = "//input[@name='contactName']"
    # Both company and individual sign Up
    textbox_FullName_xpath = "//input[@name='fullname']"
    textbox_email_xpath = "//input[@name='email']"
    textbox_phone_xpath = "//input[@type='tel']"
    textbox_password_xpath = "//input[@type='password']"
    textbox_ConfirmPassword_xpath = "(//input[@type='password'])[2]"
    checkbox_termsConditions_xpath = "(//input[@aria-label='Checkbox demo'])[1]"
    Button_signupNow_xpath = "//button[normalize-space()='Sign up now!']"
    dd_country_xpath = "(//div[@id='country'])[1]"
    dd_state_xpath = "//div[@id='state']"
    dd_city_xpath = "//div[@id='city']"
    dd_india_xpath = "(//li[@role='option'])[2]"
    dd_Telangana_xpath = "//li[@data-value='TG']"
    dd_Hyderabad_xpath = "//li[normalize-space()='Hyderabad']"
    textBox_enterOtp_xpath = "//input[@type='tel']"
    button_verify_xpath = "//button[normalize-space()='Verify']"
    button_ContinueToLogin_xpath = "//button[normalize-space()='continue to login']"
    # Employee Sign Up
    text_searchCompany_xpath = "//input[@placeholder='Search company...*']"
    Button_employeeSignUp_xpath = "//b[contains(text(),'EMPLOYEE SIGNUP')]"
    Click_selectCompany_xpath = "//div[@data-popper-placement='bottom']"

    def __init__(self,driver):
        self.driver=driver

    def clicksignuplink(self):
        self.driver.find_element(By.XPATH, self.link_signUp_xpath).click()

    # Employee Sign Up
    def setSearchCompany(self, name):
        # self.driver.find_element(By.XPATH, self.text_searchCompany_xpath).send_keys(Password)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.text_searchCompany_xpath))
        )
        element.send_keys(name)
    def ClickEmployeeSignUp(self):
        time.sleep(3)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.Button_employeeSignUp_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)

    def ClickSelectCompany(self):
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.Click_selectCompany_xpath).click()
        # Simulate pressing the down arrow key
        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        # Add a delay if necessary:
        time.sleep(0.1)

        # Simulate pressing the Enter key
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        # Add a delay if necessary:
        time.sleep(0.1)
    def clickCompanysignupButton(self):
        time.sleep(3)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.button_companySignUp_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)

    def clickIndividualSignupButton(self):
        time.sleep(3)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.button_IndividualSignUp_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)

    def clickCompanysignupButton(self):
        time.sleep(3)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.button_companySignUp_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)

    def setCompanyName(self, companyName):

        self.driver.find_element(By.XPATH, self.textbox_companyName_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_companyName_xpath).send_keys(companyName)

    def setSearchIndustryType(self, searchIndustryType):
        self.driver.find_element(By.XPATH, self.textbox_searchIndustryType_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_searchIndustryType_xpath).send_keys(searchIndustryType)

    def selectCompany(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.list_selectCompany_xpath).click()

    def setContactName(self, contactName):
        self.driver.find_element(By.XPATH, self.textbox_contactName_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_contactName_xpath).send_keys(contactName)

    def setFullName(self, email):
        self.driver.find_element(By.XPATH, self.textbox_FullName_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_FullName_xpath).send_keys(email)
    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setPhone(self, phone):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.textbox_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_phone_xpath).send_keys(phone)
        # time.sleep(2)

    def setPassword(self, password):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def setConfirmPassword(self, ConfirmPassword):
        self.driver.find_element(By.XPATH, self.textbox_ConfirmPassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_ConfirmPassword_xpath).send_keys(ConfirmPassword)

    def clicktermsConditions(self):

        element = self.driver.find_element(By.XPATH, self.checkbox_termsConditions_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)

    def clickcountrydd(self):
        self.driver.find_element(By.XPATH, self.dd_country_xpath).click()

    def clickindia(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.dd_india_xpath)))
        element.click()
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(1)
        # self.driver.execute_script("arguments[0].click();", element)

        # self.driver.find_element(By.XPATH, self.dd_india_xpath).click()

    def clickstatedd(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dd_state_xpath).click()

    def clickTelangana(self):
        time.sleep(1)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.dd_Telangana_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)


    def clickcitydd(self):
        # self.driver.find_element(By.XPATH, self.dd_city_xpath).click()
        time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.dd_city_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)

    def clickHyderabad(self):
        time.sleep(1)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.dd_Hyderabad_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(2)

    def clicksignupNow(self):
        self.driver.find_element(By.XPATH, self.Button_signupNow_xpath).click()
        time.sleep(2)

    def setOtp(self,otp):
        self.driver.find_element(By.XPATH, self.textBox_enterOtp_xpath).send_keys(otp)

    def clickVerifyButton(self):
        self.driver.find_element(By.XPATH, self.button_verify_xpath).click()
        time.sleep(5)

    def clickContinueToLogin(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_ContinueToLogin_xpath)))
        element.click()




