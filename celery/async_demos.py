# import asyncio
# import time
# from time import sleep
#
#
# async def f1():
#     for i in range(5):
#         print(f"f1({i})")
#         # sleep(1.5)
#         await asyncio.sleep(1.5)
#
#
# async def f2():
#     for i in range(5):
#         print(f"f2({i})")
#         # sleep(1)
#         await asyncio.sleep(1)
#
#
# async def main():
#     await asyncio.gather(
#         f1(),
#         f2(),
#     )
#
#
# start = time.time()
# # main()
# asyncio.run(main())  # 7.549298286437988
#
# end = time.time()
# print(end - start)   # 12.541394472122192
