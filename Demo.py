import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random
import pygame

'''
def main():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe", options=option)
    # driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    # driver.maximize_window()
    url = "https://www.wjx.cn/vm/QOuSHnC.aspx"
    driver.get(url)
'''


def main(driver):
    driver.get(url)
    # 1.是否养宠物
    s1 = "div[for^='q1_1']";
    # driver.find_element_by_css_selector(s1).click()
    driver.find_element(by=By.CSS_SELECTOR, value=s1).click()
    # 2.养了几只宠物
    num = numberOfPets()
    s2 = "div[for^=" + "'" + num + "'" + "]"

    driver.find_element(by=By.CSS_SELECTOR, value=s2).click()
    # driver.find_element_by_css_selector(s2).click()

    # time.sleep(0.5)
    # 3.宠物类别
    petType = typeOfPet(1)

    s3 = "div[for^=" + "'" + petType + "'" + "]"
    driver.find_element(by=By.CSS_SELECTOR, value=s3).click()
    # driver.find_element_by_css_selector(s3).click()

    # 4.宠物具体品种
    driver.find_element(by=By.ID, value="q4").send_keys(specificPet(petType))
    print()
    # driver.find_element_by_id("q4").send_keys(specificPet(type))
    # 5.宠物性别
    s5 = "div[for^=" + "'" + sexOfPet(petType, 1) + "'" + "]"
    driver.find_element(by=By.CSS_SELECTOR, value=s5).click()

    # 6.宠物年龄
    s6 = "div[for^=" + "'" + ageOfPet(1) + "'" + "]"
    driver.find_element(by=By.CSS_SELECTOR, value=s6).click()

    # time.sleep(0.5)
    if num != "q2_1":
        # 7.宠物2类别
        type2 = typeOfPet(2)

        s7 = "div[for^=" + "'" + type2 + "'" + "]"

        driver.find_element(by=By.CSS_SELECTOR, value=s7).click()
        # 8.宠物具体品种
        driver.find_element(by=By.ID, value="q8").send_keys(specificPet(type2))
        # 9.宠物2性别
        s9 = "div[for^=" + "'" + sexOfPet(type2, 2) + "'" + "]"
        driver.find_element(by=By.CSS_SELECTOR, value=s9).click()
        # 10.宠物年龄
        s10 = "div[for^=" + "'" + ageOfPet(2) + "'" + "]"
        driver.find_element(by=By.CSS_SELECTOR, value=s10).click()

    # 11.宠物主年龄
    s11 = ageOfOwner()

    driver.find_element(by=By.ID, value="q11").send_keys(s11)

    # 12.宠物主性别
    s12 = "div[for^=" + "'" + sexOfOwner() + "'" + "]"
    driver.find_element(by=By.CSS_SELECTOR, value=s12).click()
    # 13.宠物主学历
    driver.find_element(by=By.ID, value="q13").send_keys(profession())

    # time.sleep(1)
    # 14.宠物主城市
    driver.find_element(by=By.NAME, value="q14").send_keys(city(petType))
    # 15.宠物主收入
    s15 = "div[for^=" + "'" + income() + "'" + "]"
    driver.find_element(by=By.CSS_SELECTOR, value=s15).click()

    # 提交
    driver.find_element(by=By.ID, value="ctlNext").click()
    # 认证
    time.sleep(1)
    # driver.switch_to.alert.accept()

    # driver.switch_to.default_content()

    # driver.find_element_by_id("rectTop").click()
    m = driver.find_element(by=By.ID, value="rectTop")
    driver.execute_script("arguments[0].click();", m)
    time.sleep(7)

    # driver.close()


def test():
    ty = typeOfPet(1)
    # print(ty)
    sp = specificPet("q3_6")
    print(sp)


# function
# 2.养了几只宠物
def numberOfPets():
    percent = random.randint(0, 99)
    if percent < 17:
        return "q2_3"
    elif percent < 17 + 36:
        return "q2_2"
    else:
        return "q2_1"


