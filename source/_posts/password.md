---
title: Hexo文章简单加密访问
date: 2017-05-31
tags: hexo
categories: github博客搭建
keywords:
	- Hexo
	- 加密
description: 网上找的简单的加密文章的办法，通过alert  实现
password: password
---

### 网上找的简单的加密文章的办法，通过alert  实现
找到themes->next->layout->_partials->head.swig文件。
按道理是添加在任何地方都行，但是推荐加在所有的<meta>标签之后，个人建议，仅做参考。以下是我加的代码：

```java
<script>
    (function(){
        if('{{ page.password }}'){
            if (prompt('请输入文章密码','') !== '{{ page.password }}'){
                alert('密码错误！');
                history.back();
            }
        }
    })();
</script>
```

---
使用时候，头部加入password标签，后面跟密码即可


