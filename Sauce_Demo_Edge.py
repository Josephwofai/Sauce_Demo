from modulefinder import Module

import select
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Edge()
time.sleep(4)
driver.maximize_window()

# Navigate to the URL
driver.get("https://www.saucedemo.com/")
time.sleep(10)

# Input Credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

# Add_Product_to_Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(3)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(3)

# My_Cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(3)
driver.find_element(By.NAME, "checkout").click()
time.sleep(3)

# Checkout_Your_Information
driver.find_element(By.ID, "first-name").send_keys("Ralia")
time.sleep(3)
driver.find_element(By.ID, "last-name").send_keys("Odinga")
time.sleep(3)
driver.find_element(By.NAME, "postalCode").send_keys("12345")
time.sleep(5)
driver.find_element(By.ID, "continue").click()
time.sleep(8)

# Checkout: Overview
driver.find_element(By.ID, "finish").click()
time.sleep(6)

# Hand_Bogger_Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(3)
