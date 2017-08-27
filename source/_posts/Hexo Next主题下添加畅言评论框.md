---
title: "Hexo Next主题下添加畅言评论框"
comments: true
date: 2017-05-07
type: "categories"
categories: "github博客搭建" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - github
description: #你對本頁的描述 可以省略
---

### 关于畅言
在写下面内容的时候，本来我是打算用畅言的，但是网站不备案，畅言只能用15天，所以看大家是不是备案了

安装畅言时候也有很多坑，最恶心的就是相互不能看到评论，然后就是多个页面共用一个评论，查啊查，改啊改，后来才解决。。以下教程都是血的教训的总结啊。。

------------

大多数在github博客上要添加评论框，都是添加多说评论框，但是命苦吧，等我想添加它的时候才发现，多说已经要倒下了，默哀三分钟。

之后选择了畅言评论框，具体添加方法如下


------

### 注册畅言帐号

进入[畅言官网](https://www.kuaizhan.com/) , 这里进入的其实是快站，他们是一家，于是我就注册了快站帐号。

并同时新建了一个站点，后面切换到畅言就可以使用评论服务了

### 登录并进入畅言后台

注册完后，登录进入畅言官网，获取你的畅言 app id 和 app key。

<img src="https://github.com/myAccount/blogMaterial/blob/master/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E6%B7%BB%E5%8A%A0%E7%95%85%E8%A8%80%E8%AF%84%E8%AE%BA%E6%A1%86/1.jpg?raw=true" width="50%" height="50" />

<font color=#00FFFF >我不知道其他有没人发现，我反正是被坑的很惨，这里给我的APP key 和在畅言生成通用安装代码时候 conf 里面的值不一致，所以请大家确认一下，一致最好，不一致以conf值为准，不然会相互看不到评论 </font>
### Next主题开启畅言系统

很多人会说需要把畅言官网通用安装密码拷贝下来，然后新建评论模板啥的，这里其实我使用的Next5.1主题里面已经安装好了多个第三方评论系统，包括畅言，安装的目录在：
`C:\hexo\themes\next\layout\_third-party\comments\changyan.swig`

如果没有，请自行到该文件夹创建模板

假设已经有了，这里什么都不用修改，直接进行主题中畅言系统的开启配置即可

打开主题配置文件：`C:\hexo\themes\next\_config.yml` 找到如下为知并修改添加APPKEY,APPID

```bash
# changyan
changyan:
  enable: true
  appid:  你的appid
  appkey: 你的appkey
```

完成之后，重新`hexo d -g` 就可以看到文章里显示评论框了。
但是这里并不完美，使用起来有几个bug，一是多个文章共用一个评论，二就是表情那个框不能用，接下来修改下以下文件就行
`C:\hexo\themes\next\layout\_partials\comments.swig`

打开并找到如下位置并修改：
```html
  {% elseif theme.changyan.appid and theme.changyan.appkey %}
      <div id="SOHUCS" sid= "{{ page.permalink }}" style="padding: 0px 20px 0px 30px;"></div>
    {% endif %}
```



之后保存，重新`hexo d -g`




### tips

#### 确保每篇文章开头部分front-matter 中添加了 comments: true 不然是看不到评论的

#### 关闭多余评论
博客界面中目录，归档，标签里面可能也会有评论框出现，这里需要将`C:\hexo\source\`里面对应的categories,tags,about页面中的三个index.md 文件分别修改，这里的三个文件是控制这三类文件默认是统一配置，比如我不需要tags里面有评论，直接在tags目录下的index.md 添加
```bash
---
title: tags
type: "tags"
date: 2017-05-05 09:02:17
comments: false
---
```
即可

#### 评论框配置
至于评论框外表颜色这些主题类型的设置，其实是在畅言网站里面设置的`畅言后台管理-系统设置-PC版设置-主题样式`中调节

--------

如果以上内容帮到了你，请打赏点如何？^_^_