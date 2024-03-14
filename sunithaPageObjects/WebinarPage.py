import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC


# import self
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait


class WebinarPage:
    textbox_username_name = "email"
    textbox_password_name = "password"
    button_login_xpath = "//button[normalize-space()='Login']"
    newsFeed_click_xpath = "//div[@class='resNavLink activeLink']"
    TrainingAndWebinar_click_xpath = "(//span[contains(text(),'Training & Webinar')])[1]"
    New_button_xpath = "//div[@class='flexAutoRow pointer pdngLSM webSearch']//button[@id='create new']"
    Webinar_RadioButton_xpath = "//span[normalize-space()='Webinar']"
    Title_input_id = "title"
    Description_input_id = "description"
    # Date_Time_click_xpath = "//button[@aria-label='Choose date, selected date is Feb 14, 2024']//*[name()='svg']"
    Date_Time_click_xpath="(//button[@type='button'])[4]"
    Calendar_forward_arrow_xpath = "//button[@title='Next month']//*[name()='svg']"
    select_date_click_xpath = "//button[normalize-space()='25']"
    calendar_hours_click_xpath = "//div[@class='MuiClock-squareMask css-1umqo6f']"
    normal_path_click_xpath = "//div[@class='flexCol pdngXS oneFiveSelect']"
    hrs_list_click_id = "hr"
    time_click_xpath = "//li[normalize-space()='02']"
    minutes_list_click_id = "minutes"
    select_minutes_click_xpath = "//li[normalize-space()='03']"
    Toggle_button_click_xpath = "//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']"
    Limit_seats_input_xpath = "//input[@id='noOfSeats']"
    Add_CoHost_click_xpath = "//div[@class='flexRow respdngVSM']//input[@id='employee']"
    select_CoHost_click_xpath = "//div[@class='flexRow respdngSM brdrBSM ']//div[@class='flexAutoRow']//*[name()='svg']"
    Add_panelist_input_xpath = "(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd css-1y3zh1'])[2]"
    Select_panelist_xpath = "//div[@class='flexRow respdngSM brdrBSM ']//div[@class='flexAutoRow']//*[name()='svg']"
    participants_manufacturer_click_xpath = "//span[normalize-space()='Manufacturer']"
    participants_shareHolder_click_xpath = "//span[normalize-space()='share holder']"
    participants_vendor_click_xpath = "//span[normalize-space()='vendor']"
    participants_partner_click_xpath = "//span[normalize-space()='partner']"
    participants_distributor_click_xpath = "//span[normalize-space()='distributor']"
    memberSearch_input_click_xpath = "//div[@class='flexRow']//input[@id='employee']"
    AddEmail_button_click_xpath = "//div[@class='flexRow']//div[@class='MuiInputAdornment-root MuiInputAdornment-positionEnd MuiInputAdornment-outlined MuiInputAdornment-sizeSmall css-1nvf7g0']//*[name()='svg']"
    # Schedule_button_click_xpath = "//button[@id='Create']"
    PublicEnable_click_xpath = "//div[@class='flexRow alignCntr ']//input[@type='checkbox']"
    Text_addCoHost_xpath = "//span[normalize-space()='Add Co-host']"
    cancel_button_click_xpath = "//button[@id='cancel']"

    Schedule_button_click_xpath = "//button[@id='Create']"

    # Webinar Past Tab-----------------------------------------------------------------------------
    Past_tab_button_id = "past tab"
    Date_FebMonth_xpath = "//button[contains(text(),'‹')]"
    Date_click_xpath = "//abbr[@aria-label='February 27, 2024']"
    View_pastSession_xpath = "//button[normalize-space()='View']"
    ChatHistory_click_xpath = "//span[normalize-space()='View chat history']"
    CloseChatHistory_click_xpath = "//span[@aria-label='Close']"
    ViewPollHistory_click_xpath = "//span[normalize-space()='View poll history']"
    closePollHistory_click_xpath = "//div[@class='flexAutoRow alignCntr pointer pdngHXS']//*[name()='svg']"
    PastSessions_breadCrumb_xpath = "//span[@class='breadCrumbTxt pointer headingSM']"

    #Webinar Past Session Search Bar----------------------------------------------------------------------
    Search_pastSessions_id = "search"
    Session_card_xpath = "//span[@class='scheduleTitleTxt PrimaryHoverTxt fontWeightMD ellipsisTxt']"
    sessionCard_close_xpath = "//div[@class='flexAutoRow alignCntr pointer pdngRSM']"
    calendar_jan17_xpath = "//abbr[@aria-label='January 17, 2024']"

    #Webinar Past Session Filter------------------------------------------------------------------------------------
    Past_Filter_Xpath = "//button[@aria-label='Filter']//*[name()='svg']"
    Training_checkBox_xpath = "(//input[@type='checkbox'])[2]"
    Apply_button_xpath = "//div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div[3]/button"

    #Webinar Upcomin Tab---------------------------------------------------------------------------------
    UpcomingTab_button_id = "upcoming tab"
    MarchMonth_forward_arrow = "//button[contains(text(),'›')]"
    Calendar_Feb_xpath = "//button[28]"
    Upcoming_March_25 = "//button[normalize-space()='25']"
    search_WebinarMeeting_xpath  = "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall MuiInputBase-adornedStart css-18yqadl']//input[@id='search']"
    Session_Edit_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium pointer css-vubbuv'])[3]"
    edit_listbox_xpath = "//span[normalize-space()='Edit']"

    UpdateMeeting_button_id = "Create"
    UpdateConfirm_xpath = "(//button[text()='Update'])[2]"
    #Moreaction_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium pointer css-vubbuv'])[3]"
    copy_link_xpath = "//span[normalize-space()='Copy link']"
    copy_invitation_xpath = "//span[normalize-space()='Copy invitation']"
    Copy_Button_xpath = "//button[normalize-space()='Copy']"
    CancelCard_xpath = "//button[normalize-space()='Cancel']"
    ViewRegistrants_xpath = "//span[normalize-space()='View Registrants']"
    BreadCrumb_Xpath = "//span[@class='breadCrumbTxt pointer headingSM']"
    DeleteSession_xpath = "//span[normalize-space()='Delete']"
    Delete_Webinar_xpath = "//button[normalize-space()='Delete']"

    #Training Session-------------------------------------------------------------------------------------------------------------
    Webinar_checkbox_xpath = "(//input[@type='checkbox'])[2]"
    Trining_jan26_xpath  = "//abbr[@aria-label='January 26, 2024']"
    Training_Search_xpath = "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall MuiInputBase-adornedStart css-18yqadl']//input[@id='search']"
    Training_PTS_xpath = "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall MuiInputBase-adornedStart css-18yqadl']//input[@id='search']"
    TodayMeeting_start_xpath = "//button[contains(@class,'MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButton-disableElevation whiteTxt css-1wkmqsn')]"

    #start the meeting___________
    select_todayDate_click_xpath = "//button[normalize-space()='14']"
    manualTime_input_xpath = "//input[@id=':r9:']"
    current_time_xpath = "//div[@class='MuiClock-squareMask css-1umqo6f']"

    #Book the meeting from employee side______________
    BookSeat_linkTest_xpath = "//button[text()='Book a seat']"
    Logout_linkTest_xpath = "//div[@class='flexMinWidthCol pdngXS']"
    CloseToaster_button_xpath = "//div[@class='flexRow alignCntr justifyEnd poniter']//*[name()='svg']"






    def __init__(self, driver):
        self.driver = driver


    def setUserName(self, username):
        # time.sleep(2)
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)
        # time.sleep(1)

    def setpassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
        # time.sleep(1)

    def clickLogin(self, timeout10):
        wait = WebDriverWait(self.driver, timeout10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        element.click()
        time.sleep(2)
       # self.driver.find_element(By.XPATH, self.button_login_xpath).click()



    def clickTAndWModule(self):
        time.sleep(3)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.TrainingAndWebinar_click_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Wait for a short while to ensure the element is clickable
        element.click()
        time.sleep(1)

    def NewButton(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.New_button_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.New_button_xpath).click()



    def WebinarRadioButton(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Webinar_RadioButton_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Webinar_RadioButton_xpath).click()


    def setTitle(self, Tittle):
        time.sleep(1)
        self.driver.find_element(By.ID, self.Title_input_id).send_keys(Tittle)

    def EditTitle(self,Tittle):
        time.sleep(1)
        self.driver.find_element(By.ID, self.Title_input_id).send_keys(Keys.CONTROL, 'a',
                                                                        Keys.DELETE)
         #Select and delete existing text
        self.driver.find_element(By.ID, self.Title_input_id).send_keys(Tittle)



    def setDescription(self, description):
        time.sleep(1)
        self.driver.find_element(By.ID, self.Description_input_id).send_keys(description)


    def DateTime(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Date_Time_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Date_Time_click_xpath).click()

    def CalendarforwardArrow(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Calendar_forward_arrow_xpath)))
        element.click()


    def selectDate(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_date_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.select_date_click_xpath).click()



    def calendarHours(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.calendar_hours_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.calendar_hours_click_xpath).click()


    def NormalPath(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.normal_path_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.normal_path_click_xpath).click()

    def Hrs(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.hrs_list_click_id)))
        element.click()
        # self.driver.find_element(By.ID, self.hrs_list_click_id).click()


    def SelectHours(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.time_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.time_click_xpath).click()


    def minutes(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.minutes_list_click_id)))
        element.click()
        # self.driver.find_element(By.ID, self.minutes_list_click_id).click()


    def SelectMinutes(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_minutes_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.select_minutes_click_xpath).click()


    def ToggleButton(self):
        time.sleep(2)
        # time.sleep(4)  # Consider removing this sleep if not necessary
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Toggle_button_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Toggle_button_click_xpath).click()

    def LimitSeats(self, LimitSeats):
        time.sleep(1)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.Text_addCoHost_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        self.driver.find_element(By.XPATH, self.Limit_seats_input_xpath).send_keys(LimitSeats)

    def coHostSearch(self, coHost):
        self.driver.find_element(By.XPATH, self.Add_CoHost_click_xpath).send_keys(coHost)
        time.sleep(1)

    def selectCoHost(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_CoHost_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.select_CoHost_click_xpath).click()


    def AddPanelist(self,panelist):
        self.driver.find_element(By.XPATH,self.Add_panelist_input_xpath).send_keys(panelist)
        time.sleep(1)

    def SelectPanelist(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Select_panelist_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Select_panelist_xpath).click()

    def manufacturer(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.participants_manufacturer_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.participants_manufacturer_click_xpath).click()

    def shareHolder(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.participants_shareHolder_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.participants_shareHolder_click_xpath).click()

    def vendor(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.participants_vendor_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.participants_vendor_click_xpath).click()

    def partner(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.participants_partner_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.participants_partner_click_xpath).click()

    def distributor(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.participants_distributor_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.participants_distributor_click_xpath).click()

    def memberEMail(self, Email):
        self.driver.find_element(By.XPATH, self.memberSearch_input_click_xpath).send_keys(Email)
        time.sleep(1)

    def setAddEmail(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.AddEmail_button_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.AddEmail_button_click_xpath).click()

    def PublicEnable(self):
        element = self.driver.find_element(By.XPATH,self.PublicEnable_click_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(1)
        element.click()

    def Schedule(self):
        time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.Schedule_button_click_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)


        # Wait for a short while to ensure the element is clickable
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Schedule_button_click_xpath).click()

        #Webinar Past Tab___________________________

    def PastTab(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.Past_tab_button_id)))
        element.click()
        # self.driver.find_element(By.ID, self.Past_tab_button_id).click()

    def FebMonth(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Date_FebMonth_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Date_janMonth_xpath).click()


    def FebDate(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Date_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Date_click_xpath).click()


    def PastViewButton(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.View_pastSession_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.View_pastSession_xpath).click()

    def ChatHistory(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.ChatHistory_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.ChatHistory_click_xpath).click()


    def CloseChatHistrory(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.CloseChatHistory_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.CloseChatHistory_click_xpath).click()

    def ViewPollHistory(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.ViewPollHistory_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.ViewPollHistory_click_xpath).click()

    def ClosePollHistory(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.closePollHistory_click_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.closePollHistory_click_xpath).click()

    def PastSessionBreadcrumb(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.PastSessions_breadCrumb_xpath)))
        element.click()

        # self.driver.find_element(By.XPATH,self.PastSessions_breadCrumb_xpath).click()



        #Past Session search Bar____________________________________
    def PastSearch(self,PastTabSearch):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.Search_pastSessions_id)))
        element.send_keys(PastTabSearch)



    def SessionCard(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Session_card_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self. Session_card_xpath).click()


    def SessionCardClose(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.sessionCard_close_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.sessionCard_close_xpath).click()


        #calendar click on jan 17
    def calendarjan17(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.calendar_jan17_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.calendar_jan17_xpath).click()

            # Past Tab Filter

    def PastTabFilter(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Past_Filter_Xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Past_Filter_Xpath).click()

    def TrainingCheckBox(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Training_checkBox_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Training_checkBox_xpath).click()

    def ApplyButton(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Apply_button_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Apply_button_xpath).click()

        #UPCOMING TAB########
    def UpcomingTab(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.UpcomingTab_button_id)))
        element.click()
        # self.driver.find_element(By.ID,self.UpcomingTab_button_id).click()

    def CalendarFeb(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Calendar_Feb_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Calendar_Feb_xpath).click()

    def MarchMonth(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.MarchMonth_forward_arrow)))
        element.click()


    def UpcomingMar25(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Upcoming_March_25)))
        element.click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH,self.Upcoming_Feb_25).click()


    def searchWebinarMeeting(self,web):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.search_WebinarMeeting_xpath).send_keys(web)

    def SessionEdit(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Session_Edit_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Session_Edit_xpath).click()


    def editListbox(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.edit_listbox_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.edit_listbox_xpath).click()

    def EditTitle(self,Tittle):
        time.sleep(3)
        self.driver.find_element(By.ID, self.Title_input_id).send_keys(Keys.CONTROL, 'a',
         Keys.DELETE)
        #Select and delete existing text
        self.driver.find_element(By.ID, self.Title_input_id).send_keys(Tittle)

    #def UpdateMeeting(self):
       # self.driver.find_element(By.XPATH,self.UpdateMeeting_button_Xpath).click()

    def UpdateMeeting(self):
        time.sleep(2)
        # Scroll to bring the element into view
        element = (self.driver.find_element(By.XPATH, self.cancel_button_click_xpath))


        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(4)
        self.driver.find_element(By.ID,self.UpdateMeeting_button_id).click()

    def UpdateConfirm(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.UpdateConfirm_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.UpdateConfirm_xpath).click()



    #def Moreaction(self):
        #self.driver.find_element(By.XPATH,self.Moreaction_xpath).click()

    def copyLink(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.copy_link_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.copy_link_xpath).click()

    def copyInvitation(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.copy_invitation_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.copy_invitation_xpath).click()

    def CopyButton(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Copy_Button_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Copy_Button_xpath).click()

    def CancelCard(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.CancelCard_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.CancelCard_xpath).click()

    def ViewRegistrants(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.ViewRegistrants_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.ViewRegistrants_xpath).click()


    def BreadCrumb(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.BreadCrumb_Xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.BreadCrumb_Xpath).click()




    def DeleteSession(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.DeleteSession_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.DeleteSession_xpath).click()

    def DeleteWebinar(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Delete_Webinar_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Delete_Webinar_xpath).click()

        #Training session---------------------------------------------

    def WebinarCheckbox(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Webinar_checkbox_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Webinar_checkbox_xpath).click()

    def TriningJan26(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Trining_jan26_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.Trining_jan26_xpath).click()

    def TrainingSearch(self,Training):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.Training_Search_xpath).send_keys(Training)

    def TrainingPTS(self,PTS):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.Training_PTS_xpath).send_keys(PTS)


    def TodayMeetingStart(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.TodayMeeting_start_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.TodayMeeting_start_xpath).send_keys()

    # def todayDate(self):
    #     time.sleep(3)
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_todayDate_click_xpath)))
    #     element.click()
    #     # self.driver.find_element(By.XPATH,self.select_todayDate_click_xpath).click()
    def manualTimeinput(self, manualtime):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.manualTime_input_xpath).send_keys(Keys.CONTROL, 'a',
                                                                              Keys.DELETE)

        self.driver.find_element(By.XPATH,self.manualTime_input_xpath).send_keys(manualtime)
        time.sleep(2)


    # def currentTime(self,):
        # time.sleep(2)
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.current_time_xpath)))
        # element.click()
        # self.driver.find_element(By.XPATH,self.current_time_xpath).click()


    def BookSeat(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.BookSeat_linkTest_xpath)))
        element.click()

    def CloseToaster(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.CloseToaster_button_xpath)))
        element.click()

    def Logout(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Logout_linkTest_xpath)))
        element.click()






























