---
title: "Github+Hexo+NEXT主题+域名绑定 博客搭建全记录"
comments: true
date: 2017-05-07
type: "categories"
categories: "github博客搭建" #文章分類目錄 可以省略
tags: #文章標籤 可以省略
     - github
description: #你對本頁的描述 可以省略
photos:
- http://opj0cbfmf.bkt.clouddn.com/github+hexo.jpg
---

Hexo是一个快速、简洁且高效的博客框架，而Github是一个免费的代码托管工具，利用Github Page可以免费创建一个静态网站。下面将介绍如何使用Hexo和Github，在Windows环境中搭建自己的微博

-----

### 安装和配置Hexo及Github

#### 安装Hexo

安装Hexo前，需要安装以下：

- Node.js  [下载地址](https://nodejs.org/en/)
- Git  [下载地址](https://github.com/git-for-windows/git/releases/download/v2.12.2.windows.2/Git-2.12.2.2-64-bit.exe) 这里用迅雷下速度比较快，给的链接是64位的 如果要32位的自行百度
这里提供个githup for win的图形化客户端，百度云下载：[Git for win](http://pan.baidu.com/s/1skUY5xb) 但是并不建议使用。。玩git 还是用git bash 方式比较高大上~~


如果已经安装完成以上程序，打开Git-bash，输入
```bash
npm install -g hexo-cli
```
即可完成Hexo的安装。

#### 使用Hexo进行本地建站
选择一个本地的文件夹，如C:\hexo

输入
```bash
hexo init C:/hexo
cd C:/hexo
npm install

```

如果hexo安装成功，则在C:\hexo文件夹下的文件目录为
```bash
.
├── _config.yml // 网站的配置信息，你可以在此配置大部分的参数。
├── package.json 
├── scaffolds // 模板文件夹。当你新建文章时，Hexo会根据scaffold来建立文件。
├── source // 存放用户资源的地方
|   ├── _drafts
|   └── _posts
└── themes // 存放网站的主题。Hexo会根据主题来生成静态页面。
```
详细文件或文件夹的具体含义见 [Hexo官方文档](https://hexo.io/zh-cn/docs/setup.html)

之后输入
```bash
hexo server 
```

此时会启动本地部署好的默认的博客网站 地址是：[http://localhost:4000/](http://localhost:4000/)
不出意外 这里应该是没啥问题的。。

#### 创建Github账号
访问Github官网进行注册 ，这里没啥好说的。

#### 创建与账号同名的Repository
一定要同名的Repository，比如帐号是myid,那新建的Repository名称应该是myid.github.io

#### 配置SSH

##### (1) 生成SSH

检查是否已经有SSH Key，打开Git Bash，输入

cd ~/.ssh
如果没有这个目录，则生成一个新的SSH，输入
```bash
ssh-keygen -t rsa -C "your e-mail"
```
其中，your e-mail是你注册Github时用到的邮箱。

然后接下来几步都直接按回车键，最后生成如下

![rsa](http://i.imgur.com/RSCTurW.jpg)

##### (2) 复制公钥内容到Github账户信息中

打开~/.ssh/id_rsa.pub文件，复制里面的内容；

打开Github官网，登陆后进入到个人设置(点击头像->setting)，点击右侧的SSH Keys，点击Add SSH key；填写title之后，将之前复制的内容粘贴到Key框中，最后点击Add key即可。

##### (3) 测试SSH是否配置成功

输入
```bash
ssh -T git@github.com
```
如果显示以下，则说明ssh配置成功。
```
Hi username! You've successfully authenticated, but GitHub does not
provide shell access.
```

##### (4) 配置github 账户
```bash
git config --global user.name "username"
git config --global user.email "email"
```
配置完之后输入：
```
git config --list查看已设配置
```
看username ,email是不是都对了


将网站发布到Github的同名repository中

打开C:\Hexo文件夹中的_config.yml文件，找到如下位置，填写
```yml
# Deployment
## Docs: http://hexo.io/docs/deployment.html
deploy: 
  type: git
  repo: git@github.com:MyGithub/MyGithub.github.io
```
注： (1) 其中MyGithub替换成你的Github账户; (2)注意在yml文件中，:后面都是要带空格的。

此时，通过访问http://MyGithub.github.io可以看到默认的Hexo首页面（与之前本地测试时一样）。

### 选择Hexo主题及发表文章
#### (1) 下载Next主题
我自己用的是Next主题，有很多版本，我没有使用最新的，用了个5.1.1版本 [下载地址](http://pan.baidu.com/s/1bJXJdG)

下载之后解压，重命名为next,拷贝到C:\hexo\themes 目录中即可

#### (2) 修改网站的主题为Next

打开C:\Hexo下的_config.yml文件，找到theme字段，将其修改为next
```bash
# Extensions
## Plugins: http://hexo.io/plugins/
## Themes: http://hexo.io/themes/
theme: next
```
#### (3) 本地验证是否可用

输入
```bash
hexo s --debug
```
访问本地网站[http://localhost:4000/](http://localhost:4000/)，确认网站主题是否切换为Next.

#### (4) 更新Github
在git中进入网站根目录 
```bash
$ cd c:/hexo
$ hexo -g #编译本地内容
$ hexo -d #发布到github
```
这里可能会报错，如果提示需要安装hexo-deployer-git插件，就执行以下语句：
```bash
$ npm install hexo-deployer-git
```
之后重新部署发布即可

### 发布文章
这里可以参考hexo的官方文档，通过命令的形式来玩
```bash
hexo n "name of the new post"
```
回车后，在source文件夹下的_post文件夹下，可以看到新建了一个name of the new post.md的文件
也可以到C:\hexo\source\_posts 目录下直接新建.md 结尾的文件就可以了，所以平时如果写了markdown格式的文档可以拷贝到这个路径下直接就发布了

完了之后走一遍：
```bash
hexo g -d
```

关于文章，注意需要使用markdown语法进行书写,这里推荐一个markdown的[简明语法介绍](http://ibruce.info/2013/11/26/markdown/)

### Goddady 域名与github博客地址绑定

截止到目前为止，你应该可以通过访问[http://MyGithub.github.io](http://MyGithub.github.io)来看到以上创建的网站了。

但是，如何拥有一个属于自己的域名地址，并将其指向在Github上所创建的网站呢？

#### 注册域名
我选择了国外的[Goddady](https://sg.godaddy.com/zh?isc=gennbacn29&countrview=1&currencytype=CNY&mkwid=WFSMCUdy&cvosrc=ppc.baidu)进行域名的注册  花了我29大洋申请了个域名[barrysite.me](http://barrysite.me/),怎么注册买东西这里不说。只谈绑定操作

##### 进入godaddy DNS 管理界面

##### 修改如下两个地方
![1](https://github.com/myAccount/blogMaterial/blob/master/1.jpg?raw=true)

类型为A的地方，IP地址修改为Githup服务器ip地址，通过以下命令获取：
```bash
ping github.io
```

类型为CNAME的地方，值修改为博客地址 如：myAccount.github.io

##### 添加CNAME文件到Github对应的repository
这里注意的是不要直接在github上建立这个文件，要在hexo的sources目录下新建个CNAME
内容就是你购买的域名,如我的：
```bash
barrysite.me
```


之后重新部署发布即可。 至此，可以通过自己的域名直接访问博客了。[我的博客地址](http://barrysite.me)


### Hexo Next主题下基本配置

列举了安装之后如何订制你的博客，请参考我的另一篇文章：
[Hexo Next主题下基本配置](http://barrysite.me/2017/05/07/Hexo%20Next%E4%B8%BB%E9%A2%98%E4%B8%8B%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE/)





