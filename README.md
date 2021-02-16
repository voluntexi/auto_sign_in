疫情自动打卡（青柠疫服）  
---
感谢“ FunkyPants”的”daka“项目提供思路
---

使用教程：

* 配置Python运行环境

 - WIN+R 输入CMD-> CD到该自动打卡脚本目录，执行 

  ```
  pip install -r requirements.txt
  ```

* 安装模块
  * selenium 
  * request 

 - 下载对应浏览器版本的 webdriver 。（本程序默认为谷歌浏览器，可自行修改）并存放到本文件夹下。并修改代码中 webdriver 的路径。

   具体操作：

    - 以谷歌浏览器为例子，打开浏览器在设置->关于里版本即为当前浏览器版本
    - 然后打开下面连接，寻找到和浏览器版本相同的文件->根据电脑系统下载->解压->存放在该自动打卡脚本目录
    - webdriver 下载地址：http://chromedriver.storage.googleapis.com/index.html

 - 打开autoBadgeSystem.py在相应位置修改名字、学号、密码等变量。
- 进入百度开放平台：https://ai.baidu.com/获取文字识别，根据提供文档获取相应的Access_token
- 打开recognize.py在相应位置输入获取的Access_token
 - 运行 autoBadgeSystem.py

---

百度的文字识别接口，需要一个月更新一次AT

更新方法见百度开放平台




