import yaml
import asyncio
import time
import random
from utilities import reset_all

from light import Light

from patterns.progression import progression

test_pattern = None


def decode_position(pos):
    panel_index = int(pos[0]) - 1
    row = ord('x') - ord(pos[1])
    col = int(pos[2]) - 1
    panels = [(0, 2.25), (19, 2.25), (41, 2.675), (62, 2.675), (92, 2.53125)]
    panel = panels[panel_index]
    return (panel[0] + panel[1] * col, row * 3)


async def control_loop(lights):
    if test_pattern:
        await test_pattern(lights)
        reset_all(lights)
        await asyncio.sleep(1)
    else:
        while True:
            all_patterns = [progression]
            for pattern in all_patterns:
                reset_all(lights)
                await pattern(lights)


async def main():
    with open("ips.yml", "r") as file:
        ips = yaml.safe_load(file)

    lights = [Light(ip, decode_position(pos)) for ip, pos in ips.items()]

    await asyncio.gather(*[light.connect() for light in lights])

    await asyncio.gather(control_loop(lights),
                         *[light.comm_loop() for light in lights])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
