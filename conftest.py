import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action='store', default='en', help="Choose language en/us/ru/fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    browser = None
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    browser = webdriver.Chrome(executable_path="/Users/lingvvarm/webdrivers/chromedriver", options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()