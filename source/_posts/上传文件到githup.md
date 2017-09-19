---
title: 上传文件到github
comments: true
type: categories
categories: github学习
tags:
  - github
abbrlink: 33472
date: 2017-05-06 00:00:00
description:
---

### 创建自己的github资源库
登录自己的github帐号，然后创建资源库，这里我随意创建了 blogMaterial 仓库

初始界面如图：


![d](https://github.com/myAccount/image_home/blob/master/image/1.jpg?raw=true)

### 打开git命令行工具
#### 1. 到自己存放github项目的文件夹 我在本地文件夹为C:\github_folder，进入这个文件夹
``` bash
$ cd github_folder/

```

#### 2. 在自己本地clone这个仓库
``` bash
git clone https://github.com/myAccount/blogMaterial

```


#### 3. 进入clone 的这个文件夹子
在Windows系统里可以直接进入这个文件夹，做你的操作，比如新建个文件夹，或者文件，如图
![2](https://github.com/myAccount/image_home/blob/master/image/2.jpg?raw=true)

### 同步到github

执行命令：
```bash
git add *  #可以将当前目录下所有改动都加到待提交状态
git add [文件夹名称] #将该文件夹内容加到待提交状态
git add filename  #单个的文件  当然也可以用通配符啥的 如*.txt

git status #可以查看下有那些发生了改动

git commit -m "测试" #提交改动

git push origin master #上传到github

```

可以看到发生了如下变化：
![3](https://github.com/myAccount/image_home/blob/master/image/3.jpg?raw=true)