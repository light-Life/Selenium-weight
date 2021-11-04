# 下面可能图片加载不出来，文章地址：https://hellohy.top/huayang/8294.html

# 项目介绍
此脚本使用 Selenium 爬取爱站权重进行分析<br>
主要是为了方便批量的时候少做无用功，更加迅速精准的提交
![](https://hellohy.top/wp-content/uploads/2021/11/image-13-1024x449.png)
![](https://hellohy.top/wp-content/uploads/2021/11/image-14.png)
![](https://hellohy.top/wp-content/uploads/2021/11/image-15-1024x259.png)
# 结构
![](https://hellohy.top/wp-content/uploads/2021/11/Selenium-weight-1024x538.png)
# 食用方法
## macOS
首先你得有 chrome

然后去下载 chromedriver

https://npm.taobao.org/mirrors/chromedriver

![](https://hellohy.top/wp-content/uploads/2020/11/image-14.png)
这里有很多版本目前最新的 chrome 下载这个即可
![](https://hellohy.top/wp-content/uploads/2020/11/image-22.png)

上点开访达然后 command+shift+g

搜索 /usr/local/bin 把下载好的文件拖进去就行了

然后运行这段代码看是否能正常调用

```
from selenium import 
webdriverbrowser = webdriver.Chrome()
```
如果正常调用并且没有报错则可以开搞

如果能调用但是出现秒退的情况则可能是 chromedriver 版本问题

## win 配置
https://blog.csdn.net/hijacklei/article/details/107876474

# 其他
师傅们看我这么用心给个 Star✩不过分吧ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊˚
