# downloading all of PDF file on the entire site

[TOC]


## parameter:

- raw_url
    用于下载的网站名
- root_url
    当出现了下载地址是省略的，在下载地址前加入根地址


## example

由于最近在学习machine learning, 在线观看 斯坦福大学 教授 Andrew Ng 的上课视频，在斯坦福的授课官网上下载课件：

root_url = "http://cs229.stanford.edu/"

raw_url = "http://cs229.stanford.edu/materials.html"

## expectation

该代码并非完完全全是自己编写的，大部分事网上借鉴的，由于下载的网站不同，我对正则表达式进行了修改，加了[^...]  避免了出现 href="http://blah~.php",<a\>dad</a\>href="http://blah ~  .pdf" 匹配问题
