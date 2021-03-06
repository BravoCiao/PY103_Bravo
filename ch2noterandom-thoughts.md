#### 最终代码思路是： {#-}

* 只写一个Class，里面包含了Frame、放在Frame里面的各组件、引用的文件、创建的字典和List，与按钮相对应的指令在下面定义方法，最后进入窗体主循环。在写的过程中，去掉了messagebox，只留下最基本的窗口。

#### 本周大事记： {#-}

#### • 用语言学习逻辑&数学？ {#-}

大猫的教程里拆了一个官方文档，把每一个英文对应的含义用中文封装好，比如Class是类、Application是类名、**init**是一个初始化函数...学习GUI的一个难点在于tkinter的英文文档中，没有像大猫的教程把各个部分拆解得这么细致的，再加上毕竟英文不是母语，也囿于技术功底薄弱看不到全貌，阅读Reference一直是似懂与非懂之间的角力战，语言隔阂带来文化陌生感，用\[大侠—杨过\]类比\[类—类名\]自然比\[Laptop—MacBookPro\]来得亲切。

困顿在技术与语言筑起的圆墙中，凭一己之力做不成飞翔在天空的鹰，也没办法和别人合作建起通天的巴别塔。

Howard Earl Gardner在1983年提出了多元智能理论，如果参照这个理论模型，我想我是语言智能开发大大超过逻辑&数学智能的类型，我的学习过程大大依赖文字解释。  
不管中文、英文，名词锚定对我来说重要的一点是让无形的收束住边界，变得有形可分类，当非可视化的功能有了名词这个盒子去盛放、去划定边界，代码就可以看成是一个个大盒子、小盒子的嵌套排布。当弄清楚了每个盒子封装的内容，我就逐渐能看清不同同学的架构逻辑了。

#### • 最小行动！最小行动！最小行动！ {#-}

本周的学习是一个不断精简、只求最小行动的过程。

##### ♢ Macro: {#-macro-}

原先的设想是做一个美观的界面，周二下载了背景图、天气图标，构思好了查询系统的视觉和概念主题、思考了怎么摆放按键、搭配字体。时间进度条拉到周四，此时只完成了两个半的功能。只能把要求精简到完成主要功能就好。储存的资料图只好搁置在硬盘仓库里，等到以后有机会再开封。  
这是我目前跟着Py103课程，觉得技术的使用最能接近我脑中理想图景的一次，但没有能力完成，是最大的憾事。

一开始想着复用上一周的成果节省时间，探索module半天无果，决定放弃引入另一个变量增加复杂度，用笨办法把所有指令写在了一个python文件里面，只调用了weather\_info.txt文档。  
和我储物的偏好类似，在不确定每一个储物柜里要放什么之前，先把所有书和工具摊开在敞开的架子上，建立眼睛和物品的直接联系，足够简单清晰、避免遗漏。等有了较明确的储物规划再入柜。

##### ♢ Micro: {#-micro-}

微观到代码部分。  
界面有四个按键，每一个按键和一个指令相连，Quit键的指令就是退出整个窗口，直接写出来不再定义。  
最后精简下来定义的方法只有三个：查询天气、得到历史数据和返回查询手册。  
查询天气的部分，也只精简到两种选择：1.查询到天气，返回数据；2.输入有误，查询help文档  
放弃messagebox，所有信息显示在一个窗口。

一切以最小行动为原则。

我的代码不完美，但我完成啦~ &lt;\(￣︶￣\)&gt;

##### Credits to： {#credits-to-}

[Shippomiru的教程](https://github.com/shippomiru/Py103/blob/master/Chap2/note/02-tkinter.md)  
从shippo的教程里了解到tkinter各部分的分类与层级关系  
[大猫的教程](http://www.huangdamao.com/2017/01/17/chap2note/)  
大猫拆了官方教程详细解释了代码各部分的具体细节

[fatfox的1.0版GUI代码](https://github.com/fatfox2016/Py103/blob/master/Chap2/project/weather_GUI.py)  
拆了fatfox的代码，每一行写了注释，把不清楚的地方手动挖出来  
[kunbao7的代码](https://github.com/kunbao7/Py103/blob/master/Chap2/project/guiDemo1.py)  
kunbao的代码结构清晰容易对应，功能也定义得很细致  
和kunbao的搭框架思路差不多，但kunbao引入了另一个python文件，这个放弃了。  
[柳白猿的代码](https://github.com/xbaiyuan/Py103/blob/master/Chap2/project/ch2_gui_basic.py)  
柳白猿也只引用了txt文件，参考了返回历史数据的写法

李明教练&假牙教练  
感谢忍受我很犟地硬是要用解释梳理完成每个部分才肯去完成代码...

#### 下一周行动指南： {#-}

* 多发issue
 
  虽然把自己的“醉点”放在众人面前供人浏览检视，需要克服极大的心理障碍，但可以梳理思路、避免“嘴巴比脑袋快“、能批量解决问题、避免低效、避兔麻烦人。



