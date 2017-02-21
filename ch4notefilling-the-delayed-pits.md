本周的任务是把API、CLI和Web联系起来，完成一个内网可用的天气查询系统。

任务要求：  
完成一个网页版天气查询程序，实现以下功能：  
基本功能

* 输入城市名，获取该城市最新天气情况
* 点击「帮助」，获取帮助信息
* 点击「历史」，获取历史查询信息
* 部署在命令行界面

卡包已经给任务进行了分拆：

* 利用 HTML，CSS 等生成网页
* 使用 Web 框架 Flask 与浏览器进行交互
* 完成一个内网可用的天气查询应用
 
  ———————————————————————————————
* 服务器和浏览器之间是如何实现交互的？  
  浏览器发送请求到服务器，服务器收到请求再进行响应，传送一个HTML文档到浏览器生成页面，重复。这个就是基本的浏览器—服务器交互流程。无论这个过程中涉及到多复杂的语法，浏览器接收到的永远是HTML文件。

* HTTP  
  HTTP\(The Hypertext Transfer Protocol超文本传输协议\)是服务器和浏览器进行沟通的语言。

* HTTP Method  
  不同的HTTP方法对应不同请求\(request\)，基本的Method有GET和POST, 它们都是在和服务器要响应，不同点在于，POST会传给服务器用户要修改的数据。打个比方，都是去披萨店买披萨，GET是直接向老板要Menu上现成的搭配，照着编号点餐就行，POST可以自己决定要8寸还是12寸，夏威夷口味还是全肉宴，是不是多加层Cheese等等。  
  要在Flask里面使用HTTP方法，我们需要引入request：  
  `from flask import request`

