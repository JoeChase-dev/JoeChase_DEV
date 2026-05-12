"""协程版本（await同步调用）"""
import asyncio
async def crawl_page(url):
    print(f"crawling {url}")
    sleep_time = int(url.split("_")[-1])
    await asyncio.sleep(sleep_time)
    print(f"OK {url}")
async def main(urls):
    for url in urls:
        await crawl_page(url)

asyncio.run(main(["url_1", "url_2", "url_3", "url_4"]))
# 总耗时仍然是10秒，因为await是阻塞的！
# 相当于用异步接口写了同步代码