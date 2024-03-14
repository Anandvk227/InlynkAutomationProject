import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mediaDrivePage:
    ModuleMediaDrive_xpath = "//span[text()='Media Drive']"
    NoText_xpath = "//span[text()='There are no items']"
    ButtonNew_xpath = "//button[normalize-space()='New']"
    CreateFolder_xpath = "//span[text()='Create Folder']"
    inputFolderName = "//input[@placeholder='Enter a folder name']"
    buttonCreate = "//button[@id='Create']"
    UploadFolder_xpath = "//input[@id='folderType']"
    UploadFiles_xpath = "(//input[@id='filesType'])[1]"
    threeDotsMenu_xapth = "//span[@class=' lightTxt pdngRSM pointer']//*[name()='svg']"
    threeDotsShare_xapth = "//li[@value='share']"
    ShareInputSearch_xapth = "//input[@placeholder='Search by Name & Company']"
    threeDotsZip_xpath = "//li[@value='zip']"
    # //div[contains(text(),'File/Folder converted to zip')]
    threeDotsMoveTo_xpath = "//li[@value='MoveTo']"
    MoveToSearchInput_xpath = "//input[@id='search']"
    # clickSearchedFolder = "(//span[text()='folder'])[2]"
    # add this above in scripts tpo search
    ClickButtonMove_xpath = "//button[normalize-space()='Move']"
    # //div[contains(text(),'Folder moved successfully')]
    ClickMoveToTrash_xpath = "//li[@value='delete']"
    conTrash_xpath = "(//button[text()='Trash'])[2]"
    # //div[contains(text(),'Item Moved to Trash.')]
    rename_xpath = "//li[@value='rename']"
    renameInput_xpath = "//input[@id='renameInput']"
    # //div[contains(text(),'Folder name updated successfully')]
    searchField_xpath = "//input[@type='search']"
    closeFile_xpath = "//div[@aria-label='Close']//div[@class='flexInline alignCntr justifyCntr pointer mediaBtns']"
    ViewMode_xpath = "(//button[@type='button'])[7]"
    Filter_xpath = "(//button[@type='button'])[8]"
    AllCheckBox_xpath = "//body/div[@id='long-menu']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper MuiMenu-paper MuiMenu-paper css-pwxzbm']/ul[@role='menu']/li[1]/div[1]/div[1]/span[1]"
    imagesCheckBox_xpath = "//body/div[@id='long-menu']/div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper MuiMenu-paper MuiMenu-paper css-pwxzbm']/ul[@role='menu']/li[3]/div[1]/div[1]/span[1]"
    Closetoaster_xpath = "//button[@class='Toastify__close-button Toastify__close-button--light']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]"

    # share files
    downArrow_xpath = "//div[@role='presentation']//div[2]//li[1]//div[3]//span[2]//*[name()='svg']"
    None_xpath = "//div[@class='flexAutoCol']//span[contains(text(),'None')]"
    Edit_xpath = "//span[normalize-space()='Edit']"
    View_xpath = "//span[normalize-space()='View']"
    # Tabs
    Tab_MyTemplate_xpath = "//button[normalize-space()='My Template']"
    Tab_SharedWithMe_xpath = "//button[normalize-space()='Shared with me']"
    Tab_Employee_xpath = "//button[normalize-space()='Employee']"
    Tab_Trash_xpath = "//button[normalize-space()='Trash']"
    Tab_search_xpath = "//input[@type='search']"
    threedotsRename_xpath = "//li[@value='rename']"
    CancelRename_xpath = "//button[normalize-space()='Cancel']"
    Done_xpath = "//button[normalize-space()='Done']"
    # MoveTo
    ButtonMove_xpath = "//button[normalize-space()='Move']"
    # Three dots Edit
    threeDotsEdit_xpath = "//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters menuIcon pdngHXS css-1slzbpg']"
    ContinueButton_xpath = "(//button[@type='button'][normalize-space()='Continue'])[1]"
    UploadLogo_xpath = "(//div[@class='flexInline edmLogoBrdr pdngXS justifyCntr alignCntr'])[1]"
    FileMediakit_xpath = "//div[@class='pointer uploadLogoWidth']"
    UploadLogo2_xpath = "//div[@class='flexAutoRow alignCntr justifyEnd edmLogoBrdr pdngXS']"
    chooseFromSystem_xpath = "//input[@id='preview']"
    submitButton_xpath = "//button[normalize-space()='SUBMIT']"
    CropSaveButton_xpath = "(//button[text()='Save'])[3]"
    PreviewButton_xpath = "//button[normalize-space()='Preview']"
    DownloadButton_xpath = "//button[normalize-space()='Download']"
    SaveButton_xpath = "(//button[text()='Save'])[3]"
    EnterFileName_xpath = "//input[@id='name']"
    FileSaveButton_xpath = "(//button[text()='Save'])[4]"
    # zip
    ButtonPreviewZip_xpath = "//div[@aria-label='Zip']//div[@class='flexInline alignCntr justifyCntr pointer mediaBtns']"
    # Trash
    threeDotsDelete_xpath = "//li[@value='delete']"
    ConfDelete_xpath = "//button[normalize-space()='Delete']"
    TrashRestore_xpath = "//li[@value='restore']"
    TrashConfRestore_xpath = "//button[normalize-space()='Restore']"
    TabMyFiles_xpath = "//button[normalize-space()='My Files']"
    # Delete Trash all
    SelectAllCheckBox_xpath = "//th[@class='MuiTableCell-root MuiTableCell-head MuiTableCell-stickyHeader MuiTableCell-paddingCheckbox MuiTableCell-sizeMedium css-148ires']//span[@class='MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeMedium css-2ucf59']"
    TrashAll_xpath = "//button[@aria-label='Trash']"
    DeleteAll_xpath = "//button[@aria-label='Delete']"
    More_Option_xpath = "//button[@aria-label='More Option']"
    AllConfDelete_xpath = "//button[contains(text(),'Delete')]"

    # Employees
    MainFile_xpath = "//span[text()='Main']"
    DeleteEmpFolder_xpath = "//tbody/tr[1]/td[2]/div[1]/span[1]"


    def __init__(self, driver):
        self.driver = driver


    def clickMediaDrive(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ModuleMediaDrive_xpath))
        )
        element.click()
    def clickButtonNew(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ButtonNew_xpath))
        )
        element.click()
    def setinputFolderName(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.inputFolderName))
        )
        element.send_keys(name)
    def setSearchField(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.searchField_xpath))
        )
        element.send_keys(name)
    def setUploadFolder(self, file_path):
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.UploadFiles_xpath))
        )
        file_input.send_keys(file_path)
    def setUploadFiles(self, file_path):
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.UploadFiles_xpath))
        )
        file_input.send_keys(file_path)

    def setchooseFromSystem(self, file_path):
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.chooseFromSystem_xpath))
        )
        file_input.send_keys(file_path)

    def clickUploadFiles(self):
        element = self.driver.find_element(By.XPATH, self.UploadFiles_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
    def clickbuttonCreate(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.buttonCreate))
        )
        element.click()
    def NoTextDisplayed(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.NoText_xpath))
        )
        element.is_displayed()
    def clickthreeDotsMenu(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsMenu_xapth))
        )
        element.click()
    def clickthreeDotsShare(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsShare_xapth))
        )
        element.click()
    def setShareInputSearch(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ShareInputSearch_xapth))
        )
        element.send_keys(name)
    def clickZipthreeDots(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsZip_xpath))
        )
        element.click()
    def clickMoveTothreeDots(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsMoveTo_xpath))
        )
        element.click()
    def setMoveToSearchInput(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MoveToSearchInput_xpath))
        )
        element.send_keys(name)
    def setrenameInput(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.renameInput_xpath))
        )
        element.send_keys(name)
    def ClickButtonMove(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ClickButtonMove_xpath))
        )
        element.click()
    def ClickMoveToTrash(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ClickMoveToTrash_xpath))
        )
        element.click()
    def ClickconfTrash(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.conTrash_xpath))
        )
        element.click()
    def ClickRename(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.rename_xpath))
        )
        element.click()
    def ClickcloseFile(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.closeFile_xpath))
        )
        element.click()
    def ClickViewMode(self):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ViewMode_xpath))
        )
        element.click()
    def ClickFilter(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Filter_xpath))
        )
        element.click()
    def ClickAllCheckBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.AllCheckBox_xpath))
        )
        element.click()
    def ClickImagesCheckBox(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.imagesCheckBox_xpath))
        )
        element.click()

    def clickCreateFolder(self):
        self.driver.find_element(By.XPATH, self.CreateFolder_xpath).click()
    def clickClosetoaster(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Closetoaster_xpath))
        )
        element.click()

