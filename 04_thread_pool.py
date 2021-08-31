import blog_spider
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.crew, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))

    for url,html in htmls:
        print(url, len(html))
print("获取网页完成")

# 网页解析
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = dict()
    for url, html in htmls:
        future = pool.submit(blog_spider.parser, html)
        futures[future] = url

    for future, url in futures.items():
        print(url, future.result())


