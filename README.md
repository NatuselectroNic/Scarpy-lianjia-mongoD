# 连家网爬虫

这是一个 Scrapy 爬虫，用于从连家网站提取房地产经纪人的信息，并将其存储到 MongoDB 数据库中。

## 安装

1. 克隆代码仓库：

    ```bash
    git clone https://github.com/your-username/lianjia-spider.git
    ```

2. 使用 pip 安装依赖：

    ```bash
    cd lianjia-spider
    pip install -r requirements.txt
    ```

## 使用方法

1. 确保你已安装并运行了 MongoDB。
2. 在 `lianjia/lianjia/spiders/lianjia_spider.py` 中更新 MongoDB 连接细节：
    ```python
    client = pymongo.MongoClient('mongodb://your-mongodb-uri/')
    db = client['lianjia']
    collection = db['lianjia_agents']
    ```

3. 运行爬虫：
   
    ```bash
    cd lianjia-spider/lianjia
    scrapy crawl lianjia
    ```

## 配置

你可以修改 `lianjia/lianjia/spiders/lianjia_spider.py` 中的 `MAX_LENGTH` 变量来更改存储在 MongoDB 中的最大内容长度。

## 贡献

如果你想为这个项目做贡献，请随时提交问题或拉取请求。

## 许可证

该项目基于 MIT 许可证发布 - 详见 [LICENSE](LICENSE) 文件。
