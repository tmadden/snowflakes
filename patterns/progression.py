import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add


async def progression(lights):
    loop = PeriodicLoop(0.1, 10)
    lights = sorted(lights, key=lambda light: light.p[0] + light.p[1])
    index = 0
    while not loop.done():
        lights[(index - 12) % 17].set_state(off)
        lights[index % 17].set_state(on)
        index += 1
        await loop.next()


# async def progression(lights):
#     loop = PeriodicLoop(0.1, 10)
#     index = 0
#     while not loop.done():
#         lights[(index - 4) % 17].set_state(off)
#         lights[index % 17].set_state(on)
#         index += 1
#         await loop.next()

# async def progression(lights):
#     loop = PeriodicLoop(0.1, 10)
#     index = -1
#     print('index: {}'.format(index))
#     while True:
#         if keyboard.is_pressed('z' if (index % 2) else 'x'):
#             lights[index].set_state(off)
#             index += 1
#             lights[index].set_state(on)
#         await asyncio.sleep(0.001)
