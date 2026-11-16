# monitor.py

import asyncio

from wt901 import WT901BLE
from imu_gui import IMUGui
#from cube_visualizer import CubeVisualizer

ADDRESS = "FF:3F:7B:9C:51:25"


async def main():
    imu = WT901BLE(ADDRESS)

   # cube = CubeVisualizer()

    gui = IMUGui(imu)

    imu.set_gui(gui)

    await imu.connect()

    await imu.start_stream()

    while True:
        gui.root.update()
        #cube.update(
         #   imu.roll,
          #  imu.pitch,
           # imu.yaw
        #)
        await asyncio.sleep(0.05)


asyncio.run(main())
