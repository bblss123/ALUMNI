# ALUMNI

ALUMNI一个开源的校友会平台

## 依赖

运行pip install -r requirement.txt安装以下依赖，或手动输入以下代码

```
django==3.2.5
xlrd==1.2.0
requests==2.25.1
requests-html==0.10.0
pyexcel-xls
```

## 目录介绍

后端项目的目录如下

```
Fduers/
|----Fuders/        存放django的配置文件
|----alumni/        存放后端的主要代码，包括数据库模型等一系列代码
|----functionality/ 存放功能性函数
|----generator/     存放测试数据生成器
```

## 进度

前端:
```
templates/
|----home1.html     主站
|----tie.html       帖子页面
|----tieLists.html  筛选器跳转
```

需要完成：
1. 主站

* 热点话题的内容渲染
* 点击帖子标题后帖子数据的传输
* 与发帖、个人主页等页面的跳转

2. 帖子

* 帖子内容的渲染
* 回贴渲染
* 跟帖的表单提交之后的渲染（目前预留了一个div display:none）
