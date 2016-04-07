import scrapy
from mongo import mongoFront


handle = mongoFront()

##############################################################
# Author: Vineel Koneru
# This funciton is to connect news website and extract all 
# the necessary HTML info (eg title, main points, cotnent etc..  
# from the news articles and parse the information. finally 
# calling databse funciton to upload into mongo collections.
############################################################


class StackOverflowSpider(scrapy.Spider):
    name = 'guardian'
    start_urls = ["http://www.theguardian.com/news/2016/apr/05/all" ]

    def parse(self, response):
        count = 0
        for href in response.css('.fc-container__inner .fc-slice-wrapper .fc-item__container .fc-item__content a::attr(href)'):
            full_url = response.urljoin(href.extract())
            #print full_url
            count = count + 1
            yield scrapy.Request(full_url, callback=self.parse_each_link)
        print "totally " + str(count) + " links"
        # yield scrapy.Request("http://www.theguardian.com/news/commentisfree/2016/apr/05/panama-papers-britain-house-order-cameron", callback=self.parse_each_link)

    def parse_each_link(self, response):
        print "response is..", response
        #print "response.rul", response.url
        datatowrite = {}
        datatowrite['url'] = response.url
        datatowrite['title'] = response.css('.content__headline::text ').extract()[0]
        datatowrite['minExplanation'] = response.css('.content__standfirst::text').extract()[1]
        datatowrite['points'] = []
        for main_links in response.css('.content__standfirst a::text'):
            datatowrite['points'].append(main_links.extract())

        datatowrite['body'] = []
        for each_para in  response.css('.content__article-body p::text'):
            datatowrite['body'].append(each_para.extract())
        handle.upload(datatowrite)