# 3.主要宠物类型
def typeOfPet(i):
    percent = random.uniform(0, 1.79)
    if percent < 0.04:
        if i == 1:
            return "q3_8"
        else:
            return "q7_8"
    elif percent < 0.1:
        if i == 1:
            return "q3_7"
        else:
            return "q7_7"
    elif percent < 0.19:
        if i == 1:
            return "q3_6"
        else:
            return "q7_6"
    elif percent < 0.28:
        if i == 1:
            return "q3_5"
        else:
            return "q7_5"
    elif percent < 0.37:
        if i == 1:
            return "q3_4"
        else:
            return "q7_4"
    elif percent < 0.53:
        if i == 1:
            return "q3_3"
        else:
            return "q7_3"
    elif percent < 1.09:
        if i == 1:
            return "q3_2"
        else:
            return "q7_2"
    else:
        if i == 1:
            return "q3_1"
        else:
            return "q7_1"


# 4.宠物具体品种
def specificPet(t):
    if t == "q3_1" or t == "q7_1":
        r = random.randint(0, 131)
        if r < 18:
            return "橘猫"
        elif r < 32:
            return "白猫"
        elif r < 43:
            return "狸花猫"
        elif r < 52:
            return "黑猫"
        elif r < 59:
            return "奶牛猫(黑白)"
        elif r < 65:
            return "三花猫(黑白橘)"
        elif r < 69:
            return "玳瑁猫(黑橘)"
        elif r < 72:
            return "山东狮子猫"
        elif r < 83:
            return "英短蓝猫"
        elif r < 90:
            return "英短蓝白"
        elif r < 96:
            return "银渐层"
        elif r < 101:
            return "金渐层"
        elif r < 110:
            return "加菲猫"
        elif r < 117:
            return "美国短毛猫"
        elif r < 123:
            return "布偶猫"
        elif r < 127:
            return "暹罗猫"  # xian
        elif r < 130:
            return "苏格兰折耳猫"
        else:
            return "金吉拉"
    elif t == "q3_2" or t == "q7_2":
        r = random.randint(0, 115)
        if r < 17:
            return "哈士奇犬"
        elif r < 30:
            return "金毛寻回犬"
        elif r < 38:
            return "萨摩耶犬"
        elif r < 44:
            return "拉布拉多犬"
        elif r < 48:
            return "秋田犬"
        elif r < 51:
            return "边境牧羊犬"
        elif r < 53:
            return "德国牧羊犬"
        elif r < 55:
            return "阿拉斯加雪橇犬"
        elif r < 57:
            return "苏格兰牧羊犬"
        elif r < 58:
            return "古代牧羊犬"
        elif r < 65:
            return "柴犬"
        elif r < 71:
            return "中华田园犬"
        elif r < 73:
            return "松狮犬"
        elif r < 91:
            return "泰迪犬"
        elif r < 98:
            return "博美犬"
        elif r < 105:
            return "吉娃娃"
        elif r < 111:
            return "比熊犬"
        elif r < 113:
            return "迷你雪纳瑞"
        elif r < 115:
            return "蝴蝶犬"
        else:
            return "约克夏梗犬"
    elif t == "q3_3" or t == "q7_3":
        r = random.randint(0, 201)
        if r < 36:
            return "金鱼"
        elif r < 58:
            return "孔雀鱼"
        elif r < 79:
            return "锦鲤"
        elif r < 93:
            return "小丑鱼"
        elif r < 105:
            return "鹦鹉鱼"
        elif r < 117:
            return "七彩神仙鱼"
        elif r < 126:
            return "红箭鱼"
        elif r < 135:
            return "罗汉鱼"
        elif r < 144:
            return "霓虹灯鱼"
        elif r < 152:
            return "神仙鱼"
        elif r < 160:
            return "龙鱼"
        else:
            return "其它类型"
    elif t == "q3_4" or t == "q7_4":
        return "鹦鹉"
    elif t == "q3_5" or t == "q7_5":
        r = random.randint(0, 131)
        if r < 66:
            return "龟类"
        elif r < 104:
            return "蜥蜴类"
        elif r < 118:
            return "节肢类"
        else:
            return "蛇类"
    elif t == "q3_6" or t == "q7_6":
        r = random.randint(0, 160)
        if r < 23:
            return "荷兰兔"
        elif r < 40:
            return "迷你垂耳兔"
        elif r < 54:
            return "荷兰侏儒兔"
        elif r < 67:
            return "斑点兔"
        elif r < 80:
            return "荷兰垂耳兔"
        elif r < 91:
            return "安哥拉兔"
        elif r < 102:
            return "美国长毛垂耳兔"
        elif r < 113:
            return "公主兔"
        elif r < 123:
            return "波兰兔"
        else:
            return "其它可食用兔"
    elif t == "q3_7" or t == "q7_7":
        r = random.randint(0, 117)
        if r < 78:
            return "仓鼠"
        elif r < 101:
            return "龙猫"
        else:
            return "豚鼠"
    elif t == "q3_8" or t == "q7_8":
        other = ["雨蛙", "螃蟹", "剑齿虎", "东北虎", "皮卡丘", "卡比"]
        r = random.randint(0, 5)
        return other[r]
    else:
        return "寄"


