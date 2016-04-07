# hello-world
Install python 2.7 version
Scrapy and pymongo modules are the prerequesties 
Run below command in order to execute scritps
'scrapy runspider guardian_spider.py'
I have hosted this application in AWS ec2-instance, please use below URL and proivde POST request as shwon below in order to fetch matching records.
http://52.23.254.79/api/titles - search in title

{
 "title" : "paris"
}

http://52.23.254.79/api/url - search in url

{
 "url" : "http://www.theguardian.com/news/2016/apr/05/uk-could-impose-direct-rule-on-tax-havens-says-jeremy-corbyn-panama-papers"
}
