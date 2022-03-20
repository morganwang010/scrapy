import scrapy
import pymysql
from getpic.items import GetHuaweiItem


class HuaweiKBSpider(scrapy.Spider):
    name = 'huaweikb'
    allowed_domains = ['huaweicloud.com']
    start_urls = ['https://www.huaweicloud.com/zhishi/page-1']
    db = pymysql.connect(host='192.168.0.100',
                     user='root',
                     password='123456',
                     database='huawei',
                     port=13306)
    db.connect()
    cursor = db.cursor()

    def parse(self, response):
        data = response.xpath("//div[@class='list-items']//a//@href").extract()
        for i in range(187,188):
            url = "https://www.huaweicloud.com/zhishi/page-" + str(i)
            yield scrapy.Request(url, callback=self.parse_page,meta={"page":url})
    def parse_page(self, response):
        pageList = response.xpath("//div[@class='list-items']//a//@href").extract()
        pageListName = response.meta['page']
        for page in pageList:
            pageUrl = "https://www.huaweicloud.com" + page
            yield scrapy.Request(pageUrl, callback=self.parse_page_detail,meta={"page":pageListName,"pageUrl":pageUrl})
    def parse_page_detail(self, response):
        item = GetHuaweiItem()
        page = response.meta['page']
        pageUrl = response.meta['pageUrl']
        item['title'] = ('').join(response.xpath("//h1[@class='cloud-blog-detail-title']//text()").extract())
        item['content'] = ('').join(response.xpath("//div[@id='blogContent']//p").extract())
        # sql = 'insert into zhishi(title,content,page,pageUrl) values("%s","%s","%s","%s")' % (item['title'],item['content'],page,pageUrl)
        sql = "insert into zhishi (title,content,page,pageUrl) values (%s,%s,%s,%s)"  
        data=(item['title'],item['content'],page,pageUrl)
        self.cursor.execute(sql, data)
        self.db.commit()
        yield item
 
        
