# python3 -m pytest  --capture=tee-sys --html=report.html  -v main.py


import pytest

from API_Test.Requests import *

phone = "+71111111111"
code = "0000"
serial_number = "7868768767698765"
order_id = 385
product_code = "211221112"
product_code2 = "11111111"
email = "test@gmail.com"
name = "test"


def test_SingUp():
    assert SingUp(phone)['message'] == 'OK'


def test_Login():
    tokens = Login(phone, code)
    global access_token
    access_token = tokens[0]
    global refresh_token
    refresh_token = tokens[1]

    assert access_token


def test_Get_Social():
    assert Get_Social()['message'] == 'OK'


def test_Check_Token():
    assert Check_Token(refresh_token)['message'] == 'OK'


def test_Update_Token():
    global refresh_token
    tokens = Update_Tokens(refresh_token)
    global access_token
    s = access_token
    access_token = tokens[0]
    refresh_token = tokens[1]
    assert access_token != s


def test_Market_List():
    assert Market_List(access_token)['message'] == 'OK'


def test_Open_Market():
    assert Open_Market(access_token, serial_number)['message'] == 'OK'


def test_Close_Market():
    assert Close_Market(access_token, order_id)['message'] == 'OK'


def test_Get_Position():
    assert Get_Position(access_token, product_code, order_id)['message'] == 'OK'


def test_Add_Order():
    assert Add_Order(access_token, product_code, product_code2, order_id)['message'] == 'OK'


def test_Profile_Data():
    assert Profile_Data(access_token)['message'] == 'OK'


def test_Change_Profile():
    assert Change_Profile(access_token, email, phone, name)['message'] == 'OK'


def test_Get_History():
    assert Get_History(access_token)['message'] == 'OK'


