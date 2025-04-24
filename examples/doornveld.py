#!/usr/bin/env python

import argparse
import asyncio
import logging
import sys

from velbusaio.controller import Velbus
from velbusaio.velbusfast import VelbusFast

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--connect", help="Connection string", required=True)
# parser.add_argument("--address", help="Address of the module to load", required=True)
args = parser.parse_args()


async def main(connect_str: str):
    # velbus = Velbus(dsn=connect_str)
    velbus = VelbusFast(destination=connect_str)
    cache_dir = velbus.get_cache_dir()
    print("Cache dir: {}".format(cache_dir))

    await velbus.connect()
    await velbus.start()
    for mod in (velbus.get_modules()).values():
        print(mod)
        print("")
    await velbus.stop()


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger("asyncio").setLevel(logging.DEBUG)
asyncio.run(main(args.connect), debug=True)
