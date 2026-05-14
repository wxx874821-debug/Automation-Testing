import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_login_success(browser):
    # 登录成功用例
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    assert "Products" in browser.page_source

def test_login_fail(browser):
    # 登录失败用例
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("locked_out_user")
    browser.find_element(By.ID, "password").send_keys("wrongpass")
    browser.find_element(By.ID, "login-button").click()
    # Swag Labs 登录失败提示在 <h3 data-test="error"> 中
    error_text = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Epic sadface" in error_text