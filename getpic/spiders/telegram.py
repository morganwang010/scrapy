import scrapy
from getpic.items import GetpicItem


class TelegramSpider(scrapy.Spider):
    name = 'telegram'
    allowed_domains = ['wsjk.tj.gov.cn']
    start_urls = ['http://wsjk.tj.gov.cn/ZTZL1/ZTZL750/YQFKZL9424/FKDT1207/202201/t20220115_5779768.html']

    def parse(self, response):
        data = response.xpath("//div[@class='view TRS_UEDITOR trs_paper_default trs_web']//img//@src").extract()
        if not len(data):
            return
        for d in data:
            item = GetpicItem()
            item['nickname'] = d.replace("./","")
            item['imgurl'] = d.replace("./","http://wsjk.tj.gov.cn/ZTZL1/ZTZL750/YQFKZL9424/FKDT1207/202201/")
            print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            yield item
        
