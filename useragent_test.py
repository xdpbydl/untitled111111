from fake_useragent import UserAgent
ua = UserAgent()
#ie浏览器的user agent
print(ua.ie)

#opera浏览器
print(ua.opera)
#
# #chrome浏览器
print(ua.chrome)
#
# #firefox浏览器
print(ua.firefox)
#
# #safri浏览器
print(ua.safari)
#
# #最常用的方式
# #写爬虫最实用的是可以随意变换headers，一定要有随机性。支持随机生成请求头
print(ua.random)
print(ua.random)
print(ua.random)