# 5.宠物性别
def sexOfPet(t, index):
    i = random.randint(0, 99)
    if t == "q3_1" or "q7_1":
        if i < 64:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    elif t == "q3_2" or "q7_2":
        if i < 68:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    elif t == "q3_3" or "q7_3":
        if i < 55:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    elif t == "q3_4" or "q7_4":
        if i < 72:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    elif t == "q3_5" or "q7_5":
        if i < 42:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    elif t == "q3_6" or "q7_6":
        if i < 50:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    elif t == "q3_7" or "q7_7":
        if i < 51:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    elif t == "q3_8" or "q7_8":
        if i < 47:
            if index == 1:
                return "q5_1"
            else:
                return "q9_1"
        else:
            if index == 1:
                return "q5_2"
            else:
                return "q9_2"
    else:
        return "GG"


# 6.宠物年龄
def ageOfPet(index):
    i = random.randint(0, 99)
    if i < 7:
        if index == 1:
            result = "q6_1"
        else:
            result = "q10_1"
    elif i < 7 + 38:
        if index == 1:
            result = "q6_2"
        else:
            result = "q10_2"
    elif i < 7 + 38 + 27:
        if index == 1:
            result = "q6_3"
        else:
            result = "q10_3"
    elif i < 7 + 38 + 27 + 24:
        if index == 1:
            result = "q6_4"
        else:
            result = "q10_4"
    else:
        if index == 1:
            result = "q6_5"
        else:
            result = "q10_5"

    return result


# 11.宠物主年龄
def ageOfOwner():
    r = random.randint(0, 99)
    if r < 6:
        age = random.randint(47, 80)
    elif r < 12:
        age = random.randint(42, 47)
    elif r < 26:
        age = random.randint(37, 42)
    elif r < 53:
        age = random.randint(32, 37)
    elif r < 86:
        age = random.randint(27, 32)
    else:
        age = random.randint(0, 26)

    return age


# 12.宠物主性别
def sexOfOwner():
    r = random.randint(0, 99)
    if r < 39:
        return "q12_1"
    else:
        return "q12_2"


# 13.宠物主学历
def profession():
    r = random.randint(0, 99)
    if r < 3:
        result = "高中及以下"
    elif r < 3 + 15:
        result = "大学专科"
    elif r < 3 + 15 + 74:
        result = "大学本科"
    else:
        result = "研究生"

    return result


