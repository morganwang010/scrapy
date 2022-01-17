# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy,os
from getpic.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline

class GetpicPipeline1(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    def get_media_requests(self, item, info):

        imgurl = item['imgurl']
        print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"+imgurl)
        yield scrapy.Request(imgurl)
    #     s设置item相关信息 重新设置path和图片名
    def item_completed(self, results, item, info):
        print("ddddXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(results)
        imgpath = [x['path'] for ok, x in results if ok]
        
        print(imgpath)
        os.rename(IMAGES_STORE+imgpath[0], IMAGES_STORE+item['nickname'] + ".jpg")
        return item