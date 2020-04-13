import requests
import pandas as pd
import random



URL = pd.read_excel('D:\MyFiles\ChromeDownload\全球气象数据下载链接.xlsx')
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'
          }

proxies = {
            'http':'171.13.201.132:9999',
            'https':'171.13.201.132:9999'
          }

def get_data(start,end):
  for d in range(int(start),int(end)):
      all_df = []
      for num in range(1,34):
          url=URL.iat[d,1] + '&np=' + str(num)
          print(url)

          html=requests.get(url, headers=headers)# timeout=5，即5秒后超时
          #如果报错TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应,连接尝试失败。
          #尝试添加timeout参数
          #或者添加proxies=proxies参数，即再定义代理,在代理IP网站中查找免费代理IP
          test=html.text

          df_in_list=pd.read_html(test) 
          df = df_in_list[0]

          all_df.append(df)
      all_df = pd.concat(all_df,ignore_index=True)    
    
      all_df.to_excel("9_" + URL.iat[d,0].strftime('%Y%m%d') + '-' + URL.iat[d,0].strftime('%Y%m%d') +'_' + str(random.randint(100000,999999)) + ".xls",index=False)


if __name__ == '__main__':
    start = input('请输入你要下载的起始行：\n')
    end = input('请输入你要下载的结束行：\n')
    get_data(start,end)