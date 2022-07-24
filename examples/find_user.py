import asyncio

from destiny_api_client import DestinyClient



async def main():
    client = DestinyClient()
    await client.say_hello()


if __name__ == '__main__':
    asyncio.run(main())