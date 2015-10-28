import urllib
import urllib2
import httplib
import time
import json
import annotater_parser
import sys
import random

if __name__ == "__main__":
	print "Start"
	url = "http://brat.statnlp.com/main/ajax.cgi"

	studentId = sys.argv[1]
	if len(studentId) != 7:
		raise IndexError

	values = {
		"action": "createSpan",
		"offsets": "[[157,160]]",
		"collection":"/sms_corpus/students/1000660/",
		"document":"sms_corpus",
		"type":"Noun-Phrase",
		"comment": "",
		"attributes":"{}",
		"normalizations":"[]",
		"protocol":"1"
	}

	values["collection"] = "/sms_corpus/students/{0}/".format(sys.argv[1])
	
	headers = {
		"Host": "brat.statnlp.com",
		"Connection": "keep-alive",
		# "Content-Length": "193",
		"Accept": "*/*",
		"Origin": "http://brat.statnlp.com",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"Referer": "http://brat.statnlp.com/main/",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-GB,en-US;q=0.8,en;q=0.6",
		"Cookie": "sid=9a41085b3b60422ca3c750afbbdb455491b7c495f8d40949678308c6"
	}

	def login(idPass):
		sid = '%056x' % random.randrange(16**56)
		headers["Cookie"] = "sid={0}".format(sid)
		loginValues = {
			"action": "login",
			"protocol":"1",
			"user": idPass,
			"password": idPass
		}
		data = urllib.urlencode(loginValues)
		req = urllib2.Request(url,data,headers)
		response = urllib2.urlopen(req)
		reponseData = response.read()

	def sendAnnotations():
		print "Sending annotations"
		modifications = open("modifications.txt", "r")
		modLines = modifications.readlines()

		lineCount = 1
		for line in modLines:
			values["offsets"] = "[{0}]".format(line)
			data = urllib.urlencode(values)
			req = urllib2.Request(url,data,headers)
			# conn = httplib.HTTPConnection(url)
			response = urllib2.urlopen(req)
			reponseData =  json.loads(response.read())
			while "exception" in reponseData:
				# print reponseData
				time.sleep(100)
				response = urllib2.urlopen(req)
				reponseData =  json.loads(response.read())
			print "Annotation {0} sent".format(lineCount)
			lineCount += 1
			# conn.close()

	def removeAnnotations(offsets, id_):
		values["action"] = "deleteSpan"
		values["offsets"] = str(offsets)
		values["id"] = id_
		# print values
		data = urllib.urlencode(values)
		req = urllib2.Request(url,data,headers)
		# conn = httplib.HTTPConnection(url)
		response = urllib2.urlopen(req)
		reponseData = response.read()
		if "exception" in json.loads(reponseData):
			print "{0} error occurred".format(id_)
			# print json.loads(reponseData)
		else:
			print "{0} deleted".format(id_)

	command = sys.argv[2]
	login(sys.argv[1])

	if command == "del":
		try:
			for i in range(int(sys.argv[3]), int(sys.argv[4])):
				removeAnnotations([[100,101]], "T{0}".format(str(i)))
		except:			
			removeAnnotations([[100,101]], "T{0}".format(str(sys.argv[3])))
	elif command == "send":
		try:
			annotater_parser.parseAnnotations(sys.argv[3], sys.argv[4])
		except:
			annotater_parser.parseAnnotations()
		sendAnnotations()
	elif command == "local":
		# try:
			annotater_parser.parseAnnotations(sys.argv[3], sys.argv[4])
		# except:
		# 	annotater_parser.parseAnnotations()



