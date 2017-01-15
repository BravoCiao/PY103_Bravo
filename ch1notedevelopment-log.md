首先，根据卡片从github库里面领取天气数据文件，因为把文件用Github同步到自己fork生成的仓库，不是这一周的主项目，所以暂时放在一边，天气数据是直接复制粘贴到txt编辑器里面的。

我也想优雅，但还是先解决大任务再想姿态的问题吧。

连同上一周的CLI，现在有下列不影响主任务完成，但了解了会提升效率的子任务有待完成：

* CLI
* 搜索Git Remote、Git Fetch、Git Pull

我的方式是每次达到一个最小行动，然后一步步跟进更新，最后完成目标。

一共有四个功能要完成：

* 输入城市名字，获取该城市的天气情况；
* 输入指令，获取帮助信息；
* 输入指令，获取历史查询信息；
* 输入指令，退出程序。

### Function 1：输入城市名字，获取该城市的天气情况 {#function-1-}



##### Function 1· Step 1：读取Weather\_info.txt里面的数据 {#function-1-step-1-weather_info-txt-}



下载完天气数据之后，先根据[lpthw第16课的内容](https://learnpythonthehardway.org/book/ex16.html)，Reading and Writing Files,以及读写教程：[Python 读写文件参考 Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

简单地写了一个程序，完成第一个小目标、能成功读取天气数据后再进行下一步的搜索  
但运行时候出现了如下的问题：

![](/assets/截图01.png)



怀疑是读取中文字符出现问题，写了一个纯英文的文档进行读取，发现可以运行。

到Google上进行了搜索，首先看了英文网页，发现其他人的问题中除了这一项，还会混杂其他干扰因素，对我的问题没有针对性，接着打开[搜索关键词得到结果排第一的知乎网页](https://www.zhihu.com/question/22699590)，按照答案给的方法，

修改txt = open\(filename,'r'\)为txt = open\(filename,'r',encoding = "utf8"\)

成功运行读取程序。  
了解了是字符串和编码的问题，去看了reference里面[廖雪峰的博文](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)



#### 摘录如下： {#-}



——————————————————————————————————————————————————————————————————————————  
"但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。

因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。

现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

字符 ASCII Unicode UTF-8  
A 01000001 00000000 01000001 01000001  
中 x 01001110 00101101 11100100 10111000 10101101  
从上面的表格还可以发现，UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。  
用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件："  
——————————————————————————————————————————————————————————————————————————

#### 摘录结束

所以我们保存的txt文档是用UTF-8编码的，在文档中打开转换成Unicode编码，但是作为文件保存的时候是UTF-8编码，Python3采用Unicode编码，所以没办法识别UTF-8编码的文件，需要在打开的时候在括号里多加一个指令，encoding = "utf8"，转换编码类型进行读取。

第一步读取数据已经完成。



##### Function 1· Step 2：输入城市名 {#function-1-step-2-}



这个是之前学过的，需要引入input\(\)指令。

代码：

![](/assets/截图08.png)

运行结果：

![](/assets/截图07.png)

可以看见，可以得到输入的城市名，但是城市名没有办法和读取数据联系在一起



##### Function 1· Step 3： 根据输入的城市名，读取某一行的数据，研究字典 {#function-1-step-3-}



我尝试了f = open\(\)和f.read\(\),f.readline\(\)  
但是f.read\(\)能读取一整篇txt文档，f.readline\(\)能读取而且只能读取文档第一行

进行到这一步，我的困惑是不知道怎么根据城市名，找到这个城市在文档中的定位并且输出。卡片中的第三个问题：

* 读取之后是储存在什么数据类型里？

我不知道为什么要关注这个问题，但因为想不出来，先阅读了后面“把天气数据转化为字典”的卡片。

阅读完了reference里面给的三个链接，也没太有弄懂什么是dictionary，对于dictionary的概念，我感觉模糊不清，也不懂为什么需要dictionary。看了lpthw里面有关dictionary的[Exercise 39: Dictionaries, Oh Lovely Dictionaries](https://learnpythonthehardway.org/book/ex39.html),发现里面的dictionary都是自己输入的、数量有限的集合，不是一个和读取已有文件结合起来操作的指令。

我不知道怎么把两者结合起来。

之后参考了[Python Dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)，大概知道了dict要怎么写，接下来是考虑怎么把一个包含两列用“，”隔开数据的txt文档写进dict里面

先后参考了这两个链接：

[Python - file to dictionary?](http://stackoverflow.com/questions/4803999/python-file-to-dictionary)

[Python - converting textfile contents into dictionary values/keys easily](http://stackoverflow.com/questions/5942874/python-converting-textfile-contents-into-dictionary-values-keys-easily)

写出来的代码是这样的：

![](/assets/截图09.png)

给出的结果有如下问题：

![](/assets/截图10.png)

在Google上查，参考这个链接[Python 3.3 programming. ValueError: invalid literal for int \(\) with base 10. \(Beginner\)](http://stackoverflow.com/questions/13861594/python-3-3-programming-valueerror-invalid-literal-for-int-with-base-10-be)  
和[官方文档对int\(\)的解释](https://docs.python.org/3/library/functions.html#int)

猜测int\(\)是用于读取整数，而不是读取中文的

所以删掉int\(\),更新代码成以下这样：

![](/assets/截图11.png)

运行的结果是这样的：

![](/assets/截图12.png)

虽然不知道为什么有\n,但是我要的把两列数据用“：”分开的效果，是可以放进{}里面成为dictionary的格式，姑且认为读取文件进dict成功

参考lpthw里面[Exercise 39: Dictionaries, Oh Lovely Dictionaries](https://learnpythonthehardway.org/book/ex39.html)读取dict数据的操作，代码如下：

![](/assets/截图13.png)

实现效果是这样的：

![](/assets/截图14.png)

尽管有一些不完美，例如指令和结果不在一行上，以及输入的城市名带有' '，这样的小问题，这一步暂时算成功，先进行下一步，再完成改进。



##### Function 1· Step 4： 让查询天气的功能循环运行 {#function-1-step-4-}



先参考lpthw loop章节的教程：  
[Exercise 33: While Loops](https://learnpythonthehardway.org/book/ex33.html)

发现教程里面给的都是和数学相关的，数字可以比大小，但是文字没办法比大小，条件只能是看某一组文字是不是在一组文字的集合里面，这是我在Step 4碰到的第一个问题。

看到lpthw[Exercise 35: Branches and Functions](https://learnpythonthehardway.org/book/ex35.html)里面的这一行代码

```
if
"flee"
in
 choice:
    start()
```

可以尝试if-in这个指令

接下来的问题，前提是知道用户输入的内容，才能知道相应的输入能不能和文档对应上，也才能知道要不要进行循环，我不知道怎么做才更优雅，试了一种笨办法：把同样的代码复制粘贴两次。

代码是这样的：

![](/assets/截图15.png)

运行结果是这样的：

![](/assets/截图16.png)

第一个查询天气的功能完成了~

### Function 2：输入help，获取帮助文档 {#function-2-help-}



一旦建立好了代码结构，第二个功能实现起来很简单。

添加了下面这一段代码：

![](/assets/截图17.png)

实现效果：

![](/assets/截图18.png)

### Function 3：输入 history，获取查询历史 {#function-3-history-}



思路是新建一个list，用于把查询的历史写进这个list再进行读取。  
参考lpthw[Exercise 33: While Loops](https://learnpythonthehardway.org/book/ex33.html)

更新代码成这样：

![](/assets/截图19.png)

实现效果是这样：

![](/assets/截图20.png)

有一个小问题是，显示出来的只有城市名，缺少天气状况。先放在一边不管，等主要功能全完成了再回来改进。

### Function 4：输入 quit，退出天气查询系统 {#function-4-quit-}



在代码的最后加上：

![](/assets/截图21.png)

实现效果：

![](/assets/截图22.png)

至此，主体功能大致实现。

————————————————————————————主体功能实现的分割线——————————————————————————————————

### Debug Journal · 待解决大瑕疵： {#debug-journal-}

* 指令和输入结果显示不在同一行
* 输出“ 某某城市的天气状况为：”，这个某某城市上边带有' '标志
* 查询历史结果，输出的只有城市名，没有天气

依靠自己的力量实在无法解决问题了，前去围观学友@CallingCrab的代码，看到了这两行：

* x = input \('请输入您想要查询的城市名称'\)
* print \('%s的天气情况为' % x, weather\_dict\[x\]\)

把自己的代码更新成这个格式，运行结果：

![](/assets/截图23.png)

#### Debug Journal · ✔ · 第一个瑕疵剔除 {#debug-journal-}



在解决问题的途中又发现了新问题：



##### ————Bug分支 · 只有输入城市名才能进入循环，输入help、history就会自动退出循环 {#-bug-help-history-}

参考@CallingCrab的代码，加了一个while True：  
代码长这样：

![](/assets/截图24.png)

但问题是运行时候会跳不出循环，只能用Ctrl+C手动退出

![](/assets/截图25.png)

lpthw[Exercise 33: While Loops](https://learnpythonthehardway.org/book/ex33.html)里面使用的是数字，用数字判断真假，逻辑链简单直接，但是文字要复杂一点。

参考[Exercise 35: Branches and Functions](https://learnpythonthehardway.org/book/ex35.html),更新了代码，用了if，elif，else语法，成功运行代码。

![](/assets/截图26.png)

![](/assets/截图27.png)

##### ————Bug分支 · 解决 {#-bug-}



星期六晚上答疑，询问了剩下来的两个问题：  
第一个出现' '的错误是因为我用的是% r而不是% s，@yanzhiw 给了我lpthw[Exercise 24: More Practice](https://learnpythonthehardway.org/book/ex24.html)的链接作参考，这个是我知识的盲点，我一直以来都是认为% s是代表字符串，% r是raw\_input\(\),可以代表任何代码的部分，不管任何部分用% r都万事大吉。需要课下再把概念理清楚。



#### Debug Journal · ✔ · 第二个瑕疵剔除 {#debug-journal-}



不知道怎么把两个变量放进一个list里面，参考了[这篇帖子](http://stackoverflow.com/questions/14860460/append-several-variables-to-a-list-in-python)

把append\(\)改成extend\(\):

![](/assets/截图35.png)

可以打印出城市和天气，但不在同一行上：

![](/assets/截图36.png)

继续参考[这篇帖子第二名的答案](http://stackoverflow.com/questions/29513126/python-understanding-difference-between-append-and-extend)  
更新代码：

![](/assets/截图37.png)

运行结果，是显示在同一行了，但是中间没空格：

![](/assets/截图38.png)

最后参考[这篇帖子](http://stackoverflow.com/questions/12892698/adding-spaces-to-items-in-list-python)  
在extend\(\)加了一个空格字符' '

![](/assets/截图39.png)

总算是运行成功了！

![](/assets/截图40.png)

#### Debug Journal · ✔ · 第三个瑕疵剔除 {#debug-journal-}



———————————————————————————————意料之外瑕疵的分割线———————————————————————————————

### · 后续发现的新问题 & 改进 {#-}

阅读了已经关闭的issue，发现我原先的代码里面也存在print出来dict后面跟着\n的问题，参考了@yanzhiw在[这篇issue](https://github.com/AIMinder/Py103/issues/166)里面的建议：

知道了str.strip\(\)这个函数：

str.strip\(\[chars\]\)  
这个函数的用法是删除字符串左右两边符合chars的字符，如果为空，那么删除\n \t \r字符。

加了.strip\(\)这个函数在d\[key\] = val后面，像这样：

![](/assets/截图34.png)

print出来的dict就没有\n字符了

