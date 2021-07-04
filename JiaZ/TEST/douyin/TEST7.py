import requests
import json
# 抖音视频的URL
url="https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAU7ibxriLF-GSBF5QKa1Op9hxcMAPVmzmXwXqqvMfrhs&count=21&max_cursor=0&aid=1128&_signature=rrFSDQAAzq.dR1hiGSYhIa6xUh&dytk="
#url = "https://www.iesdouyin.com/share/user/3086470115?iid=MS4wLjABAAAAJeeaAiobNMXuEVSh-6ZtHXQlYpmok-Ad-Cs_Nm3nb0RXABRMuEu4WozPXsQwbp6t&with_sec_did=1&u_code=lcaf4kl86mf&sec_uid=MS4wLjABAAAAf0C1gFEdMvoFGiiMUZbYQeLVpezDCv4fyNjWk9W2myE&did=MS4wLjABAAAA8Dbj0aa9kUGqifhiyfPTtd6QTtCCy0Jl_eGsI-_pp0ohnO4BZncU1vue3DPqOZi8&timestamp=1623768446&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin"
headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}
#调用requests中的get获取抖音作者主页的网页链接
r = requests.get(url=url, headers=headers,stream=True)
#输出访问状态，如为<200>即为访问成功
print("初始访问状态:",r)
#使用json解析获取的网页内容
data_json = json.loads(r.text)
#使用json解析网页后，data_json的内容为dict格式，我们可以通过以下方式查看健名
print(data_json.keys())
#pd参数为布尔类型参数，data_json['aweme_list'] == []是为了判断'aweme_list'下一级内容是否为空，为空则为True
pd = data_json['aweme_list'] == []
#接下来使用循环来解决我们之前所提到的“隐藏内容”问题
while pd == True:
#只要“aweme_list”下一级内容为空，则反复访问作者主页链接，直到成功显示隐藏内容为止跳出循环
    r = requests.get(url=url, headers=headers,stream=True)
    data_json = json.loads(r.text)
    pd = data_json['aweme_list']== []
#下一级内容不为空，则访问下一级标签
for i in range(len(data_json['aweme_list'])):
    print(data_json['aweme_list'][i]['video']['play_addr_lowbr']['url_list'][0])