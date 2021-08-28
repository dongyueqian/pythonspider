import blog_spider
import threading
import time

def single_thread():
    print("单线程开始执行...")
    for url in blog_spider.urls:
        blog_spider.crew(url)
    print("单线程执行完成...")

def multi_threa():
    print("多线程开始执行...")
    threads = list()
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.crew, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("多线程执行完成...")

if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("单线程执行时间： ", end - start, "秒")
    print("=" * 50)
    start = time.time()
    multi_threa()
    end = time.time()
    print("多线程执行时间： ", end - start, "秒")
