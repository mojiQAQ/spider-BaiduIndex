# -*- coding: utf8 -*-

import codecs
from datetime import datetime
from get_index import BaiduIndex

if __name__ == "__main__":
    """
    最多一次请求5个关键词
    """
    # 查看城市和省份的对应代码
    # print BaiduIndex.city_code
    # print BaiduIndex.province_code

    baidu_index = BaiduIndex(['人民币贬值'], '2009-01-01', '2019-03-31')
    for data in baidu_index('人民币贬值', 'all'):
        if datetime.strptime(data["date"], "%Y-%m-%d").strftime("%w") != "0" and datetime.strptime(data["date"], "%Y-%m-%d").strftime("%w") != "6":
            print data["date"], ",", data["index"]
            with open("test.csv", 'ab') as f:
                f.write(codecs.BOM_UTF8)
                f.write('"{0}","{1}"\r'.format(data["date"], data["index"]))

        
    print '获取1个关键词的全部数据'
    baidu_index.result['人民币贬值']
    # print '获取1个关键词的移动端数据'
    # print(baidu_index.result['人民币贬值']['wise'])
    # print '获取1个关键词的pc端数据'
    # print(baidu_index.result['人民币贬值']['pc'])
