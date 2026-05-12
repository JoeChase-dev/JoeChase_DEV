import asyncio

async def crawl_page(url):
    print(f"crawling{url}")
    sleep_time = int(url.split("_")[-1])
    await asyncio.sleep(sleep_time)
    print(f"{url} OK")

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task

# asyncio.run(main(["url_1", "url_2", "url_3", "url_4"]))

async def main_gather(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main_gather(["url_1", "url_2", "url_3", "url_4"]))