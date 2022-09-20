import requests
from bs4 import BeautifulSoup
import lxml


#
# r = requests.get('http://www.santostang.com')
#
# print("文本编码:{}".format(r.encoding))
# print("响应状态码:{}".format(r.status_code))
# print("字符串方式的响应体:{}".format(r.text))

# key_dict = {'key1': 'value1', 'key2': 'value2'}
# rget = requests.get('http://httpbin.org/get', params=key_dict)
# print("URL已经正确编码:{}".format(rget.url))
# print("字符串方式的响应体:{}".format(rget.text))
#
# rpost = requests.post("http://httpbin.org/post", dataOpt=key_dict)
# print(rpost.text)

# link = 'http://www.santostang.com'
# rlink = requests.get(link, timeout=0.001)

def catch(i):
    link = 'https://test.longdaoyun.com/search/opportunity/?pageNumber={}'.format(i)
    headers = {
        "Host": "test.longdaoyun.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.169.400 QQBrowse"
    }

    rlink = requests.get(link, headers=headers)
    soup = BeautifulSoup(rlink.text, 'lxml')
    div_list = soup.find_all(attrs={'class': 'project'})
    for i in range(0, len(div_list)):
        div_project = div_list.__getitem__(i).find_next({'a'})
        print(div_project['href'])
        print(div_project.find_next('h4').text)


if __name__ == '__main__':
    for i in range(1, 5):
        catch(i)
