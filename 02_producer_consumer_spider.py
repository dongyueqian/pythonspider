
import blog_spider
import queue
import time
import threading
import random

# 生产者
def do_craw(url_queue:queue.Queue, html_queue:queue.Queue):
    '''
    :param url_queue: 存放url的队列
    :param html_queue: 存放html页面的队列
    :return:
    '''
    while True:
        url = url_queue.get() # 获取url_queue中的url
        html = blog_spider.crew(url) # 获取url对应的网页
        html_queue.put(html) # 将网页放在html_queue队列中
        print(threading.current_thread().name, f"craw {url}", "url_queue.size=", url_queue.qsize())
        time.sleep(random.randint(1, 2))


# 消费者
def do_parser(html_queue:queue.Queue, file_out):
    while True:
        html = html_queue.get() # 获取html_queue中的网页
        results = blog_spider.parser(html)  # 解析html，得到一个「链接+标题」的tuple
        for result in results:
            file_out.write(str(result) + "\n")  # 将得到的「链接+标题」写入文件

        print(threading.current_thread().name, f"results.size", len(results), "html_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1,2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)
    # 启动3个生产者线程
    for index in range(3):
        thread = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{index}") # name=f"craw{index}"线程名
        thread.start()

    file_out = open("02_data.txt", "w")
    # 启动2个消费者线程
    for index in range(2):
        thread = threading.Thread(target=do_parser, args=(html_queue, file_out), name=f"parse{index}")
        thread.start()