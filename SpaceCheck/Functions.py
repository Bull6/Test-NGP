from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from random import choice
from random import randint
import os


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://spacecheck.ru/test?token=Sr-sCWV6i-fV6f5dQb31xDPfo3socVj-"

    def find_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def visible_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_window(self, handlesNum):
        self.driver.switch_to.window(self.driver.window_handles[handlesNum])

    def current_URL(self):
        return self.driver.current_url
