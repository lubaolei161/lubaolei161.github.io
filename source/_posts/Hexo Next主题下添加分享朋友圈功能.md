---
title: "Hexo Next主题下添加分享朋友圈功能"
comments: true
date: 2017-05-07
type: "categories"
categories: "github博客搭建" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - github
description: #你對本頁的描述 可以省略
---

偶尔写点东西还是需要分享下到朋友圈啥的，但是现在天朝管制比较厉害，像为知笔记，以前免费版本就可以分享笔记到朋友圈，现在都要收费了，印象笔记在天朝无论是不是会员，这功能就直接给阉割了。。那自己的博客难道不能了么，大约查了下，如果想分享，域名还要去备案，我靠，备案，那得多麻烦。。或者自己接微信API开发吧，那就头大了。

然而，其实有个很方便的第三方插件就能实现：jiathis

### 注册jiathis帐号
首先登录[jiathis官方网站](http://www.jiathis.com/),然后注册帐号，直接生成分享代码，大小自己选择。其实这段代码在Next文件中已经有了，只要记住自己的uid即可

### 修改jiathis.swig文件
打开next主题下的`C:\hexo\themes\next\layout\_partials\share\jiathis.swig `文件，可以自己选择需要添加到分享到哪些地方，不要的就删除

### 修改主题配置文件
找到share属性并设置jiathis为true ，莫有就在配置文件中添加
```bash
# Share
jiathis:
  enable: true
# Warning: JiaThis does not support https.
  add_this_id: yourUID
```

需要注意的是仅支持http，还好我域名能用。。不然又得找其他方法了。。[展示效果](http://barrysite.me/2017/05/07/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E6%B7%BB%E5%8A%A0%E5%88%86%E4%BA%AB%E6%9C%8B%E5%8F%8B%E5%9C%88%E5%8A%9F%E8%83%BD/)


### 分享到微信朋友圈

针对微信分享，这里要通过手机扫描二维码，然后点击继续访问，转换为手机预览之后，然后再右上角分享，之后就可以在朋友圈看到自己的内容了。。

这一步完成之后，别人点链接看到的还是需要再次点击继续访问，也是因为域名没备案，目前没找到其他好的办法解决，算是美中不足吧。。

<img src="https://github.com/myAccount/blogMaterial/blob/master/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E6%B7%BB%E5%8A%A0%E5%88%86%E4%BA%AB%E6%9C%8B%E5%8F%8B%E5%9C%88%E5%8A%9F%E8%83%BD/1.PNG?raw=true" width="50%" height="50%" />



-----
以上设置都只针对我自己的环境，所用Next的版本为5.1，个别版本可能有所不同

