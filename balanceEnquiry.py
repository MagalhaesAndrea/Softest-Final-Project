#Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import scroll_into_view_if_needed
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BalanceEnquiry(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/index.php")


    def test_a_login(self):
        driver = self.driver
        driver.find_element(By.NAME, "uid").click()
        driver.find_element(By.NAME, "uid").send_keys("mngr602094")
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys("EmEhApa")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "btnLogin"))).click()

        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()

    # Cannot leave the field empty
    def test_b_empty_account(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='AccSubmit']"))).click()
        time.sleep(3)
        assert driver.switch_to.alert.text == "Please fill all fields"
        driver.switch_to.alert.accept()

    # Must be only numeric, no characters
    def test_c_character_account(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("acc123")
        character1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        assert "Characters are not allowed" in character1.text, "Does not contain character warning"

        driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("123Acc")
        character2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        assert "Characters are not allowed" in character2.text, "Does not contain special warning"

    # Cannot use special characters
    def test_d_special_character_account(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("123!@#")
        special1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        assert "Special characters are not allowed" in special1.text, "Does not contain character warning"

        driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("!@#")
        special2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        assert "Special characters are not allowed" in special2.text, "Does not contain special warning"

    # Cannot leave the first space blank
    def test_e_account_first_space(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(" ")
        blank_space = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        assert "Characters are not allowed" in blank_space.text, "Does not contain character warning"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()