# import asyncio

# async def greet(n):
#     await asyncio.sleep(3)
#     return n*n

# async def main():
#     res = await asyncio.gather(
#         greet(2),
#         greet(3),
#         greet(4)
#     )
#     print(res)

# asyncio.run(main())

import asyncio

async def main():
    task = asyncio.create_task(fn2())
    print("one")
    print("four")
    await asyncio.sleep(1)
    print("five")

async def fn2():
    await asyncio.sleep(1)
    print("two")

asyncio.run(main())
    

