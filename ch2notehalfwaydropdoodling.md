必完成任务：

* 输入代码、调用桌面软件
* 输入城市名，获取对应的天气情况
* 点击 Help，获取帮助信息
* 点击 History，获取历史查询信息
* 点击 Quit，退出程序

选做任务：

* 增加活动条
* 重新安排按键布局
* 设定默认程式

配置更改：  
经过大妈指点，把terminal从cmd换成了cmder

用《怎样解题》的方法分拆任务：  
已知量：Ch1 MVP 任务的代码、 列表里的Reference  
未知量：五个需要实现的功能  
条件：在图形交互的界面中实现这些功能

* 研究tkinter
 
  参考
  [25.1. tkinter— Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
 
  在命令行用py -m tkinter，调出了一个界面，如图：
  ![](/assets/截图02.png) 
  检查出来tkinter已经安装好了，是tcl/tk version 8.6

第一时间想到的是给自己节省时间、提高效率，阅读了Reference里的  
[6. Modules — Python 3.5.3rc1 documentation](https://docs.python.org/3.5/tutorial/modules.html)  
知道可以在tkinter里面引入Ch1 MVP的代码作为模组，模组就是保存为.py的形式

参考[An Introduction To Tkinter\_Part I\_Hello, Tkinter 的内容](http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm)  
提供的试运行代码如下：  
from Tkinter import \*

root = Tk\(\)

w = Label\(root, text="Hello, world!"\)  
w.pack\(\)

root.mainloop\(\)

在tkinter中调用模组\(module\)的基本语法是  
import tkinter / from tkinter import \*

『 注: An Introduction To Tkinter教程给的是from Tkinter import \*，但T为大写没办法在我的cmder里面运行，全部改成小写。』

root = Tk\(\)  
如果要启动tkinter，需要在代码中输入tkinter root widget ，会生成一个包含标题栏的窗口。每一个程序只能有一个root widget，而且要在其他widget之前创建。

w = Label\(root, text="Hello, world!"\)  
w.pack\(\)  
接下来是Label widget，Label widget可以显示文本、图标或图片。  
pack是让Label widget去自动适应括号里面的内容大小，并且让内容可见。

root.mainloop\(\)  
如果没有输入tkinter event loop，那么窗口就不会显示出来。  
event loop不只会保存用户的行为记录，例如点鼠标、打键盘，或者窗口活动，比如改变窗口大小，还会有顺序地记录下tkinter内部的活动（由pack指令排序）、记录更新。

#### · 了解了tkinter引入模组的代码和其他注意点 {#-tkinter-}

————————————————————————————————————  
接着下一课：[An Introduction To Tkinter\_Part I\_Hello, Again](http://effbot.org/tkinterbook/tkinter-hello-again.htm)  
这一课的示范代码：  
————————————————————————————————————  
from Tkinter import \*

class App:

```
def
__init__
(self, master)
:


    frame = Frame(master)
    frame.pack()

    self.button = Button(
        frame, text=
"QUIT"
, fg=
"red"
, command=frame.quit
        )
    self.button.pack(side=LEFT)

    self.hi_there = Button(frame, text=
"Hello"
, command=self.say_hi)
    self.hi_there.pack(side=LEFT)


def
say_hi
(self)
:
print
"hi there, everyone!"
```

root = Tk\(\)

app = App\(root\)

root.mainloop\(\)  
root.destroy\(\) \# optional; see description below  
————————————————————————————————————  
分拆代码：

class App:  
def**init**\(self, master\):  
frame = Frame\(master\)  
frame.pack\(\)

这个app以class的形式写成，**init**是由Frame这个母widget\(the master\)构成的，母widget相当于一个容器，盛放这段代码中的另外两个子widget。母widget的内容是frame这个变量。用pack让frame这个widget可见。

接下来是两个叫Button的子widget：

self.button = Button\(frame, text="QUIT", fg="red", command=frame.quit\)  
self.button.pack\(side=LEFT\)

self.hi\_there = Button\(frame, text="Hello", command=self.say\_hi\)  
self.hi\_there.pack\(side=LEFT\)

第一个子widget给了Label叫Quit，fg是foreground的缩写，用来改变字体的颜色，第二个子widget的Label是Hello，两个子widget都接到一个命令指令，也都有pack让子widget变得可见。括号里面的side=LEFT是让两个按钮靠左排列，第二个挨着第一个放，像这样：

如果括号里面没有指令，按钮会靠上边放置  
def say\_hi\(self\):  
print "hi there, everyone!"  
say\_hi\(self\)是第二个子widget的指令内容，打印“hi there， everyone！”

root = Tk\(\)

app = App\(root\)

root.mainloop\(\)  
root.destroy\(\)

用root widget启动tkinter，app = App\(root\)说明App class在这个root widget里面运行，用root.mainloop\(\)结束代码。root.destroy\(\)只有在某些开发环境下才需要。

学会了Button widget，对应需要完成的三个功能：History、Help 和 Quit，模仿例子写代码：

![](/assets/截图03.png)![](/assets/截图04.png)

试图引入Ch1的代码，但是引入的效果和之前一个星期的task效果一样：

![](/assets/截图05.png)

另：如果root widget里面的tk写小写的，代码运行不了：

![](/assets/截图06.png)

![](/assets/截图077.png)

先放弃引入Module，实现Help、Quit按钮和窗口:

![](/assets/截图099.png)

运行出来会有这样的问题：

![](/assets/截图088.png)



上Google查，根据这篇帖子[Python AttributeError: Object has no attribute](http://stackoverflow.com/questions/11685936/python-attributeerror-object-has-no-attribute)第一名的答案  
猜测是某些标点的问题  
把button.help和button.quit中的.替换成\_,之后运行成功，猜测是.xxx会被python认为是一种method  
运行成功的效果：

![](/assets/截图100.png)

* ~~输入代码、调用桌面软件~~
* 输入城市名，获取对应的天气情况
* 点击 Help，获取帮助信息
* 点击 History，获取历史查询信息
* ~~点击 Quit，退出程序~~

点击Help按钮，获取到的帮助信息是在terminal里面显示的，不算完全成功  
梳理一下，现在还需要完成的有：

* 点击History，获得的帮助信息显示在窗口里面，而不是Terminal里面
* 创建能输入城市名的窗口
* 把指令和天气信息文档连接起来
* 点击History，反馈历史信息

Entry Widget和创建窗口的功能对应，研究[The Tkinter Entry Widget](http://effbot.org/tkinterbook/entry.htm)，把给出的代码复制到编辑器里面，再对照页面的说明以及[Python Tkinter Entry](https://www.tutorialspoint.com/python/tk_entry.htm)一起理解，大概摸清楚了Entry Widget的写法和规则。

```
                                                      |
                                                      |
                                                      |状 
                                                      |况
                                                      |急
                                                      |转
                                                      |直
                                                      |下
                                                      |，
                                                      |来
                                                      |到
                                                      |周
                                                      |四
                                                      | 。
                                                      |
                                                      |
```

记笔记的好处是，随时可以拿来回顾之前对自己的忠告。  
中间一直关注issue动态，从周四开始读同学教程、尝试自己写代码。  
尝试的中间比较值得一提的一点是，代码写成这样的话：

![](/assets/截图111.png)

点击History输出的结果只有最后一次查询的结果：

![](/assets/截图122.png)

但是后来经过教练指导，给修改了一下，我研究之后，发现是list给写到def**init**下面了，推测是把数据写在def**init**下面，所有其他def的对象都可以调用，如果写在其他def下面，每次都会生成新的数据。  
最后的版本是把所有txt文档的调用和读取进字典全部放在def**init**下面。

  
一周的时间刨去写代码的探索期，暂时没能力像大猫一样站在一个引领者的角色给六个月之前的自己写教程，试试看之后几周行不行，或者换一个写作方式。

