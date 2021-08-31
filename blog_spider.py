import requests
from bs4 import BeautifulSoup

# 以 f开头表示在字符串内支持大括号内的python表达式
urls = [
    f'https://www.cnblogs.com/#p{page}' for page in range(50,101)
]
# print(urls)


def crew(url):
    '''
    :param url: url链接
    :return: 网页
    '''
    r = requests.get(url)
    # print(url,len(r.text))
    return r.text
#
# for url in urls:
#     crew(url)

# 解析html
def parser(html):
    '''
    :param html: 网页
    :return: 链接+标题
    '''
    # class="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a',class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]

# parser(urls[0])

for result in parser(crew(urls[0])):
    print(result)