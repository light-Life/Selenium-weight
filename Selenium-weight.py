# !/usr/bin/python
# -*- coding:utf-8 -*-
# author: huayang
# time: 2021.10.12-2021.11.4
import re
import os
import time
import json
import xlwt
import requests
import threading
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)

print("""\033[0;36m请选择扫描的类型：
1 【单个扫描】
2 【批量扫描(url.txt)】
\033[0m""")
choice = input('请输入数字:')
if choice == '1':
    url = input('url:')
    if 'http://' in url:
        url = url[7:]
    elif 'https://' in url:
        url = url[8:]
    try:
        browser.get('https://www.aizhan.com/cha/' + url)

        html =  str(browser.page_source)

        Baidu_amount = re.findall('.*?baidurank_ip" class="red">(.*?)</span>.*?',html)#百度流量

        print('\033[1;32m百度流量\033[0m',Baidu_amount[0])

        Move_amout = re.findall('.*?baidurank_m_ip">(.*?)</span>.*?',html)#移动流量

        print('\033[1;32m移动流量\033[0m',Move_amout[0])

        Baidu = re.findall('.*?//statics.aizhan.com/images/br/(.*?).png.*?', html)#百度权重

        print('\033[1;32m百度权重\033[0m',Baidu[0])

        Move = re.findall('.*?//statics.aizhan.com/images/mbr/(.*?).png.*?',html)#移动权重

        print('\033[1;32m移动权重\033[0m',Move[0])

        Google = re.findall('.*?//statics.aizhan.com/images/pr/(.*?).png.*?',html)#谷歌权重

        print('\033[1;32m谷歌权重\033[0m',Google[0])

        Qihu360 = re.findall('.*?//statics.aizhan.com/images/360/(.*?).png.*?',html)#360权重

        print('\033[1;32m360权重\033[0m',Qihu360[0])

        Shenma = re.findall('.*?//statics.aizhan.com/images/sm/(.*?).png.*?', html)#神马权重

        print('\033[1;32m神马权重\033[0m',Shenma[0])

        Sougou = re.findall('.*?//statics.aizhan.com/images/sr/(.*?).png.*?', html)#搜狗权重

        print('\033[1;32m搜狗权重\033[0m',Sougou[0])

        Beian = re.findall('.*?icp_icp">(.*?)</a>.*?', html)#备案信息

        print('\033[1;32m备案信息\033[0m',Beian[0])

        Xingzhi = re.findall('.*?id="icp_type">(.*?)</span>.*?', html)#性质

        print('\033[1;32m性质\033[0m',Xingzhi[0])

        Mingcheng = re.findall('.*?icp_company">(.*?)</span>.*?', html)#名称

        print('\033[1;32m名称\033[0m',Mingcheng[0])

    except:
        pass

