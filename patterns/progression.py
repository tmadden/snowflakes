import asyncio
import time
import random

from utilities import *

colors = [
    rgb(255, 0, 64), snowy, warm_white, gorgeous, good_purple,
    rgb(32, 32, 255)
]

gradients = [[-1, -1, 1], [-0.6, 0.8, 1], [1, 2, 2]]


async def progression(lights):
    for color in colors:
        loop = PeriodicLoop(0.01)
        keep_going = True
        t = 0
        gradient = random.choice(gradients)
        while keep_going:
            keep_going = False
            for light in lights:
                if light.p[0] * gradient[0] + light.p[1] * gradient[1] > t:
                    light.set_state(color)
                else:
                    keep_going = True
            t -= gradient[2]
            await loop.next()
        await asyncio.sleep(2)


# import keyboard
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