* HTTP Response Codes  
  每做了一个HTTP请求，服务器都会返回一个编码，告诉我们状态如何。  
  具体请参考：[List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

* HTML、CSS  
  所有我们看到的网页，按钮排布、颜色、背景、内容，这些安排都是被写在HTML文件里的，浏览器接收到的都是HTML文件并进行读取，HTML文件里面会包含HTTP命令，HTTP命令和内容有关，其他的HTML语法和排版有关。CSS可以用来进一步进行美化工作。  
  HTML写法参考这个：[HTML Basic Examples](https://www.w3schools.com/html/html_basic.asp)

* 为什么我们需要网页框架？ Flask框架  
  所有的网页，不管是简单的、炫目的，背后都是代码由代码实现的。Flask是一个在Python里写就的微型网页应用框架，其他的框架还有Django.

官网上给的MVP代码：

```
from
 flask 
import
 Flask
app = Flask(__name__)

@app.route('/')
def
hello_world
()
:
return
'Hello, World!'
```

用浏览器打开，可以看到'Hello, World!'字样显示在网页当中，更加复杂的内容排布可以通过HTML文件写成。

* 装饰器&为什么要有装饰器  
  装饰器本身就是一种函数，它被用来打包另外的函数，给其他函数增加额外的功能，目的是让代码结构清晰。语法是在最前面加@，上面使用了route\(\)装饰器。

* Flask&HTML  
  Flask是Web Framework，翻译过来是网页框架，HTML用来描述我们看到的那个网页框架，用中文说似乎都是网页框架，那怎么准旗区分它们？用英文辅助，Flask是支持整个浏览器—服务器之间交互的Structure，而HTML是网页的appearance，打个粗疏的比方就是，Flask是支撑人立起来的骨骼结构、人体这个系统运作的逻辑，HTML是脸面：鼻子放哪里、眼睛要多大、涂不涂口红之类的...

* Jinja2模板&为什么要使用模板？  
  模板的目的，是用来实现HTML文件和代码的分离，因为例如要写一个长达6000行的HTML文件在代码里是不现实的，用了模板可以让代码简洁、结构清晰，也更好维护。  
  Jinja2是Python内置的模板语言，Flask已经内置了Jinja2模板，只要已经安装好了Flask就可以使用Jinja2，模板仅仅是文本文件。它可以生成任何基于文本的格式（HTML、XML、CSV、LaTex 等等）。 它并没有特定的扩展名， .html 或 .xml 都是可以的，这里我们使用HTML格式。

* render\_template  
  如果要在Flask中使用模板，就要用render\_template方法，下面是官网给出的MVP代码：

  ```
  from
   flask 
  import
   render_template

  @app.route('/hello/')
  @app.route('/hello/
  <
  name
  >
  ')
  def
  hello
  (name=None)
  :
  return
   render_template(
  'hello.html'
  , name=name)
  ```

  我们需要建立一个名为templates的文件夹，存放模板文件,代码运行时候会自动去这个文件夹里面找文件。

* 坑  
  开发网页应用这一章最大的坑就是不知道怎么实现HTML、Flask和API之间的联系，逻辑框架都有，就是败在细枝末节。

  * GET与POST的对应
  * request.form\['xx'\]、request.args.get\("yy"\)里面，xx、yy对应的值到底是HTML文件里面的那一个？
  * return render\_template\('index.html',weatherdata=weatherdata\)，\(\)里面对应的到底是HTML里的哪一部分？

    ```
    @app.route('/',methods=['GET','POST'])
    def
    index
    ()
    :
    if
     request.method == 
    'POST'
    :
        cityname = request.form[
    'cityname'
    ]
        weatherdata = get_weather(cityname)
        historylist.append(weatherdata[
    0
    ]+weatherdata[
    1
    ]+weatherdata[
    2
    ])
    
    return
     render_template(
    'index.html'
    ,weatherdata=weatherdata)


    elif
     request.method == 
    'GET'
    :
    
    if
     request.args.get(
    "button"
    ) == 
    'History'
    :
        
    return
     render_template(
    'index.html'
    ,
                                            searchhistory=historylist)
    
    elif
     request.args.get(
    "button"
    ) == 
    'Help'
    :
        
    return
     render_template(
    'index.html'
    ,
                                            Help=
    ' '
    )
    
    else
    :
        
    return
     render_template(
    'index.html'
    )
    ```

    这是主程序的一段代码，里面的if..elif相应的request.method对应的是HTML文件里面的GET和POST  
    request.args.get\("button"\) == 'Help':，button对应HTML文件里的name=button，==‘Help’对应value="Help"  
    我一开始把HTML文件里POST请求的city\_searched错误对应到主程序的代码里，结果传入的值一直是value="Submit"，一直得不到正确的结果。

    ```
    <
    form
    action
    =
    "/"
    method
    =
    "post"
    >
    <
    input
    type
    =
    "text"
    name
    =
    "cityname"
    /
    >
    <
    br
    /
    >
    <
    br
    /
    >
    <
    input
    type
    =
    "submit"
    name
    =
    "city_searched"
    value
    =
    "Submit"
    /
    >
    <
    /
    form
    >
    <
    form
    action
    =
    "/"
    method
    =
    "get"
    >
    <
    input
    type
    =
    "submit"
    name
    =
    "button"
    value
    =
    "History"
    /
    >
    <
    input
    type
    =
    "submit"
    name
    =
    "button"
    value
    =
    "Help"
    /
    >
    <
    /
    form
    >
    <
    center
    >
    {% if weatherdata %}
        
    <
    p
    >
    {{weatherdata[0]}} {{weatherdata[1]} {{weatherdata[2]}}
    <
    /
    p
    >

                {% elif Help %}
        
    <
    p
    >
     · 输入 『城市名』，查询该城市的天气 
    <
    /
    P
    >
    <
    P
    >
     · 点击 『Help』，获取帮助文档 
    <
    /
    P
    >
    <
    P
    >
     · 点击 『History』，获取查询历史 
    <
    /
    p
    >

                {% elif searchhistory %}
                    {% for city_searched in searchhistory %}
                    
    <
    p
    >
    {{city_searched}}
    <
    /
    p
    >

                    {% endfor %}
                {% else %}
                {% endif %}
    
    <
    /
    center
    >
    ```

    render\_template\('index.html',weatherdata=weatherdata\)，\(\)里面的参数，对应的是HTML里，if语句的条件，给哪个条件赋值，就做哪个条件相应的指令。



