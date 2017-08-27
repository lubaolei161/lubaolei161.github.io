---
title: "Hexo Next主题下基本配置"
comments: true
date: 2017-05-07
type: "categories"
categories: "github博客搭建" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - github
description: #你對本頁的描述 可以省略
---

关于Hexo 以及Next的一些基本设置参考官方文档
* [Hexo](https://hexo.io/zh-cn/docs/setup.html)
* [Next](http://theme-next.iissnan.com/) 

主要针对以下几个地方稍微记录一下：
* 头像设置
* 打赏功能
* 首页文章缩进
* 网站图标设置
* 增加评论框服务
* 添加站点数据统计功能
* 开启站内搜索功能
* Hexo Next主题增加留言页
* Hexo Next主题下添加分享朋友圈功能
* 安装hexo-addlink插件，文末添加版权声明


### 头像设置
这里说的头像是侧边栏简介里的个人头像，如果不做设置显示的是空人头
建了博客，啥事也没干，二话不说先上头像，官方Next文档里虽然写了，但是我怎么试都没成功，也可能长的丑。。

我的办法如下：

其实在hexo/public/images文件夹下面有avatar.gif 文件，这个文件就是侧边栏的空人头图像，直接把自己的头像改名为这个文件并替换，重新提交发布即可

### 打赏功能

修改Next的主题配置文件`hexo/themes/next/_config.yml`

添加
```bash
reward_comment: 生活不易，求打赏红包~~
wechatpay: /uploads/wechat-reward-image.JPG
# alipay: /path/to/alipay-reward-image
```

我只添加了微信打赏，按需吧。。 需要上传二维码，直接上传到了hexo/public/uploads 下面即可

### 首页文章缩放

文章多了如果首页完全显示那是很蛋疼的，需要设置一下
修改Next的主题配置文件`hexo/themes/next/_config.yml`,找到如下属性并设置为true
```bash
auto_excerpt:
  enable: true
  length: 150
```

### 网站图标设置
就是网址打开时候地址栏里的图标，不设置一个总感觉好low
不用修改任何配置文件，直接拿自己的图标文件命名为favicon.ico 上传到hexo/source文件夹下即可

### 增加评论框服务
以前大多数人都用多说，但是多说7月份就关闭了，所以可以取代的，就是disqus,网易云跟帖,畅言，友言，来必力

disqus国外的，天朝言论不自由，管制了，墙了，别折腾了
畅言：本来想用，但是要备案，不然只能15天。。算了。。当然你要是备案了，想装的话可以参考我另一篇文章：[畅言安装指南](http://barrysite.me/2017/05/07/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E6%B7%BB%E5%8A%A0%E7%95%85%E8%A8%80%E8%AF%84%E8%AE%BA%E6%A1%86/)
友言：参考官方配置，很简单，但是我就是不能正常显示。。也没解决，放弃了
来必力：韩国的，可以用，我折腾了下，一直不能成功注册这网站，不知道是不是我网络问题，配置也是很简单的，哪天vpn好了我再试试吧
网易云跟帖： 其它因为各种原因都让我放弃了，虽然不咋地，但是确实安装很简单，一行代码就搞定了，使用测试了一下也没什么bug  ，就是它了。。

装个评论服务，我踩的雷已经可以炸掉一做碉堡了，不得不吐槽啊。。

下面就说下网易云跟帖安装：

官方配置里其实有，我摘录下：

登陆 [网易云跟帖](https://gentie.163.com/),注册帐号，然后基本设置一下，然后在获取代码--app sdk 一栏获取你的APP KEY,也就是 Product Key。 编辑 主题配置文件， 编辑 gentie_productKey 字段，设置如下：
```bash
gentie_productKey: #your-gentie-product-key
```

之后就可正常使用了。。。

### 添加站点数据统计功能

- *站点访问统计*
- *文章阅读统计*

最简单的方法就是直接修改主题配置菜单添加 不蒜子统计插件,找到并修改如下：

```bash
busuanzi_count:
  # count values only if the other configs are false
  enable: true
  # custom uv span for the whole site
  site_uv: true
  site_uv_header: <i class="fa fa-user"></i>本站访客数
  site_uv_footer: 人次
  # custom pv span for the whole site
  site_pv: true
  site_pv_header: <i class="fa fa-eye"></i>本站总访问量
  site_pv_footer: 次
  # custom pv span for one page only
  page_pv: true
  page_pv_header: <i class="fa fa-eye"></i>阅读次数
  page_pv_footer: 次
```

其中有三种数据，可以单独进行开关设置。 修改完之后可以看到效果
![1](https://github.com/myAccount/blogMaterial/blob/master/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE/1.jpg?raw=true)

![2](https://github.com/myAccount/blogMaterial/blob/master/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE/2.jpg?raw=true)

### 开启站内搜索功能
NexT 支持集成 Swiftype、 微搜索、Local Search 和 Algolia，各种搜索配置官方文档均有说明，但是尝试了一下只有本地搜索用着比较顺手

配置也简单，如下：
#### 1. 安装 hexo-generator-searchdb，在站点的根目录下执行以下命令：
```python
$ npm install hexo-generator-searchdb --save
```
#### 2. 站点配置文件，新增以下内容到任意位置：
<font color=#00ffff >经测试，这一步可以不做，不然多生成一个search.xml 冲突</font>
```python
search:
  path: search.xml
  field: post
  format: html
  limit: 10000
```
#### 3. 主题配置文件，启用本地搜索功能：
```python
# Local search
local_search:
  enable: true
```

### Hexo Next主题增加留言页
参考：[Hexo Next主题增加留言页](http://barrysite.me/2017/05/08/hexo%E7%BD%91%E7%AB%99NexT%E4%B8%BB%E9%A2%98%E5%A2%9E%E5%8A%A0%E7%95%99%E8%A8%80%E9%A1%B5/)

### Hexo Next主题下添加分享朋友圈功能
参考： [Hexo Next主题下添加分享朋友圈功能](http://barrysite.me/2017/05/07/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E6%B7%BB%E5%8A%A0%E5%88%86%E4%BA%AB%E6%9C%8B%E5%8F%8B%E5%9C%88%E5%8A%9F%E8%83%BD/)

### 安装hexo-addlink插件，文末添加版权声明
安装个插件，然后稍微配置下，就可以在每篇文章末加入自己的版权声明
```bash
$ npm install hexo-addlink --save
```

配置：_config.yml增加如下信息：
```bash
addlink:
  before_text: hello # text before the post link
  after_text: bye # text after the post link
```

比如我的：
```bash
addlink:
  before_text: 本文出自Barry的博客 # text before the post link
  after_text: 欢迎转载，转载请注明出处！ # text after the post link

```

之后重新发布就可以看到效果了


-----
以上设置都只针对我自己的环境，所用Next的版本为5.1，个别版本可能有所不同

