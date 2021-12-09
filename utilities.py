import asyncio
import math
import time

from pywizlight.rgbcw import rgb2rgbcw


def index(p):
    return p[0] * 4 + p[1]


def in_bounds(p):
    return p[0] >= 0 and p[0] < 4 and p[1] >= 0 and p[1] < 4


def flipped(v):
    return [-v[0], -v[1]]


def equal(a, b):
    return round(a[0]) == round(b[0]) and round(a[1]) == round(b[1])


def reset_all(lights):
    for light in lights:
        light.set_state(off)


class PeriodicLoop:
    def __init__(self, period, length=None):
        self.period = period
        self.next_frame_time = time.perf_counter()
        if length:
            self.finish_time = self.next_frame_time + length
        else:
            self.finish_time = None

    async def next(self):
        self.next_frame_time += self.period
        now = time.perf_counter()
        await asyncio.sleep(self.next_frame_time - now)

    def done(self):
        if self.finish_time:
            return self.next_frame_time >= self.finish_time
        return False


def raw_rgb(r, g, b):
    return {'r': r, 'g': g, 'b': b}


def rgb(r, g, b):
    rgb, cw = rgb2rgbcw((r, g, b))
    red, green, blue = rgb
    state = {'r': r, 'g': g, 'b': b}
    if cw:
        state['c'] = cw
        state['w'] = cw
    return state


def color(c):
    return rgb(round(c.red * 255), round(c.green * 255), round(c.blue * 255))


def dim(c, intensity):
    return {**c, 'brightness': intensity}


on = {'c': 255, 'w': 255}
off = None

cold_white = {'c': 255}
warm_white = {'w': 255}

light_gorgeous = rgb(128, 0, 255)
gorgeous = rgb(160, 0, 255)
snowy = raw_rgb(32, 0, 255)
pretty = raw_rgb(255, 0, 192)
good_purple = raw_rgb(123, 0, 255)

palette = [light_gorgeous, gorgeous, snowy, pretty, good_purple]

# prominent_lights = ['5l4', '2r8', '4h4']
prominent_lights = [14, 16, 9]
