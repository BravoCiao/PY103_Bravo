完成了开学前的准备，下面进行第一周的任务



Ch0 的任务是：



- 熟悉基础环境配置 

- 用Python3.x改写LPTHW里面5±2个练习



不要以为Ch0的任务会是最简单的，你一个小白在初期的环境配置上会栽进大坑，这些坑就是大黑洞，“咻咻咻”地把你的时间全部吸光。



知道什么是GitBook，什么是CLI，什么是Fork吗，什么是Clone吗？全都不知道吧，你满脑子就是技术的浪漫浪漫浪漫，Une Fille Naïve.



即使学扎克伯格用纸胶带把笔记本摄像头贴起来，我都能看到你做配置时候，大脑仿佛逆生长不只10岁，一脸痴呆的表情。



系统、软件版本、Terminal...这些全是变量，面对这些变量最好是选择受众面广的、更常规的配置，可以求助的范围更广，提高学习体验。面对不懂的术语就要查，现在就把Google和仓库里给的资料全用起来吧！







有些坑还是避无可避要踩一踩的...下面列出来你有可能踩到的坑，以及解决过程供参考。



\#\#\# 让 Python2 和 Python3 在系统中共存



系统：Window8



在之前的练习中，使用的是Python2.7.13，现在要开始使用Python3.x，在官网上下载最新的Python3.6.0并安装



你遇到的第一个疑问会是：不知道在Powershell里面直接输入Python，系统要怎么区分是Python2还是Python3：\[请参考网上的设定\]\(http://jingyan.baidu.com/article/b87fe19e94ca95521935686e.html\)







你一开始一定不知道怎么用英文准确描述自己遇到的问题，搜出来的答案也不会是你想找的，技术类文档缺乏相应背景知识阅读起来很困难。初期只能委屈一下，看下中文的教程，入门之后尽快摆脱中文依赖，要看也要选择优质的中文资源，比如知乎上优质答主的答案以及优质博主的博文



根据教程修改环境变量里面的Path，但是Python3.6的安装文件夹名是Python36-32，在环境变量里Python36和Python36-32都试过了



Powershell依然运行不成功

![](/assets/截图81.png)

必要时求助教练，发现在CMD里面可以运行

![](/assets/截图82.png)

尝试在Powershell里面运行$env:path 命令，看看Powershell 是不是没有读取到环境变量配置，结果如下：

![](/assets/截图84.png)

之后改换更低的Python3.5.2版本，在教练的指导下，根据Python3.5.2的安装路径，把环境变量里面Path的变量值改成：



c:\python27;c:\python27\scripts;c:\users\admin\appdata\local\programs\python\python35;c:\users\admin\appdata\local\programs\python\python35\scripts



终于成功在Powershell里运行Python2 & 3。



但，这并不是结束。



\#\#\# 安装IPython & 更换Terminal为Gitbash



星期六有在线答疑，准备安装IPython，试了几次不成功在群里求救，没想到还会发现新的问题。



用学友给的代码，安装成功IPython，但检查之后才发现是被安装到了之前因为其他原因没有被顺利卸载的Python3.6.0目录下，李明教练还建议把小众的Powershell换成Gitbash，这样能更容易得到解答。但是安装Gitbash之后发现读取不了Python，在网上Goo到的资料显示，Gitbash也要修改相应的path，修改了之后重启Git发现可以运行了，但后来经过教练提点，发现并不是因为修改了Path的原因，是之前没有重启Gitbash。



虽然那篇资料是英文文档，但不是官方手册，没有及时跟上Git最新的优化。所以入了门，有了基本的技术知识还是阅读官方手册会更准确、少走弯路。



在Python自己的官方手册中，显示安装包里面有勾选安装Launcher的选项，倒数第二个小框

![](/assets/1664448490.jpg)

根据\[官方文档\]\(https://docs.python.org/dev/using/windows.html\\#python-launcher-for-windows\)



如果勾选了Launcher，就不必修改环境变量里面的Path了。



最后的解决方案是，把Python3.6.0和3.5.2全部删掉重装Python3.6.0，勾选Launcher，不修改Path。









\#\#\#进行到了这一步，基础的配置是：



系统：Windows8



Python版本：Python2.7.13 & Python3.6.0



Terminal：Gitbash2.11.0



其他工具：IPython







PS:一个要注意的问题是，在提问时候尽量把问题全部说清楚，不要遗漏重要细节，即使自己知道没有提蠢问题，也不要让自己看起来很蠢。嘴巴不要比手快。

