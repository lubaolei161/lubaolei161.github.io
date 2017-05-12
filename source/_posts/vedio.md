---
title: "通过 Hexo 插件插入音乐/视频"
comments: true
date: 2017-05-10 12:50:16
type: "categories"
categories: "github博客搭建" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - github
description: #你對本頁的描述 可以省略
photos:
- http://opj0cbfmf.bkt.clouddn.com/3b292df5e0fe9925a0ff2f7a3ea85edf8db1712c.jpg
---
### 关于音乐，视频添加
虽然可以通过使用html标签的方式加入音乐，视频什么的，但是逼格不够高，还是研究下hexo自带的播放器插件。。

### 插件
这里需要使用两个播放器插件

[hexo-tag-aplayer](https://github.com/grzhan/hexo-tag-aplayer#upstream-issue)

[hexo-tag-dplayer](https://github.com/NextMoe/hexo-tag-dplayer)

两款插件基于 [DIYgod] 编写的 html5 播放器 [APlayer](https://github.com/DIYgod/APlayer) 和 [DPlayer](https://github.com/DIYgod/DPlayer) 开发。

### 安装
网上大部分说直接安装以上两个插件就行，但是后来发现如果直接安装，然后使用标签在文章中是不能使用的，会提示找不到这两个标签这个错误。。

后来仔细研究了下，这连个hexo插件要想使用，还需要先安装aplayer和dpalyer

所以正确的安装步奏如下：
```bash
npm install dplayer --save
npm install aplayer --save
npm install hexo-tag-dplayer
npm install hexo-tag-aplayer
```

然后在文章中就可以正常使用了，关于标签的使用，可以到插件作者主页去查看
如果提示缺少文件什么的，请参照这篇文章进行添加:[参考](http://www.jianshu.com/p/53e0d2a617da)

### 使用Demo
以下简单的使用：

#### 插入MP3:
音乐代码：
其中author,title 前两个标签必须添加，不然报错，图片可以不用添加
```bash
{% aplayer "HUSH" "Lasse Lindh" "http://opj0cbfmf.bkt.clouddn.com/Part.3%20Lasse%20Lindh%20-%20Hush.mp3"  "http://opj0cbfmf.bkt.clouddn.com/hush.jpg" "autoplay=false" %}
```
效果如下：
{% aplayer "HUSH" "Lasse Lindh" "http://opj0cbfmf.bkt.clouddn.com/Part.3%20Lasse%20Lindh%20-%20Hush.mp3"  "http://opj0cbfmf.bkt.clouddn.com/hush.jpg" "autoplay=false" %}

#### 视频：
视频代码：
```bash
{% dplayer "url=http://home.ustc.edu.cn/~mmmwhy/GEM.mp4"  "pic=http://home.ustc.edu.cn/~mmmwhy/GEM.jpg" "loop=yes" "theme=#FADFA3" "autoplay=false" "token=tokendemo" %}
```
效果如下：
{% dplayer "url=http://home.ustc.edu.cn/~mmmwhy/GEM.mp4"  "pic=http://home.ustc.edu.cn/~mmmwhy/GEM.jpg" "loop=yes" "theme=#FADFA3" "autoplay=false" "token=tokendemo" %}

