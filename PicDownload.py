import os
import re

import requests
import json
import ast
import my_fake_useragent

from urllib.request import urlretrieve


artist = re.compile(r'P站画师:(.*?)\n', re.S)
picID = re.compile(r'ID:([0-9]*)')

def main():
    baseApi = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=0&host_uid="
    # UP 信息
    host_uid = "438550870"
    offset_dynamic_id = "0"
    askApi = baseApi + host_uid + "&offset_dynamic_id=" + offset_dynamic_id + "&need_top=1&platform=web"

    startDate = ""
    endDate = ""
    filePath = "D:\Laffey\Desktop\picTest"
    response = getHtml(askApi)
    downloadLinks, offset_dynamic_id = parser(response.text)

    downLoad(downloadLinks, filePath)



# 打开一个浏览器
''' def getDriver():
    driver = webdriver.Chrome(
        service=Service(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe"))
    return driver '''


# 获取响应内容
def getHtml(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "cookie": "l=v; buvid3=37C23B61-44EF-78D6-8A55-44C83EB0517602766infoc; i-wanna-go-back=-1; b_ut=7; CURRENT_BLACKGAP=0; CURRENT_FNVAL=80; nostalgia_conf=-1; innersign=0"
    }
    try:
        response = requests.get(url=url, headers=head)  # 响应则返回状态码200
    except Exception as e:
        return "ERROR"

    return response


# 解析获取下载链接及ID，画师等信息
def parser(text):
    # 将json对象转换为python对象
    data = json.loads(text)
    # 图片链接

    save = []
    for o in data['data']['cards']:
        card = o['card']
        card = json.loads(card)
        if list(card.keys())[0] == 'item':
            each = []
            for p in card['item']['pictures']:
                img = p['img_src']
                each.append(img)
                des = card['item']['description']
                art = artist.findall(des)[0]
                each.append(art)
                pic_id = picID.findall(des)[0]
                each.append(pic_id)
            save.append(each)
    # 下一页页偏移值
    next_offset = data['data']['next_offset']

    return save, str(next_offset)



# 传入下载链接和保存路径
def downLoad(links, path):
    for item in links:
        i = 0
        index = 1
        while i < len(item):
            urlretrieve(item[i], path + '\\' + item[i+1] + '-' + item[i+2] + '-' + str(index) + '.jpg')
            index = index + 1
            i = i + 3



if __name__ == '__main__':
    main()

