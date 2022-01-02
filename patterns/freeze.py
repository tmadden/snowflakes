import asyncio
import random

from utilities import *


async def freeze(lights):
    background_color = rgb(32, 32, 255)
    colors = [rgb(255, 0, 64), snowy, warm_white, gorgeous, good_purple]

    for light in lights:
        light.set_state(background_color)

    frozen_lights = set()
    freezing_lights = {}

    def propagate_freeze(index, color, time):
        if index in frozen_lights:
            return
        if index in freezing_lights:
            if time >= freezing_lights[index]['time']:
                return
        freezing_lights[index] = {'time': time, 'color': color}

    # Continue propagating the freeze until all the lights are frozen.
    async def do_propagation_loop(speed):
        nonlocal frozen_lights
        nonlocal freezing_lights
        update_period = 0.05
        loop = PeriodicLoop(update_period)
        while len(frozen_lights) < len(lights):
            for index in list(freezing_lights.keys()):
                freezing = freezing_lights[index]
                freezing['time'] -= update_period
                if freezing['time'] <= 0:
                    lights[index].set_state(freezing['color'])
                    for neighbor in neighbors[index]:
                        propagate_freeze(
                            neighbor, freezing['color'],
                            light_distance(lights[index], lights[neighbor]) /
                            speed)
                    del freezing_lights[index]
                    frozen_lights.add(index)
            await loop.next()
        # Reset the state.
        frozen_lights = set()
        freezing_lights = {}

    for count in range(60):
        # Seed the reset.
        for index in range(4):
            freezing_lights[index] = {'time': 0, 'color': background_color}

        # Wait for the reset to finish propagating.
        await do_propagation_loop(250)
        await asyncio.sleep(1)

        # Select the freeze color and starting point.
        seeds = {}
        for i in range(random.choice([2, 2, 3, 3, 1])):
            starting_index = random.choice(
                [i for i in range(len(lights)) if i not in seeds])
            freeze_color = random.choice([
                color for color in colors
                if color != lights[starting_index].get_state()
                and color not in seeds.values()
            ])
            seeds[starting_index] = freeze_color

        # Show the seeds.
        for index, color in seeds.items():
            lights[index].set_state(color)
            await asyncio.sleep(0.2)

        await asyncio.sleep(1)

        # Seed the freeze.
        for index, color in seeds.items():
            freezing_lights[index] = {'time': 0, 'color': color}

        # Wait for the freeze to finish propagating.
        await do_propagation_loop(125)

        # Add a little delay between freezes.
        await asyncio.sleep(2)
