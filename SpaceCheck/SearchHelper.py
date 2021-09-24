from Functions import BasePage
from Locators import SpaceCheckTestsLocators as locators
import time
from random import choice
from random import randint
import os
import pytest

timeout = 10


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(locators.open_question, timeout)
        search_field.send_keys(word)
        return search_field

    def click_on_element(self, locator):
        return self.find_element(locator, timeout).click()

    def check_visible_element(self, locator):
        return self.visible_element(locator, timeout)

    def login(self, surname, name, patronymic, phone, email):

        self.find_element(locators.login_surname, timeout).send_keys(surname)
        self.find_element(locators.login_name, timeout).send_keys(name)
        self.find_element(locators.login_patronymic, timeout).send_keys(patronymic)
        self.find_element(locators.login_phone, timeout).send_keys(phone)
        self.find_element(locators.login_email, timeout).send_keys(email)

        self.startbtn()

    def startbtn(self):
        self.find_element(locators.start_btn, timeout).click()

    def Get_ID_Question(self):
        return self.find_element(locators.id_question, timeout).get_attribute("value")

    def Get_ID_Test(self):
        return self.find_element(locators.id_test, timeout).get_attribute("value")

    def Check_Type(self):
        time.sleep(0.2)
        self.find_element(locators.instruction_button, timeout).click()
        check_type = self.find_element(locators.check_type, timeout).text
        return check_type

    def nextbtn(self):
        self.find_element(locators.next_btn, timeout).click()

    def World_Question(self):
        answers = self.find_elements(locators.answers, timeout)
        choice(answers).click()
        self.nextbtn()


    def Choose_Single(self):
        # testCheckSingle(browser)
        answers = self.find_elements(locators.answers, timeout)
        choice(answers).click()
        # #time.sleep(5)
        self.nextbtn()
        assert True

    def Open_Question(self):
        self.find_element(locators.open_question, timeout).send_keys('test\n')

    def Choose_Many(self):
        # testCheckSingle(browser)
        answers = self.find_elements(locators.answers, timeout)

        for x in range(randint(1, len(answers))):
            choice(answers).click()
        # #time.sleep(5)
        self.nextbtn()

    def Priority_Question(self):
        # testPriority(browser)
        answers = self.find_elements(locators.priority, timeout)
        # answer = shuffle(answer)

        '''if len(dropLastAnswer) != 0:
            for elem in dropLastAnswer:
                elem.click()
        dropLastAnswer = []'''

        sUm = 10

        for elem in answers:
            all_children_by_css = elem.find_elements(locators.answers)
            # #time.sleep(0.5)
            # choice(all_children_by_css).click()

            if sUm != 0:
                x = all_children_by_css[9]  # choice(all_children_by_css)
                if int(x.text) > sUm:
                    continue
                sUm = sUm - int(x.text)
                # dropLastAnswer.append(x)
                x.click()
        # #time.sleep(5)
        self.nextbtn()

    def Scale_Question(self):
        # testScale(browser)
        answers = self.find_elements(locators.radio_btn, timeout)
        x = choice(answers)
        while x.text in [1, 2, 4, 5]:
            x = choice(answers)
        x.click()
        # #time.sleep(5)
        self.nextbtn()

    def Upload_Question(self):
        self.find_element(locators.upload_file, timeout).send_keys(os.getcwd() + "/1.jpeg")

        self.find_element(locators.upload_text, timeout).send_keys('test\n')
