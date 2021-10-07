import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

options = webdriver.ChromeOptions()
options.add_argument("--headless")

@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("browser_name")
    # browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# --headless run in headless mode - апуск браузера без самого UI, чтоб это использовать
# нужно созадть объект options
#options = webdriver.ChromeOptions()
#options.add_argument("--headless")
#browser = webdriver.ChromeOptions(options=options)

# попробуй такой вариант
#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)