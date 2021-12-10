import asyncio
import datetime
import random

from utilities import *

colors = [
    rgb(255, 0, 64), snowy, warm_white, gorgeous, good_purple,
    rgb(32, 32, 255)
]


def inside_hours():
    now = datetime.datetime.now().time()
    if now > datetime.time(16, 0, 0, 0) and now < datetime.time(22, 0, 0, 0):
        return True
    return False


async def slumber(lights):
    while True:
        if inside_hours():
            break
        reset_all(lights)
        await asyncio.sleep(60)
