import os
import pymongo
import ssl



class mongoFront:
    MONGODB_URL = "mongodb://tester:tester@aws-us-east-1-portal.13.dblayer.com:11066/articles"
    def get_connection(self):
        client = pymongo.MongoClient(mongoFront.MONGODB_URL,ssl_cert_reqs=ssl.CERT_NONE)
        db = client.get_default_database()
        print db.collection_names()
        return db

    def upload(self,data):
        print "connection"
        print data
        connection = self.get_connection()
        print "test"


obj = mongoFront()
print "test"
dbhandle = obj.get_connection()
dbhandle.collection_names()




# collection = dbhandle.test


# MONGODB_URL = "mongodb://tester:tester@aws-us-east-1-portal.13.dblayer.com:11066/articles"
# client = pymongo.MongoClient(MONGODB_URL,ssl_cert_reqs=ssl.CERT_NONE)
# db = client.get_default_database()
# print db.collection_names()