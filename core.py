import time
from ping3 import ping
from decouple import config
from logging import getLogger
from utils import login

logger = getLogger()

ping_target = config('PING_TARGET', cast=str, default='8.8.8.8')
consecutive_fails = 0

while True:
    response = ping(ping_target,
                    timeout=1)

    if not response:
        consecutive_fails += 1

        if consecutive_fails >= 2:
            login()
            continue

    else:
        if consecutive_fails > 0:
            consecutive_fails = 0

    time.sleep(1)
