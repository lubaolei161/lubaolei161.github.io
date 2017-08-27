---
title: "GitHub gitlab 堡垒机 账号配置"
comments: true
date: 2017-08-28
type: "categories"
categories: "配置"
tags: #文章標籤 可以省略
     - GitHub
description: Hexo博客多台机器同步
---



###  需要在本机同时配置github  gitlab  堡垒机SSH账号

#### 生成各种账号的rsa rsa.pub秘钥对

命令：`ssh-keygen -t rsa -C "$your_email"`

生成的密钥对存在文件夹  ~/.ssh 中

为了区分不同的秘钥对，在生成后制定文件名时分别加后缀， 如github，gitlab，如图所示：



![BD5DE693-706B-414E-817C-75FA7DFA7CF4](https://ws2.sinaimg.cn/large/006tKfTcgy1fiyq76le8yj30li0700u6.jpg)

之后将各个pub 文件分别上传至对应的网站

#### 在~/.ssh 中建立config 文件

vim config  内容如下：

```Shell
host *
ControlMaster auto
ControlPath ~/.ssh/master-%r@%h:%p

Host js
    HostName ops-jumpserver-intra.yeshj.com
    Port 59155
    User myUsername
    IdentityFile ~/.ssh/id_rsa
ServerAliveInterval 80

Host github.com
    HostName  github.com
    User myUsername
    IdentityFile ~/.ssh/id_rsa_github
Host gitlab.yeshj.com
    HostName  gitlab.yeshj.com
    Port 22
    User myUsername
    IdentityFile ~/.ssh/id_rsa_gitlab
```



这个文件用来映射秘钥与 git网站的关系，实际账号啥的自己根据情况填写

前两段是用来ssh js 登陆堡垒机用的



#### 删除know_hosts文件

当前这个文件删除，之后会重新生成



----

至此，配置结束，可以分别使用gitlab github了，同时可以快捷登陆公司堡垒机







