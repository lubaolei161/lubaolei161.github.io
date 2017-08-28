---
title: "Hexo博客多台机器同步"
comments: true
date: 2017-05-31
type: "categories"
categories: "github博客搭建" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - hexo
description: Hexo博客多台机器同步
password: jqtb

---

### 思路
hexo 发布到自己的master分支，然后将hexo源文件发布到hexo 分支 ，当换电脑之后拉下最新的hexo分支文件即可

### 准备工作
不管是换到哪台电脑，nodeJs 还是要先装上，git也不必说 ，必然也要装上

之后就是选一个文件夹，然后clone 自己博客的hexo分支,并在这个文件夹下安装hexo以及hexo-deployer-git

```
// npm install hexo-cli g
// 在本地博客根目录下安装hexo
git clone -b hexo https://github.com/myAccount/myAccount.github.io.git hexo

npm install hexo
// 初始化hexo
npm init
// 安装依赖
npm install
// 安装部署相关的配置
npm install hexo-deployer-git
```

### 填坑
之前一直以为装的插件也要重装一遍，其实完全不不要，只要上面代码过一遍即可，还算方便
