# -*- coding: utf-8 -*-

# 引入用于爬虫的一个包urllib2
import urllib2

# 引入正则表达式的包
import re

def loadpage(url):
  '''
    对爬虫进行伪装，并爬取一个页面的所有内容
  '''
  # 浏览器的user_agent，用市面上浏览器的这个参数
  user_agent = 'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
  header = {'User-Agent':user_agent}
  #创建访问请求
  req = urllib2.Request(url,headers = header)
  #打开指定的url
  response  = urllib2.urlopen(req)
  #读取url的内容
  result = response.read()
  return result

def specialcontent(result):
  '''
    爬取页面指定内容,如贴吧中的帖子详情
  '''
  #撰写正则表达式
  content = re.compile(r'<div class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>',re.S)
  #用正则表达式抓取指定内容
  item_list = content.findall(result)
  #将一个结果转成一个String，并汇总成一个大的String
  s = '/n'
  for i in item_list:
    s = s + str(i)
  return s
    
    
def write_to_file(file_name,txt):
  '''
    将txt文本存入到file_name文件中
  '''
  print('正在存储文件'+file_name)
  # 打开文件
  f = open(file_name,'w')
  #将结果写入文件
  f.write(txt)
  #关闭文件
  f.close()


def tieba_spider(url, begin_page,end_page):
  '''
    构造每一个页面的url
  '''
  for i in range(begin_page,end_page+1):
    #经观察，页面编码和pn=后面的数据具有规律
    pn = 50*(i - 1)
    #构造完整的页面url
    urlreq = url+str(pn) 
    #爬取该页面的内容
    result = loadpage(urlreq)
    #将结果存入文件
    file_name = str(i)+'.txt'
    content = specialcontent(result)
    write_to_file(file_name,content)
    

if __name__ == '__main__':
  '''
    输入要爬网页的url和起止页码
  '''
  #输入要爬取的一系列网页url中固定不变的部分
  url  = raw_input('Please input url:')
  #输入起始页码
  begin_page = int(raw_input('Please begin page:'))
  #输入截止页码
  end_page = int(raw_input('Please end page:'))
  #爬取一系列网页

  tieba_spider(url,begin_page,end_page)
