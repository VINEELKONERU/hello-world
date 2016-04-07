import os
import pymongo
import ssl

############################################################
# Author: Vineel Koneru
# This funciton is to connect articles database using 
# tester:tester credetials and insert news info into test 
# collection using pymongo
#
############################################################a

class mongoFront:                         
    MONGODB_URL = "mongodb://tester:tester@aws-us-east-1-portal.12.dblayer.com:10652/articles"
    def __init__(self):
        client = pymongo.MongoClient(mongoFront.MONGODB_URL,ssl_cert_reqs=ssl.CERT_NONE)
        self.db = client.get_default_database()

    def upload(self,data):
        print "uploading data to mongodb "
        # print self.db.collection_names()
        print self.db.test2.insert_one(data)
    def find_title(self,title):
        print "finding titles with " + title
        # print self.db.collection_names()
        found_articles = self.db.test2.find({ "title": { "$regex": title, "$options": "i" }})
        datatosend = { "articles": [] }
        for each_article in found_articles:
            print each_article["title"]
	    each_record = {}
            each_record["title"] = each_article["title"]
            each_record["url"] = each_article["url"]
            datatosend["articles"].append(each_record)
	return datatosend
    def find_body(self,body):
        print "finding titles with " + body
        # print self.db.collection_names()
        found_articles = self.db.test2.find({ "body": { "$elemMatch":  { "$regex": body, "$options": "i" } } })
        datatosend = { "articles": [] }
        for each_article in found_articles:
            print each_article["title"]
            each_record = {}
            each_record["title"] = each_article["title"]
            each_record["url"] = each_article["url"]
            datatosend["articles"].append(each_record)
        return datatosend

    def find_one_article(self,url):
        print "finding titles with " + url
        # print self.db.collection_names()
        found_articles = self.db.test2.find({ "url": url }, { "_id": 0 })
        datatosend = { "articles": [] }
        for each_article in found_articles:
            print each_article["title"]
            datatosend["articles"].append(each_article)
        return datatosend
