import asyncio
from bleak import BleakClient

ADDRESS = "FF:3F:7B:9C:51:25"

UUID_NOTIFY = "0000ffe4-0000-1000-8000-00805f9a34fb"

def callback(sender, data):

    print(data.hex())

async def main():

    async with BleakClient(ADDRESS) as client:

        print("Connected")

        await client.start_notify(
            UUID_NOTIFY,
            callback
        )

        while True:
            await asyncio.sleep(1)

asyncio.run(main())