#         Share
    def clickdownArrow(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.downArrow_xpath))
        )
        element.click()

    def clickNone(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.None_xpath))
        )
        element.click()
    def clickEdit(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Edit_xpath))
        )
        element.click()
    def clickView(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.View_xpath))
        )
        element.click()
    #     tabs
    def clickTabMyTemplate(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Tab_MyTemplate_xpath))
        )
        element.click()
    def clickTabSharedWithMe(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Tab_SharedWithMe_xpath))
        )
        element.click()
    def clickTabEmployee(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Tab_Employee_xpath))
        )
        element.click()


    def clickTabTrash(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Tab_Trash_xpath))
        )
        element.click()
    def clickthreedotsRename(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threedotsRename_xpath))
        )
        element.click()
    def clickCancelRename(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CancelRename_xpath))
        )
        element.click()
    def clickDone(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Done_xpath))
        )
        element.click()

    def setTabSearch(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Tab_search_xpath))
        )
        element.send_keys(name)

    def clickButtonMove(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ButtonMove_xpath))
        )
        element.click()

    def clickthreeDotsEdit(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsEdit_xpath))
        )
        element.click()
    def clickContinueButton(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.ContinueButton_xpath))
        )
        time.sleep(3)
        element.click()
    def clickUploadLogo(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.UploadLogo_xpath))
        )
        element.click()
    def clickUploadLogo2(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.UploadLogo2_xpath))
        )
        element.click()
    def clickFileMediakit(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FileMediakit_xpath))
        )
        element.click()
    def clicksubmitButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.submitButton_xpath))
        )
        element.click()
    def clickCropSaveButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CropSaveButton_xpath))
        )
        element.click()
    def clickPreviewButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PreviewButton_xpath))
        )
        element.click()
    def clickDownloadButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DownloadButton_xpath))
        )
        element.click()
    def clickSaveButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SaveButton_xpath))
        )
        element.click()
    def setEnterFileName(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.EnterFileName_xpath))
        )
        element.send_keys(name)
    def clickFileSaveButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FileSaveButton_xpath))
        )
        element.click()
    def clickButtonPreviewZip(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ButtonPreviewZip_xpath))
        )
        element.click()
    def clickTrash3dotsDelete(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsDelete_xpath))
        )
        element.click()
    def clickTrashConfDelete(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ConfDelete_xpath))
        )
        element.click()
    def clickTrashRestore(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TrashRestore_xpath))
        )
        element.click()
    def clickTrashConfRestore(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TrashConfRestore_xpath))
        )
        element.click()

    def clickTabMyFiles(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TabMyFiles_xpath))
        )
        element.click()
    def clickSelectAllCheckBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SelectAllCheckBox_xpath))
        )
        element.click()
    def clickMore_Option(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.More_Option_xpath))
        )
        element.click()
    def clickTrashAll(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TrashAll_xpath))
        )
        element.click()
    def clickDeleteAll(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DeleteAll_xpath))
        )
        element.click()

    def clickAllConfDelete(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.AllConfDelete_xpath))
        )
        element.click()
    def clickonMainFile(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MainFile_xpath))
        )
        element.click()
    def clickDeleteEmpFolder(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DeleteEmpFolder_xpath))
        )
        element.click()





