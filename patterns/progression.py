import asyncio
import time
import random

from utilities import *

colors = [
    rgb(255, 0, 64), snowy, warm_white, gorgeous, good_purple,
    rgb(32, 32, 255)
]


async def y_progression(lights):
    for color in colors:
        loop = PeriodicLoop(0.02)
        for y in reversed(range(10, 70)):
            for light in lights:
                if light.p[1] > y:
                    light.set_state(color)
            await loop.next()
        await asyncio.sleep(2)


async def x_progression(lights):
    for color in colors:
        loop = PeriodicLoop(0.01)
        for x in reversed(range(0, 120)):
            for light in lights:
                if light.p[0] > x:
                    light.set_state(color)
            await loop.next()
        await asyncio.sleep(2)


async def sequenceOlga(lights):
    loop = PeriodicLoop(0.8, 200)
    for x in range(0, 18):
        lights[x].set_state(light_gorgeous)
    await loop.next()
    for x in range(0, 18):
        lights[x + 1].set_state(good_purple)
        lights[x].set_state(light_gorgeous)
        await loop.next()
    await loop.next()


async def screenOlga(lights):
    screen = [lights[1], lights[12], lights[17]]
    loop = PeriodicLoop(0.8, 200)

    for x in range(0, 18):
        lights[x].set_state(light_gorgeous)
    await loop.next()

    for x in range(0, 3):
        screen[x].set_state(good_purple)
        screen[(x - 1) % 3].set_state(off)
        await loop.next()


async def screensOlga(lights):
    screen1 = [lights[1], lights[12], lights[17]]
    screen2 = [lights[4], lights[7], lights[8], lights[11], lights[16]]
    screen3 = [lights[5], lights[6], lights[13]]
    screen4 = [lights[2], lights[9]]
    screen5 = [lights[0], lights[3], lights[10], lights[14], lights[15]]
    loop = PeriodicLoop(0.8, 200)

    for x in range(0, 18):
        lights[x].set_state(light_gorgeous)
    await loop.next()

    for x in range(0, 30):
        screen1[x % 3].set_state(good_purple)
        screen1[(x - 1) % 3].set_state(light_gorgeous)

        screen2[x % 5].set_state(good_purple)
        screen2[(x - 1) % 5].set_state(light_gorgeous)

        screen3[x % 3].set_state(good_purple)
        screen3[(x - 1) % 3].set_state(light_gorgeous)

        screen4[x % 2].set_state(good_purple)
        screen4[(x - 1) % 2].set_state(light_gorgeous)

        screen5[x % 5].set_state(good_purple)
        screen5[(x - 1) % 5].set_state(light_gorgeous)
        await loop.next()


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
