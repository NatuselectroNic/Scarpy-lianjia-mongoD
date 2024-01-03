import scrapy
import re
import pymongo

MAX_LENGTH = 1000

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['m.lianjia.com']
    start_urls = ['https://m.lianjia.com/bj/jingjiren/?page_size=15&_t=1&offset=15']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    }

    def parse(self, response):
        # 使用正则表达式匹配特定模式中的内容
        pattern = re.compile(r'"name":"(.*?)","agentUcid":".*?","storeName":"(.*?)","schoolTag"', re.DOTALL)
        matches = pattern.findall(response.text)

        # 创建 MongoDB 连接
        client = pymongo.MongoClient('mongodb://localhost:27017/')  # 更改为你的 MongoDB 连接地址
        db = client['lianjia']  # 更改为你想要使用的数据库名称
        collection = db['lianjia']  # 更改为你想要保存信息的集合名称

        # 将匹配到的内容写入 MongoDB
        for match in matches:
            name = match[0]
            store_name = match[1] if match[1] else "无"

            # 检查写入内容的长度，如果超出最大长度则不写入
            if len(f"{name}: {store_name}") <= MAX_LENGTH:
                agent_data = {
                    'name': name,
                    'store_name': store_name
                }
                collection.insert_one(agent_data)

        client.close()  # 关闭 MongoDB 连接