elif choice == '2':
    if os.access("url.txt", os.F_OK):
        print('\033[1;32m>>>已检测到url.txt存在<<<\033[0m\n')
        print("""\033[0;34m请选择导出类型：
        1 【导出可用纯域名(按照补天规则:爱站权重百度1、移动1、谷歌3)】
        2 【导出完整的权重文件.xls】\033[0m""")
        choice = input('请输入数字:')
        if choice == '1':
            localtime = time.localtime(time.time())
            time = time.strftime("%Y%m%d%H%M%S", time.localtime())
            print('\n\033[1;32m[+]正在创建'+time+'.txt\033[0m')
            urls = open('url.txt')
            for i in urls.readlines():
                url = i.rstrip("\n")
                if url == '': #避免空字符
                    break
                else:
                    if 'http://' in url:
                        url = url[7:]
                    elif 'https://' in url:
                        url = url[8:]
                    try:
                        print('\n\033[1;31m》》》\033[0m'+url+'\033[1;31m《《《\033[0m\n')

                        browser.get('https://www.aizhan.com/cha/' + url)

                        html = str(browser.page_source)

                        Baidu_amount = re.findall('.*?baidurank_ip" class="red">(.*?)</span>.*?', html)  # 百度流量

                        print('\033[1;32m百度流量\033[0m', Baidu_amount[0])

                        Move_amout = re.findall('.*?baidurank_m_ip">(.*?)</span>.*?', html)  # 移动流量

                        print('\033[1;32m移动流量\033[0m', Move_amout[0])

                        Baidu = re.findall('.*?//statics.aizhan.com/images/br/(.*?).png.*?', html)  # 百度权重

                        print('\033[1;32m百度权重\033[0m', Baidu[0])

                        Move = re.findall('.*?//statics.aizhan.com/images/mbr/(.*?).png.*?', html)  # 移动权重

                        print('\033[1;32m移动权重\033[0m', Move[0])

                        Google = re.findall('.*?//statics.aizhan.com/images/pr/(.*?).png.*?', html)  # 谷歌权重

                        print('\033[1;32m谷歌权重\033[0m', Google[0])

                        Qihu360 = re.findall('.*?//statics.aizhan.com/images/360/(.*?).png.*?', html)  # 360权重

                        print('\033[1;32m360权重\033[0m', Qihu360[0])

                        Shenma = re.findall('.*?//statics.aizhan.com/images/sm/(.*?).png.*?', html)  # 神马权重

                        print('\033[1;32m神马权重\033[0m', Shenma[0])

                        Sougou = re.findall('.*?//statics.aizhan.com/images/sr/(.*?).png.*?', html)  # 搜狗权重

                        print('\033[1;32m搜狗权重\033[0m', Sougou[0])

                        Beian = re.findall('.*?icp_icp">(.*?)</a>.*?', html)  # 备案信息

                        print('\033[1;32m备案信息\033[0m', Beian[0])

                        Xingzhi = re.findall('.*?id="icp_type">(.*?)</span>.*?', html)  # 性质

                        print('\033[1;32m性质\033[0m', Xingzhi[0])

                        Mingcheng = re.findall('.*?icp_company">(.*?)</span>.*?', html)  # 名称

                        print('\033[1;32m名称\033[0m', Mingcheng[0])

                        if str(Baidu[0]) > '0':
                            #print(url)
                            with open('test.txt', 'a')as f:
                                f.write(str(url) + '\n')
                                print('\n\033[1;32m[+]正在写入:\033[0m', url)
                        elif str(Move[0]) > '0':
                            #print(url)
                            with open('test.txt', 'a')as f:
                                f.write(str(url) + '\n')
                                print('\n\033[1;32m[+]正在写入:\033[0m', url)
                        elif str(Google[0]) >= '3':
                            #print(url)
                            with open('test.txt', 'a')as f:
                                f.write(str(url) + '\n')
                            print('\n\033[1;32m[+]正在写入:\033[0m', url)
                    except:
                        pass
        elif choice == '2':
            if os.access("url.txt", os.F_OK):
                print('\033[1;32m>>>已检测到url.txt存在<<<\033[0m\n')
                if os.access("权重.xls", os.F_OK):
                    print('\n\033[1;31m[○･｀Д´･ ○]已存在"权重.xls",请更改后重试\033[0m\n')
                else:
                    urls = open('url.txt')
                    global number  # 定义一个全局变量
                    number = 1
                    workbook = xlwt.Workbook(encoding='utf-8')  # 工作簿
                    worksheet = workbook.add_sheet('网站权重')  # 工作表
                    # 创建颜色
                    pattern = xlwt.Pattern()  # 创建模式对象
                    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
                    pattern.pattern_fore_colour = 5  # 设置模式颜色
                    style = xlwt.XFStyle()  # 创建样式对象
                    style.pattern = pattern  # 将模式加入到样式对象
                    # 写入头部数据
                    worksheet.write(0, 0, '域名', style)
                    worksheet.write(0, 1, '百度流量', style)
                    worksheet.write(0, 2, '移动流量', style)
                    worksheet.write(0, 3, '百度权重', style)
                    worksheet.write(0, 4, '移动权重', style)
                    worksheet.write(0, 5, '谷歌权重', style)
                    worksheet.write(0, 6, '360权重', style)
                    worksheet.write(0, 7, '神马权重', style)
                    worksheet.write(0, 8, '搜狗权重', style)
                    worksheet.write(0, 9, '备案信息', style)
                    worksheet.write(0, 10, '性质', style)
                    worksheet.write(0, 11, '名称', style)

                    for i in urls.readlines():
                        url = i.rstrip("\n")
                        if url == '': #以免传入空字符
                            break
                        else:
                            if 'http://' in url: \
                                    url = url[7:]
                            elif 'https://' in url:
                                url = url[8:]

                            print('\n\033[1;31m》》》\033[0m' + url + '\033[1;31m《《《\033[0m\n')
                            worksheet.write(number, 0, i)

                            browser.get('https://www.aizhan.com/cha/' + url)

                            html = str(browser.page_source)

                            Baidu_amount = re.findall('.*?baidurank_ip" class="red">(.*?)</span>.*?', html)  # 百度流量

                            print('\033[1;32m百度流量\033[0m', Baidu_amount[0])
                            worksheet.write(number, 1, Baidu_amount[0])

                            Move_amout = re.findall('.*?baidurank_m_ip">(.*?)</span>.*?', html)  # 移动流量

                            print('\033[1;32m移动流量\033[0m', Move_amout[0])
                            worksheet.write(number, 2, Move_amout[0])

                            Baidu = re.findall('.*?//statics.aizhan.com/images/br/(.*?).png.*?', html)  # 百度权重

                            print('\033[1;32m百度权重\033[0m', Baidu[0])
                            worksheet.write(number, 3, Baidu[0])

                            Move = re.findall('.*?//statics.aizhan.com/images/mbr/(.*?).png.*?', html)  # 移动权重

                            print('\033[1;32m移动权重\033[0m', Move[0])
                            worksheet.write(number, 4, Move[0])

                            Google = re.findall('.*?//statics.aizhan.com/images/pr/(.*?).png.*?', html)  # 谷歌权重

                            print('\033[1;32m谷歌权重\033[0m', Google[0])
                            worksheet.write(number, 5, Google[0])

                            Qihu360 = re.findall('.*?//statics.aizhan.com/images/360/(.*?).png.*?', html)  # 360权重

                            print('\033[1;32m360权重\033[0m', Qihu360[0])
                            worksheet.write(number, 6, Qihu360[0])

                            Shenma = re.findall('.*?//statics.aizhan.com/images/sm/(.*?).png.*?', html)  # 神马权重

                            print('\033[1;32m神马权重\033[0m', Shenma[0])
                            worksheet.write(number, 7, Shenma[0])

                            Sougou = re.findall('.*?//statics.aizhan.com/images/sr/(.*?).png.*?', html)  # 搜狗权重

                            print('\033[1;32m搜狗权重\033[0m', Sougou[0])
                            worksheet.write(number, 8, Sougou[0])

                            Beian = re.findall('.*?icp_icp">(.*?)</a>.*?', html)  # 备案信息

                            print('\033[1;32m备案信息\033[0m', Beian)
                            worksheet.write(number, 9, Beian)

                            Xingzhi = re.findall('.*?id="icp_type">(.*?)</span>.*?', html)  # 性质

                            print('\033[1;32m性质\033[0m', Xingzhi)
                            worksheet.write(number, 10, Xingzhi)

                            Mingcheng = re.findall('.*?icp_company">(.*?)</span>.*?', html)  # 名称

                            print('\033[1;32m名称\033[0m', Mingcheng)
                            worksheet.write(number, 11, Mingcheng)

                            # 设置单元格的宽度
                            worksheet.col(0).width = 320 * 20
                            worksheet.col(1).width = 240 * 20
                            worksheet.col(2).width = 240 * 20
                            worksheet.col(9).width = 320 * 20
                            worksheet.col(11).width = 800 * 20

                            number = number + 1
                            # 保存文件
                        workbook.save('权重.xls')
        else:
            print('\n\033[3;31m哼塔[○･｀Д´･ ○]\033[0m')

    else:
        print('\n\033[3;31m[○･｀Д´･ ○]未检测到url.txt\033[0m')

else:
    print('\n\033[3;31m[○･｀Д´･ ○]\033[0m')

