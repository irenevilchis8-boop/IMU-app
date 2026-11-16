import asyncio
from bleak import BleakClient

ADDRESS = "FF:3F:7B:9C:51:25"

async def main():

    async with BleakClient(ADDRESS) as client:

        print("CONNECTED:", client.is_connected)

        for service in client.services:

            print("\nSERVICE")
            print(service.uuid)

            for char in service.characteristics:

                print("CHAR:", char.uuid)
                print("PROPS:", char.properties)

asyncio.run(main())
