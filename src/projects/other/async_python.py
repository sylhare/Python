# aiohttp for http request, same api as requests
# asyncio for coroutines


if __name__ == '__main__':
    import asyncio


    async def hello():
        print("Hello")
        await asyncio.sleep(1)
        print("World!")


    async def main():
        await asyncio.gather(hello(), hello(), hello())


    asyncio.run(main())
