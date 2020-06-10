import requests
import json
from datetime import datetime
import pandas as pd
import time


class WxMps:

    def __init__(self, biz, appmsg_token, cookies, offset, city):
        self.biz = biz
        self.msg_token = appmsg_token
        self.offset = offset
        self.headers = {'Cookie': cookies,
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
                        }
        self.city = city

    def parse1(self, resp):
        # 控制下一个抓取的offset
        offset = resp.get('next_offset')
        # 将包含主要内容的list转为json格式
        general_msg_list = resp.get('general_msg_list')
        # 一个msg_list中含有10个msg
        msg_list = json.loads(general_msg_list)['list']
        df1 = pd.DataFrame(
            columns=['msg_id', 'post_time', 'msg_type', 'title', 'cover', 'author', 'digest', 'source_url',
                     'content_url'])
        # 循环message列表
        for msg in msg_list:
            # msg是该推送的信息，包含了comm_msg_info以及app_msg_ext_info两个信息，注意某一个推送中可能含有多个文章。
            comm_msg_info = msg.get('comm_msg_info')
            app_msg_ext_info = msg.get('app_msg_ext_info')

            # 该推送的id
            msg_id = comm_msg_info.get('id')
            # 该推送的发布时间，例如1579965567需要转化为datetime，datetime.fromtimestamp(1579965567)
            post_time = datetime.fromtimestamp(comm_msg_info['datetime'])
            # 该推送的类型
            msg_type = comm_msg_info.get('type')

            if app_msg_ext_info:
                # 推送的第一篇文章
                title, cover, author, digest, source_url, content_url = self.parse2(app_msg_ext_info)
                df2 = self.df_process(msg_id, post_time, msg_type, title, cover, author, digest, source_url,
                                      content_url)
                df1 = pd.concat([df1, df2])

                # 判断是不是多篇文章
                is_multi = app_msg_ext_info.get("is_multi")
                # 如果是1，继续爬取；如果是0，单条推送=只有一篇文章
                if is_multi:
                    multi_app_msg_item_list = app_msg_ext_info.get('multi_app_msg_item_list')
                    for information in multi_app_msg_item_list:
                        (title, cover, author, digest, source_url, content_url) = self.parse2(information)
                        df2 = self.df_process(msg_id, post_time, msg_type, title, cover, author, digest, source_url,
                                              content_url)
                        df1 = pd.concat([df1, df2])
        return df1, offset

    def start(self):
        offset = self.offset
        df1 = pd.DataFrame(
            columns=['msg_id', 'post_time', 'msg_type', 'title', 'cover', 'author', 'digest', 'source_url',
                     'content_url'])

        while offset <= 30:  # 自行修改
            print(offset)
            api = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz={0}&f=json&offset={1}&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=&wxton=&appmsg_token={2}&x5=0&f=json HTTP/1.1'.format(
                self.biz, offset, self.msg_token)
            resp = requests.get(api, headers=self.headers, verify=False).json()
            time.sleep(10)

            # ret 和 status 判断能不能继续抓取
            ret, status = resp.get('ret'), resp.get('errmsg')

            if ret == 0 or status == 'ok':
                print("Crawling : ok")
                print("\n")
                print("\n")
                df2, offset = self.parse1(resp)
                df1 = pd.concat([df1, df2])
                df1['city'] = self.city
            else:
                print("Before break, offset with problem is %d" % offset)
                break
        return df1

    def parse2(self, info):
        title = info.get('title')
        cover = info.get('cover')
        author = info.get('author')
        digest = info.get('digest')
        source_url = info.get('source_url')  # 原文地址
        content_url = info.get('content_url')  # 微信地址
        return (title, cover, author, digest, source_url, content_url)

    def df_process(self, msg_id, post_time, msg_type,
                   title, cover, author, digest, source_url, content_url):
        df = pd.DataFrame([msg_id, post_time, msg_type, title, cover,
                           author, digest, source_url, content_url]).T
        df.columns = ['msg_id', 'post_time', 'msg_type', 'title', 'cover', 'author', 'digest', 'source_url',
                      'content_url']
        return df


__biz = 'MzA5NDY5MzUzMQ=='
offset = 10
appmsg_token = 'vR3jX5BO2L%2BIFMMSUdyWdVyH9S3sPp9rN%2F%2BU80rBarff0ntDfe3RG5Pldtz93fl%2F'
cookies = 'wap_sid2=CJH2/8cHElxUUjMzOXBQLURJdzBrVUloY21sbUJ5cHNwX1dsUXQwYVh1U1hFVGF2WjVTcVZmVWRzRkhnZFRhUE03aDFRQzQ5Y2hMYUZUTjdNenczME0teUcwMDB3U2dFQUFBfjCl+v32BTgNQAE='
# cookies = 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2353 MMWEBSDK/200502 Mobile Safari/537.36'
city = "北京"
w1 = WxMps(__biz, appmsg_token, cookies, offset, city)
df1 = w1.start()