import yaml
import asyncio

from pywizlight import discovery


async def main():
    with open("lights.yml", "r") as file:
        lights = yaml.safe_load(file)

    bulbs = await discovery.discover_lights(broadcast_space="192.168.11.255")
    # print([(bulb.ip, bulb.mac) for bulb in bulbs])

    ips = []
    for mac, pos in lights.items():
        print(mac)
        ip = next(bulb.ip for bulb in bulbs if bulb.mac == mac)
        ips.append({'ip': ip, 'pos': pos})

    with open('ips.yml', 'w') as file:
        yaml.dump(ips, file, default_flow_style=False)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