# 14.宠物主生活城市
def city(t):
    r = random.randint(0, 99)
    if t == "q3_1":
        if r < 32:
            # 一线城市
            city = randomCity(1)
        elif r < 32 + 28:
            # 新一线城市
            city = randomCity(11)
        elif r < 32 + 28 + 17:
            # 二线城市
            city = randomCity(2)
        elif r < 32 + 28 + 17 + 17:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    elif t == "q3_2":
        if r < 28:
            # 一线城市
            city = randomCity(1)
        elif r < 28 + 27:
            # 新一线城市
            city = randomCity(11)
        elif r < 28 + 27 + 19:
            # 二线城市
            city = randomCity(2)
        elif r < 28 + 27 + 19 + 16:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    elif t == "q3_3":
        if r < 33:
            # 一线城市
            city = randomCity(1)
        elif r < 33 + 22:
            # 新一线城市
            city = randomCity(11)
        elif r < 33 + 22 + 20:
            # 二线城市
            city = randomCity(2)
        elif r < 33 + 22 + 20 + 14:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    elif t == "q3_4":
        if r < 31:
            # 一线城市
            city = randomCity(1)
        elif r < 31 + 26:
            # 新一线城市
            city = randomCity(11)
        elif r < 31 + 26 + 17:
            # 二线城市
            city = randomCity(2)
        elif r < 31 + 26 + 17 + 18:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    elif t == "q3_5":
        if r < 37:
            # 一线城市
            city = randomCity(1)
        elif r < 37 + 22:
            # 新一线城市
            city = randomCity(11)
        elif r < 37 + 22 + 20:
            # 二线城市
            city = randomCity(2)
        elif r < 37 + 22 + 20 + 12:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    elif t == "q3_6":
        if r < 32:
            # 一线城市
            city = randomCity(1)
        elif r < 32 + 25:
            # 新一线城市
            city = randomCity(11)
        elif r < 32 + 25 + 18:
            # 二线城市
            city = randomCity(2)
        elif r < 32 + 25 + 18 + 14:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    elif t == "q3_7":
        if r < 38:
            # 一线城市
            city = randomCity(1)
        elif r < 38 + 26:
            # 新一线城市
            city = randomCity(11)
        elif r < 38 + 26 + 15:
            # 二线城市
            city = randomCity(2)
        elif r < 38 + 26 + 15 + 16:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    elif t == "q3_8":
        if r < 39:
            # 一线城市
            city = randomCity(1)
        elif r < 39 + 18:
            # 新一线城市
            city = randomCity(11)
        elif r < 39 + 18 + 19:
            # 二线城市
            city = randomCity(2)
        elif r < 39 + 18 + 19 + 12:
            # 三线城市
            city = randomCity(3)
        else:
            # 其它城市
            city = randomCity(0)
    return city


# 15.家庭月收入
def income():
    r = random.randint(0, 99)

    if r < 5:
        return "q15_1"
    elif r < 28:
        return "q15_2"
    elif r < 68:
        return "q15_3"
    elif r < 87:
        return "q15_4"
    else:
        return "q15_5"


