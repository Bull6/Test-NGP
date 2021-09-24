import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    #driver = webdriver.Chrome("../chromedriver")
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("../chromedriver", chrome_options=options)

    yield driver
    driver.quit()
