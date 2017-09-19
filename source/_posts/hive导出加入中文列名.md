---
title: hive导出加入中文列名
comments: true
type: categories
categories: hive
tags:
  - hive
abbrlink: 57395
date: 2017-09-02 00:00:00
description:
---



#### 发邮件或者需要导出数据时候需要加入列名，以下命令开启：

```sql
set hive.cli.print.header=true;  // 打印列名 
set hive.cli.print.row.to.vertical=true;   // 开启行转列功能, 前提必须开启打印列名功能 
set hive.cli.print.row.to.vertical.num=1; // 设置每行显示的列数 

```



#### hive 的sql需要中文别名时， 中文需要用`` 引起来：

```sql
select test as `测试` from table
```



