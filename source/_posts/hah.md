---
title: "同步测试"
comments: true
date: 2017-05-31 
type: "categories"
categories: "测试" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - github
description: #你對本頁的描述 可以省略

---

### 修改_config.yml
找到你NexT主题`_config.yml`（主意是NexT主题的_config.yml，不是hexo站点目录下的_config.yml），文件路径`your-hexo-site/themes/next/_config.yml`，添加 guestbook 到 menu 中，如下:

```bash
menu:
  home: /
  categories: /categories
  # about: /about
  archives: /archives
  tags: /tags
  guestbook: /guestbook
  # sitemap: /sitemap.xml
  # commonweal: /404.html
```

### 修改zh-Hans.yml
找到你NexT主题`zh-Hans.yml`文件（我的网站是简体语言的），文件路径`your-hexo-site/themes/next/languages/zh-Hans.yml`，添加 guestbook: 留言 到 menu 中，如下:

```bash
menu:
  home: 首页
  archives: 归档
  categories: 分类
  tags: 标签
  about: 关于
  search: 搜索
  schedule: 日程表
  sitemap: 站点地图
  commonweal: 公益404
  guestbook: 留言
```

### 新建页面
新建一个 guestbook 页面：
```bash
hexo new page "guestbook"
```

之后会在source 目录下生成一个gustbook文件夹，并自动创建index.md ，可以修改里面内容
```
---
title: 给我留言
date: 2017-05-08 10:31:30
comments: true
---
```

title 后面内容默认是gustbook，我改为了`给我留言`  ,因为之前添加过畅言系统，针对其他归档，标签界面，我都是设定为`comments：false`,这里改为true，就可以使用畅言的评论系统完成留言板的功能了.