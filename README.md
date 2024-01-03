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

## 配置

你可以修改 `lianjia/lianjia/spiders/lianjia_spider.py` 中的 `MAX_LENGTH` 变量来更改存储在 MongoDB 中的最大内容长度。

## 贡献

如果你想为这个项目做贡献，请随时提交问题或拉取请求。

## 免责声明

本教程仅供教育和学习目的使用。作者力求提供准确和实用的信息，但不对信息的准确性、完整性和实时性作任何保证。读者在使用本教程中的任何信息、工具或代码时，须自行承担风险，并对其行为负全部责任。

作者对因使用本教程的信息、工具或代码所导致的任何直接或间接损失不承担责任。本教程中提供的代码示例仅供参考，读者应审慎检查代码并根据自身需求进行修改。

## 版权声明

本教程中的所有内容，包括但不限于文本、图像、代码示例，版权均归作者所有。未经作者许可，禁止未经授权转载、复制或修改本教程中的任何内容。

读者可将本教程用于个人学习和研究目的，但不得用于商业目的或未经授权的传播。任何未经许可的使用可能构成侵权行为，作者保留采取法律行动的权利。

## 附加信息

在任何情况下，本教程的信息均不构成任何形式的建议、担保或合同。作者保留随时更改或更新本教程内容的权利，无需提前通知。

## 版权声明

本文为原创文章，作者保留所有权利。文章采用 [CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 许可协议，转载请注明原文链接及本声明。
