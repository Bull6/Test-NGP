import requests


class Request:
    def __init__(self):
        self._access_token = None

    @property
    def access_token(self):
        """I'm the 'x' property."""
        # print("getter of x called")
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        # print("setter of x called")
        self._access_token = value

    @access_token.deleter
    def access_token(self):
        # print("deleter of x called")
        del self._access_token


def SingUp(phone):
    response = requests.post('https://api.myfiteat.ru/send-code'
                             , json={"phone": str(phone)})
    return response.json()


def Login(phone, code):
    response = requests.post('https://api.myfiteat.ru/login', json={
        "phone": str(phone),
        "code": str(code)
    })
    access_token = response.json()['tokens']['access_token']
    refresh_token = response.json()['tokens']['refresh_token']

    tokens = [access_token, refresh_token]

    return tokens


def Get_Social():
    response = requests.get('https://api.myfiteat.ru/get-social')
    return response.json()


def Check_Token(refresh_token):
    response = requests.post('https://api.myfiteat.ru/check-refresh', json={
        "refresh_token": refresh_token  # брать токен из Login
    })
    return response.json()


def Update_Tokens(refresh_token):
    response = requests.post('https://api.myfiteat.ru/update-tokens', json={
        "refresh_token": refresh_token  # брать токен из Login
    })
    access_token = response.json()['tokens']['access_token']
    refresh_token = response.json()['tokens']['refresh_token']

    tokens = [access_token, refresh_token]

    return tokens


def Market_List(access_token):
    response = requests.get('https://api.myfiteat.ru/markets/list', headers={'Authorization': 'Bearer ' + access_token})
    return response.json()


def Open_Market(access_token, serial_number):
    response = requests.post('https://api.myfiteat.ru/markets/open',
                             headers={'Authorization': 'Bearer ' + access_token},
                             json={"serial_number": str(serial_number)})
    return response.json()


def Close_Market(access_token, order_id):
    response = requests.post('https://api.myfiteat.ru/markets/close',
                             headers={'Authorization': 'Bearer ' + access_token},
                             json={"order_id": order_id})
    return response.json()


def Get_Position(access_token, code, order_id):
    response = requests.post('https://api.myfiteat.ru/markets/get-position',
                             headers={'Authorization': 'Bearer ' + access_token},
                             json={
                                 "code": str(code),  # product code
                                 "order_id": order_id  # id market
                             })
    return response.json()


def Add_Order(access_token, code1, code2, order_id):
    response = requests.post('https://api.myfiteat.ru/markets/add-order',
                             headers={'Authorization': 'Bearer ' + access_token},
                             json={
                                 "order_id": str(order_id),  # id market
                                 "positions":
                                     [
                                         {
                                             "code": str(code1),  # code of product
                                             "count": 2  # count product
                                         },
                                         {
                                             "code": str(code2),
                                             "count": 1
                                         }
                                     ]
                             })
    return response.json()


def Profile_Data(access_token):
    response = requests.get('https://api.myfiteat.ru/users/profile-data',
                            headers={'Authorization': 'Bearer ' + access_token})
    return response.json()


def Change_Profile(access_token, email, phone, name):
    response = requests.post('https://api.myfiteat.ru/users/change-profile',
                             headers={'Authorization': 'Bearer ' + access_token},
                             json={
                                 "email": email,  # new mail
                                 "phone": phone,  # new phone
                                 "name": name  # new name

                             })
    return response.json()


def Get_History(access_token):
    response = requests.get('https://api.myfiteat.ru/users/get-history',
                            headers={'Authorization': 'Bearer ' + access_token})
    return response.json()
