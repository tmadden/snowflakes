import asyncio
import datetime
import random

from utilities import *


def inside_hours():
    now = datetime.datetime.now().time()
    if now >= datetime.time(16, 0, 0) and now < datetime.time(22, 0, 0):
        return True
    return False


important_times = []
important_time_index = 0

import itertools


def acknowledge_important_time():
    global important_time_index
    #print('important_time_index: {}'.format(important_time_index))
    now = datetime.datetime.now().time()
    for index, time in enumerate(important_times):
        if important_time_index <= index and now >= time:
            important_time_index = index + 1


def important_time_passed():
    return False

    global important_time_index
    #print('important_time_passed?')
    #print('important_time_index: {}'.format(important_time_index))
    now = datetime.datetime.now().time()
    for index, time in enumerate(itertools.cycle(important_times)):
        #print(index)
        #print(time)
        #print(now)
        if important_time_index <= index and now >= time:
            return True
    return False


async def slumber(lights):
    while True:
        if inside_hours():
            break
        await asyncio.sleep(60)
