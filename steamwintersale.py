#!/bin/python3
# -*- coding: UTF-8 -*-
import os, re, sys, json, requests, time, datetime, random, logging, urllib
from multiprocessing.dummy import Pool as ThreadPool

def findstr(rule, string):
	find_str = re.compile(rule)
	return find_str.findall(string)

def getTime():
	return datetime.datetime.now().strftime('%m/%d-%H:%M:%S')

def getUTC():
	return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def getTimestamp():
	return int(time.time())

class filelib:
	def open(self, path, mode='r', encoding="gbk"):
		try:
			file = open(path, mode, encoding=encoding)
			content = file.read()
			file.close()
			return content
		except:
			return False
	def write(self, path, content, mode='w', encoding="gbk"):
		file = open(path, mode, encoding=encoding)
		file.write(content)
		file.close()
		return True
	def mkdir(self, dirname):
		try:
			os.mkdir(dirname)
		except:
			pass
		return True
	def opencfg(self, path):
		cont = self.open(path, encoding="utf-8")
		if cont:
			cont = re.sub('(?<!:)\\/\\/.*|\\/\\*(\\s|.)*?\\*\\/', '', cont)
			cont = cont.replace('\\', '\\\\').replace('\\\\"', '\\"')
			return json.loads(cont)
		else:
			return False


class weblib:
	def __init__(self):
		self.headers = {
			'Connection': 'keep-alive',
			'Accept': '*/*',
			'Origin': 'https://store.steampowered.com',
			'X-Requested-With': 'XMLHttpRequest',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
			'Referer': 'https://store.steampowered.com/promotion/cottage_2018/'
		}
		self.jar = requests.cookies.RequestsCookieJar()
	def setCookie(self, key, value):
		self.jar.set(key, value)
	def myprint(self, string):
		try:
			print(string)
		except:
			print("Network Error!")
	def get(self, url, name=''):
		try:
			req = requests.get(url, headers = self.headers, cookies = self.jar, timeout=90)
			return req.text
		except:
			self.myprint("%s|Bot: %s|NetworkError|Request: %s" % (getTime(), name, url))
			return False
	def post(self, url, postdata, name=''):
		try:
			req = requests.post(url, headers = self.headers, data = postdata, timeout=90)
			return req.text
		except:
			self.myprint("%s|Bot: %s|NetworkError|Request: %s" % (getTime(), name, url))
			return False
	def npost(self, url, postdata, name=''):
		try:
			req = requests.post(url, headers = self.headers, data = postdata, timeout=90)
			return req
		except:
			self.myprint("%s|Bot: %s|NetworkError|Request: %s" % (getTime(), name, url))
			return False

class steamwintersale:
	def __init__(self, data):
		self.url = 'https://store.steampowered.com/promotion/opencottagedoorajax'
		self.name = ''
		self.sessionid = ''
		self.door = -1
		self.weblib = weblib()
		self.log = logging.getLogger(data[0])
		self.log.setLevel(logging.DEBUG)
		self.log.propagate = False
		fh = logging.FileHandler("output.log")
		sh = logging.StreamHandler()
		formatter = logging.Formatter(fmt="%(asctime)s|%(thread)d|%(levelname)s|%(message)s", datefmt="%m/%d-%H:%M:%S")
		fh.setFormatter(formatter)
		sh.setFormatter(formatter)
		self.log.addHandler(fh)
		self.log.addHandler(sh)
	def loadcfg(self, data):
		self.name, path = data
		cfile = filelib().open(path)
		cookies = []
		for cookie in cfile.split(';'):
			cookie = cookie.strip().split('=', 1)
			if 'sessionid' in cookie[0]:
				self.sessionid = cookie[1]
			cookies.append(cookie)
		self.setCookies(cookies)
	def setCookies(self, cookies):
		for cookie in cookies:
			self.weblib.jar.set(cookie[0], cookie[1])
	def check(self):
		self.log.info("Bot: %s|CheckDoors|CheckCookies", self.name)
		req = self.weblib.get('https://store.steampowered.com/promotion/cottage_2018/')
		login = len(findstr("https:\/\/store.steampowered.com\/login", req))
		if login>0:
			self.log.warning("Bot: %s|CheckDoors|AccountNotLogin", self.name)
		else:
			self.log.info("Bot: %s|CheckDoors|Checking...", self.name)
			now = len(findstr('cottage_door_open', req))
			self.door = ((getTimestamp()-1545328800)//86400)+1
			if self.door>now:
				self.log.info("Bot: %s|CheckDoors|NewDoorFound", self.name)
				return True
			else:
				self.log.info("Bot: %s|CheckDoors|AlreadyOpened", self.name)
				return False
	def openDoor(self):
		self.log.info("Bot: %s|OpenDoor|Opening Door %s...", self.name, self.door)
		postdata = "sessionid="+self.sessionid+"&door_index="+str(int(self.door)-1)+"&t="+urllib.parse.quote(str(getUTC()))+"&open_door=true"
		#print("sessionid=a2eb82ba8e405ac5950280f9&door_index=1&t=2018-12-22T18%3A46%3A42&open_door=true")
		'''{
			"sessionid": self.sessionid,
			"door_index": self.door-1,
			"t": getUTC(),
			"open_door": True
		}'''
		req = self.weblib.npost(self.url, postdata, self.name)
		self.log.debug("Bot: %s|OpenDoor|StatusCode: %s", self.name, req.status_code)
		req = req.text
		if req=='null':
			self.log.warning("Bot: %s|OpenDoor|Error", self.name)
		else:
			self.log.debug("Bot: %s|OpenDoor|Success|%s", self.name, req)

def handler(data):
	bot = steamwintersale(data)
	try:
		bot.loadcfg(data)
	except:
		bot.log.error("Bot: %s|LoadConfig|Error", data[0])
	while True:
		if bot.check():
			bot.openDoor()
		bot.log.info("Bot: %s|ThreadSleep|6 hours", data[0])
		time.sleep(21600)

def main():
	try:
		filelib().mkdir('configs')
	except:
		pass
	sys.path.append('configs')
	list_dirs = os.walk('configs')
	filelists = []
	for root, dirs, files in list_dirs:
		for f in files:
			path = os.path.join(root, f)
			filelists.append([f.split('.')[0], path])
	pool = ThreadPool(len(filelists))
	for i in range(0, len(filelists)):
		pool.apply_async(handler, args=(filelists[i], ))
	pool.close()
	pool.join()

if __name__ == '__main__':
	main()
	# handler(['2w84s', 'configs/2w84s.txt'])