# 随机城市
def randomCity(i):
    firstTierCity = ["北京", "上海", "广州", "深圳"]
    newFirstTierCity = ["成都", "杭州", "重庆", "武汉", "西安", "苏州",
                        "天津", "南京", "长沙", "郑州", "东莞", "青岛", "沈阳", "宁波", "佛山"]
    secondTierCity = ["昆明", "福州", "无锡", "厦门", "哈尔滨", "长春",
                      "南昌", "济南", "宁波", "大连", "贵阳", "温州", "石家庄", "泉州",
                      "南宁", "金华", "常州", "珠海", "惠州", "嘉兴", "南通", "中山", "保定",
                      "兰州", "台州", "徐州", "太原", "绍兴", "烟台"]
    thirdTierCity = ["海口", "汕头", "潍坊", "扬州", "洛阳", "乌鲁木齐",
                     "临沂", "唐山", "镇江", "盐城", "湖州", "赣州", "漳州", "揭阳", "江门", "桂林",
                     "邯郸", "泰州", "济宁", "呼和浩特", "咸阳", "芜湖", "三亚", "阜阳", "淮安 遵义",
                     "银川", "衡阳", "上饶", "柳州", "淄博", "莆田", "绵阳", "湛江", "商丘", "宜昌",
                     "沧州", "连云港", "南阳", "蚌埠", "驻马店", "滁州", "邢台", "潮州", "秦皇岛", "肇庆",
                     "荆州", "周口", "马鞍山", "清远", "宿州", "威海", "九江", "新乡", "信阳", "襄阳",
                     "岳阳", "安庆", "菏泽", "宜春", "黄冈", "泰安", "宿迁", "株洲", "宁德", "鞍山",
                     "南充", "六安", "大庆", "舟山"]
    otherCity = ["常德", "渭南湖", "孝感", "丽水", "运城", "德州",
                 "张家口", "鄂尔多斯", "阳江", "泸州", "丹东", "曲靖", "乐山", "许昌", "湘潭",
                 "晋中", "安阳", "齐齐哈尔", "北海", "宝鸡", "抚州", "景德镇", "延安", "三明",
                 "抚顺亳州", "日照", "西宁", "衢州", "", "拉萨", "淮北", "焦作", "平顶山", "滨州",
                 "吉安", "濮阳", "眉山", "池州", "荆门", "铜仁", "长治", "衡水", "铜陵", "承德",
                 "达州", "邵阳", "德阳", "龙岩", "南平", "淮南", "黄石", "营口", "东营", "吉林",
                 "韶关", "枣庄", "包头", "怀化", "宣城", "临汾", "聊城", "梅州", "盘锦", "锦州",
                 "榆林", "玉林", "十堰", "汕尾", "咸宁", "宜宾", "永州", "益阳", "黔南州", "黔东南",
                 "恩施", "红河", "大理", "大同", "鄂州", "忻州", "吕梁", "黄山", "开封", "郴州",
                 "茂名", "漯河", "葫芦岛", "河源", "娄底"]

    if i == 1:
        r = random.randint(0, len(firstTierCity) - 1)
        result = firstTierCity[r]
    elif i == 11:
        r = random.randint(0, len(newFirstTierCity) - 1)
        result = newFirstTierCity[r]
    elif i == 2:
        r = random.randint(0, len(secondTierCity) - 1)
        result = secondTierCity[r]
    elif i == 3:
        r = random.randint(0, len(thirdTierCity) - 1)
        result = thirdTierCity[r]
    else:
        r = random.randint(0, len(otherCity) - 1)
        result = otherCity[r]

    return result


if __name__ == "__main__":

    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)

    # driver = webdriver.Chrome(service=Service(executable_path="C:\ProgramFiles\Google\Chrome\Application\chromedriver.exe"))
    # driver = webdriver.Chrome("C:\ProgramFiles\Google\Chrome\Application\chromedriver.exe", options=option)

    driver = webdriver.Edge(service=Service(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application"
                                                            "\msedgedriver.exe"))
    # driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
    })
    # driver.maximize_window()
    url = "https://www.wjx.cn/vm/QOuSHnC.aspx"
    i = 0
    count = 0

    # 播放音乐
    filePath = "./6872015.flac"
    pygame.mixer.init()
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play()

    while i < 50:
        count = i + 1
        print(count)
        main(driver)
        i = i + 1
    driver.quit()
    pygame.mixer.music.stop()

'''
    newTab = 'window.open("https://www.wjx.cn/vm/QOuSHnC.aspx")'
    driver.execute_script(newTab)
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    # 切换IP

    main(driver)

'''

'''
    i = 0
    print("起飞---------------------------")
    count = ""
    while i < 50:
        main()
        count = str(i + 1)
        print("你已经刷了" + count + "次，还剩下 999... 次，加油！")
        i = i + 1
        time.sleep(2)
'''
