
BOT_NAME = "pachong4"

SPIDER_MODULES = ["pachong4.spiders"]
NEWSPIDER_MODULE = "pachong4.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
MONGODB_URI = 'mongodb://localhost:27017/'
MONGODB_DATABASE = 'lianjia'  # 更改为你想要使用的数据库名称
