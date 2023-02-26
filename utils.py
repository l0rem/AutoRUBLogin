import requests
from decouple import config

base_url = 'https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin'

uname = config('USERNAME')
passwd = config('PASS')


def login(username: str = uname, password: str = passwd):
    body = {
        'code': 1,
        'loginid': username,
        'password': password,
        'action': 'Login'
    }

    response = requests.post(url=base_url,
                             data=body,
                             timeout=4)

    if response.ok:
        return True
    return False
