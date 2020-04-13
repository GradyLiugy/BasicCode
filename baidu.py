import requests
import re
import os
import time

# 获取图片url连接
def get_parse_page(pn,name):

    for i in range(int(pn)):
        # 1.获取网页
        print('正在获取第{}页'.format(i+1))

        # 百度图片首页的url
        # name是你要搜索的关键词
        # pn是你想下载的页数

        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' %(name,i*20)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}

        # 发送请求，获取相应
        response = requests.get(url, headers=headers)
        html = response.content.decode()
        # print(html)

        # 2.正则表达式解析网页
        # "objURL":"http://n.sinaimg.cn/sports/transform/20170406/dHEk-fycxmks5842687.jpg"
        results = re.findall('"objURL":"(.*?)",', html) # 返回一个列表

        # 根据获取到的图片链接，把图片保存到本地
        save_to_txt(results, name, i)


# 保存图片到本地
def save_to_txt(results, name, i):

    j = 0
    # 在当目录下创建文件夹
    if not os.path.exists(r'D:\MyFiles\My Code\baidu' + name):
        os.makedirs(r'D:\MyFiles\My Code\baidu' + name)

    # 下载图片
    for result in results:
        print('正在保存第{}个'.format(j))
        try:
            pic = requests.get(result, timeout=10)
            time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue

        # 可忽略，这段代码有bug
        # file_name = result.split('/')
        # file_name = file_name[len(file_name) - 1]
        # print(file_name)
        #
        # end = re.search('(.png|.jpg|.jpeg|.gif)$', file_name)
        # if end == None:
        #     file_name = file_name + '.jpg'

        # 把图片保存到文件夹
        file_full_name = r'D:\MyFiles\My Code\baidu' + name + '/' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)

        j += 1


if __name__ == '__main__':
    name = input('请输入你要下载的关键词：\n')
    pn = input('你想要下载前几页(1页有60张图片)？：\n')
    get_parse_page(pn,name)