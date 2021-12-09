import asyncio
import random

from utilities import *


async def twinkle(lights):
    background_color = rgb(32, 32, 255)
    twinkle_colors = [pretty, warm_white, blue_snowy, good_purple]

    for light in lights:
        light.set_state(background_color)

    states = [None for light in lights]

    time_step = 0.1
    loop = PeriodicLoop(time_step, 600)

    while not loop.done():
        for i in range(len(lights)):
            if states[i]:
                states[i] -= time_step
                if states[i] <= 0:
                    states[i] = None
                    light.set_state(background_color)
        if random.uniform(0, 1) < 0.1:
            i = random.choice(range(len(lights)))
            if not states[i]:
                states[i] = random.uniform(0.2, 1)
                lights[i].set_state(random.choice(twinkle_colors))
        await loop.next()
