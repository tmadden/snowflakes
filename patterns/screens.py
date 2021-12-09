from utilities import *


async def screens(lights):
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
