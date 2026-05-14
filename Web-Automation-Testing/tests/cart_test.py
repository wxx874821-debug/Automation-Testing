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

def test_add_to_cart(browser):
    # 登录
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # 添加商品到购物车
    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    
    # 校验购物车数量
    cart_count = browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert int(cart_count) >= 1