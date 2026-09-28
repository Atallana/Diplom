import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 15)

@pytest.fixture(scope="function")
def browser():
    # Настройка опций браузера
    options = Options()
    # Отключаем автоперевод Chrome
    options.add_argument("--disable-features=Translate")
    
    # Опционально: отключаем информационную панель "Chrome управляется автоматизированным ПО"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
