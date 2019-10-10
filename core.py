import requests

base_url = 'https://login.rz.ruhr-uni-bochum.de/cgi-bin/start'


def login_callback():
    response = requests.get(base_url)
    print(response.text)


login_callback()