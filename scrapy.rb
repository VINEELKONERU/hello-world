import scrapy
from mongo import mongoFront


handle = mongoFront()
dbhandle =  handle.get_connection        
# print handle.upload("test") 
collection = dbhandle.test
collection.insert_one({ "test": "test"})
class StackOverflowSpider(scrapy.Spider):
    name = 'guardian'
    start_urls = ["http://www.theguardian.com/news/2016/apr/05/all" ]

    def parse(self, response):
        # print response
        # print response.css('.fc-container__inner .fc-slice-wrapper .fc-item__container')
        count = 0
        # print response.css('.fc-container__inner .fc-slice-wrapper .fc-item__container a')
        for href in response.css('.fc-container__inner .fc-slice-wrapper .fc-item__container .fc-item__content a::attr(href)'):
            full_url = response.urljoin(href.extract())
            print full_url
            count = count + 1
            # yield scrapy.Request(full_url, callback=self.parse_each_link)
        print "totally " + str(count) + " links"
        yield scrapy.Request("http://www.theguardian.com/news/commentisfree/2016/apr/05/panama-papers-britain-house-order-cameron", callback=self.parse_each_link)
        print "exiting"
        # for href in response.css('.question-summary h3 a::attr(href)'):
            # full_url = response.urljoin(href.extract())
            # yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_each_link(self, response):
        print response.css('.content__headline::text ').extract()[0]
        print response.css('.content__standfirst::text').extract()[1]
        for main_links in response.css('.content__standfirst a::text'):
            print main_links.extract()

        for each_para in  response.css('.content__article-body p::text'):
            print each_para.extract()

        
        # yield {
        #     'title': response.css('h1 a::text').extract()[0],
        #     'votes': response.css('.question .vote-count-post::text').extract()[0],
        #     'body': response.css('.question .post-text').extract()[0],
        #     'tags': response.css('.question .post-tag::text').extract(),
        #     'link': response.url,
        # }



