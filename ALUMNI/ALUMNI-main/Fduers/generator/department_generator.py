import requests
import csv

def get_school_name():
    headers = {
    "Cookie": "JSESSIONID=289617D002DA1E5DBAB1F9B6851AB63C-memcached1; Path=/; HttpOnly",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; LLD-AL20 Build/HONORLLD-AL20)-SuperFriday_9.6.1",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Length": "146",
    "Host": "120.55.151.61",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    }
    data = "phoneModel=LLD-AL20&searchType=5&phoneBrand=HONOR&channel=huawei&page=1&platform=1&versionNumber=9.6.1&content=160027&phoneVersion=26&timestamp=0&"
    url = "http://120.55.151.61/V2/School/getUpdateSchoolList.action"
    #此处为在下课聊论坛处获取schoolID和学校名称的字典
    s = requests.Session()
    r = s.post(url = url,data = data,headers = headers)
    print(r.status_code)
    # print(r.text)
    school_text = r.text.replace("false","False")  #此处如果不替换会有关键字报错
    school_list = eval(school_text)["data"]["schoolBOs"]
    school_dict  = []
    for school in school_list:
        school_dict.append({"name":school["name"],"id":school['schoolId']})
    # print(school_dict)
    return school_dict

def get_school_content(s_list):
    
    s = requests.Session()
    school_dict_list = []
    print("爬取开始")
    for school in s_list:
        if school["name"] != "":
            # print(school["name"],school["id"])
            url = "http://120.55.151.61/V2/Academy/findBySchoolId.action"
            data = "phoneModel=LLD-AL20&phoneBrand=HONOR&schoolId=" + str(school["id"]) + "&channel=huawei&platform=1&versionNumber=9.6.1&phoneVersion=26&"
#             data = "phoneModel=LLD-AL20&phoneBrand=HONOR&schoolId=" + '1001' + "&channel=huawei&platform=1&versionNumber=9.6.1&phoneVersion=26&"

            headers = {
                "Cookie": "JSESSIONID=289617D002DA1E5DBAB1F9B6851AB63C-memcached1; Path=/; HttpOnly",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; LLD-AL20 Build/HONORLLD-AL20)-SuperFriday_9.6.1",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content-Length": "113",
                "Host": "120.55.151.61",
                "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
            }
            r = s.post(url = url,data = data,headers = headers)
            content = eval(r.text)["data"]
            temp_list = []
#             print(r.text)
            for item in content:
                temp_list.append(item["name"])
            school_dict_list.append({"name":school["name"],"id":school["id"],"content":temp_list})
            
    print("爬取结束")
    return school_dict_list
    
def save1(school_dict_list):
    f = open(".\\data\\schoolMajor.txt","w")
    f.write(str(school_dict_list))
    f.close()
    
def save2(school_dict_list):
    f = open(".\\data\\schoolMajor.csv","w")
    csv_writer = csv.writer(f)
    csv_writer.writerow(["大学","schoolID","院系"])
    for school in school_dict_list:
        contentList = [school["name"],school["id"]]
        contentList.extend(school["content"])
        csv_writer.writerow(contentList)
    f.close()
    
# a = [{"name":"清华大学","id":"1001"},{"name":"清华大学","id":"1001"}]
a = get_school_name()
for school in a:
    print(school)
b = get_school_content(a)
save2(b)