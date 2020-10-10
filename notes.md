
### 创建scrapy项目

```shell
scrapy startproject [project name]
```


### 创建爬虫

```shell
scrapy genspider [spider name] [domain name]
```


### 运行爬虫

```shell
scrapy crawl [spider name]
```

### response

response对象调用.xpath()或者.css()方法返回的是网页内容预加载的Selector对象，只有当调用了.extract()或者.re()方法的时候才会返回真实的文本数组。
实际上.css()在后台会编译成xpath()表达式。

