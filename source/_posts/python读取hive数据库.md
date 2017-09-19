---
title: python读取hive数据库
comments: true
date: 2017-09-18 21:03:22
type: "categories"
categories: "python" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - 脚本
description:
password:
---





* sql定义用''' 不用" ,方便写长sql  ，变量替换 记得在变量外添加单引号

* 返回的列表是\t分割，与hive库里分隔符设置一致




```python
import os
def get_sql_result(sql):
    data = os.popen("""hive -e "%s" """%(sql)).readlines()
    return data

sql='''
select * from dim_calendar_cctalk
where ds='%s'
limit 100;
'''

new_sql=sql%('2017-09-10')

data=get_sql_result(new_sql)


### 取第2列
for line in data:
    value=int(line.split('\t')[1].strip())
    print value

```
