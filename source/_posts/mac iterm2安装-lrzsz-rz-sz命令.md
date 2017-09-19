---
title: ' mac iterm2 安装 lrzsz rz sz命令'
comments: true
type: categories
categories: 配置
tags:
  - mac
description: iterm2 加入sz rz命令支持
abbrlink: 31913
date: 2017-08-30 00:00:00
---





### mac需要先安装brew

执行：

```shell
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```



### 安装

1. Install lrzsz on OSX: `brew install lrzsz`
2. Save the `iterm2-send-zmodem.sh` and `iterm2-recv-zmodem.sh` scripts in `/usr/local/bin/`
3. Set up Triggers in iTerm 2 like so:

```Shell
    Regular expression: rz waiting to receive.\*\*B0100
    Action: Run Silent Coprocess
    Parameters: /usr/local/bin/iterm2-send-zmodem.sh
    Instant: checked

    Regular expression: \*\*B00000000000000
    Action: Run Silent Coprocess
    Parameters: /usr/local/bin/iterm2-recv-zmodem.sh
    Instant: checked
```



以上第三点设置位置：

![QQ20170830-215600](https://ws1.sinaimg.cn/large/006tNc79gy1fj23qc274qj30pi0fsace.jpg)

![QQ20170830-215629](https://ws2.sinaimg.cn/large/006tNc79gy1fj23qg4gd9j30mc09w0tg.jpg)



参考文档：https://github.com/mmastrac/iterm2-zmodem