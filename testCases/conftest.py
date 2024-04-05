import pytest
from selenium import webdriver
from pytest_html import extras

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.binary_location = '/opt/firefox/firefox'
        firefox_options.add_argument('--headless')

        self.driver = webdriver.Firefox(options=firefox_options)

        # driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata = {
        'Project Name': 'nop Commerce',
        'Module Name': 'Customers',
        'Tester': 'Anand'
    }


@pytest.fixture()
def run_number(request):
    return request.param

# def pytest_html_report_title(report):
#     report.title = "Your Custom Report Title"
#
# def pytest_configure(config):
#     metadata = config.metadata
#     metadata['Project Name'] = 'Your Project Name'
#     metadata['Module Name'] = 'Your Module Name'
#     metadata['Tester'] = 'Your Tester Name'

