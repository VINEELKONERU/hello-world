import os
import pymongo
import ssl



class mongoFront:                         
    MONGODB_URL = "mongodb://tester:tester@aws-us-east-1-portal.12.dblayer.com:10652/articles"
    def __init__(self):
        client = pymongo.MongoClient(mongoFront.MONGODB_URL,ssl_cert_reqs=ssl.CERT_NONE)
        self.db = client.get_default_database()

    def upload(self,data):
        print "uploading data to mongodb "
        # print self.db.collection_names()
        print self.db.test.insert_one(data)