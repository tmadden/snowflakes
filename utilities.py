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

from math import sqrt


def light_distance(a, b):
    dx = a.p[0] - b.p[0]
    dy = a.p[1] - b.p[1]
    return sqrt(dx * dx + dy * dy)


def compute_neighbors(lights):
    import numpy as np

    points = np.array([light.p for light in lights])
    from scipy.spatial import Delaunay
    tris = Delaunay(points)

    # import matplotlib.pyplot as plt
    # plt.triplot(points[:, 0], points[:, 1], tris.simplices)
    # plt.plot(points[:, 0], points[:, 1], 'o')
    # for index, light in enumerate(lights):
    #     plt.text(light.p[0], light.p[1], str(index))
    # plt.show()

    def add_neighbors(i, j):
        neighbors[i].add(j)
        neighbors[j].add(i)

    neighbors = [set() for light in lights]
    for tri in tris.simplices:
        add_neighbors(tri[0], tri[1])
        add_neighbors(tri[1], tri[2])
        add_neighbors(tri[2], tri[0])
    return neighbors


neighbors = [{3, 5, 8, 9, 14}, {8, 11, 12}, {6, 9, 10, 13, 14, 15},
             {0, 10, 14, 15}, {5, 6, 7, 8, 11}, {0, 4, 6, 8, 9},
             {2, 4, 5, 7, 9, 13}, {4, 6, 11, 13, 16, 17}, {0, 1, 4, 5, 11},
             {0, 2, 5, 6, 14}, {2, 3, 13, 15, 16}, {1, 4, 7, 8, 12, 17},
             {1, 11, 17}, {2, 6, 7, 10, 16}, {0, 2, 3, 9, 15}, {3, 2, 10, 14},
             {17, 10, 13, 7}, {16, 11, 12, 7}]
