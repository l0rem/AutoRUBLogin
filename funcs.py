import requests
from decouple import config


base_url = 'https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin'

login = config('LOGIN')
passwd = config('PASS')


def login_func(action='Login'):

    body = {
        'code': 1,
        'loginid': login,
        'password': passwd,
        'action': action
    }

    response = requests.post(url=base_url,
                             data=body)

    if response.ok:
        return True
    else:
        return False
