import re,os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import requests


mobile_emulation = {"deviceName": "iPhone X"}#模拟手机
chrome_options = webdriver.ChromeOptions()#模拟手机
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  #模拟手机
chrome_options.add_argument('--headless')#无头模式
browser = webdriver.Chrome('./chromedriver.exe',options= chrome_options)#定义browser
wait=WebDriverWait(browser,10)#设置等待显式时间


def OpenUrl(ShareLink):
	try:
		ReShareLink = re.findall(r'(https?://\S+)',ShareLink)
		browser.get(ReShareLink[0])#打开短网址，例：https://v.douyin.com/4tXch5/
		MainVideoUrl = browser.current_url#获取当前网址https://www.iesdouyin.com/share/video/6768505302955347211/?region=CN&mid=6716375926952971021&u_code=10ghebkl3&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme
		html = browser.page_source#获取html
		doc = pq(html)#pyquery读取html
		VideoIDs = []
		DataId = doc('.author-list-wrap .author-video-wrap .video-wrap .author-list-wrap')
		for i in DataId.items('.author-video-item'):
			VideoIDs.append(i.attr('data-id'))
		return VideoIDs,MainVideoUrl
	except Exception as error:
		print(error)

def MutiDownloader(Path,VideoIDs,MainVideoUrl):
	DownloaderVideo(Path,MainVideoUrl)
	for VideoID in VideoIDs:
		CurrentVideoUrl = MainVideoUrl.replace(MainVideoUrl[38:57],VideoID)
		try:
			DownloaderVideo(Path,CurrentVideoUrl)
		except Exception as error:
			print(error)
			pass

def DownloaderVideo(Path,MainVideoUrl):
	browser.get(MainVideoUrl)
	html2 = browser.page_source#获取html2
	doc2 = pq(html2)#pyquery读取html2
	VideoUrl = doc2('.video-player')#获取带水印的VideoHTML
	VideoTitle = doc2('.user-title').text()#读取title
	ReVideoUrl = re.findall(r'(https?://\S+)',str(VideoUrl))#re读取带水印的Video网址
	ReVideoUrl = ReVideoUrl[0]#读出来的是集合，取第一位
	WithOutWM = ReVideoUrl.replace('playwm','play')#带水印网址切换为不带水印网址
	browser.get(WithOutWM)#打开不带水印的网址
	html3 = browser.page_source
	doc3 = pq(html3)
	VideoTrueUrl = doc3('source').attr('src')#获取视频源地址，返回并准备开始下载
	r = requests.get(VideoTrueUrl, stream=True)
	if not os.path.exists(Path):
		os.makedirs(Path)
	with open(Path+VideoTitle+'【侵删】'+'.mp4', 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024 * 1024):
			if chunk:
				f.write(chunk)

	print("%s downloaded!\n" % (VideoTitle+'【侵删】'))


def main():
	ShareLink = '#在抖音，记录美好生活##大学生被金腰带选手ko后去世 年龄轻轻的才22岁 你们怎么看 https://v.douyin.com/4gRU4Q/ 复制此链接，打开【抖音短视频】，直接观看视频！'
	VideoIDs,MainVideoUrl = OpenUrl(ShareLink)
	Path = './Video/'
	MutiDownloader(Path,VideoIDs,MainVideoUrl)
	browser.close()

if __name__ == '__main__':
	main()
