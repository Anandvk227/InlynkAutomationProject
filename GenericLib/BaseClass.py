import unittest
from selenium import webdriver
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class BaseClass(unittest.TestCase):

    baseURL = ReadConfig.getApplicationURL()
    def setUp(self):
        self.logger = LogGen.loggen()
        # self.driver = webdriver.Chrome()
        # Choose the browser you want (Chrome, Firefox, Edge, etc.)
        browser_name = "Chrome"

        if browser_name == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser_name == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser_name == "Edge":
            self.driver = webdriver.Edge()
        # Add more browser options as needed
        self.driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)

    def tearDown(self):
        try:
            # Perform an assertion that may raise an exception
            self.assertTrue(False, "Intentional failure")
        except AssertionError:
            # Test failed, take a screenshot
            test_name = self.id().split(".")[-1]
            screenshot_name = f".\\Screenshots\\ALL (Passed Failed)\\{test_name}_failure.png"
            self.take_screenshot(screenshot_name)
        finally:
            self.driver.quit()

    def take_screenshot(self, file_path):
        # Take a screenshot
        self.driver.save_screenshot(file_path)

if __name__ == "__main__":
    unittest.main()
