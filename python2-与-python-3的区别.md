\#\#\# 阅读官方文档



\#\#\#\# ·首先阅读\[官方文档：Should I use Python 2 or Python 3 for my development activity?\]\(https://wiki.python.org/moin/Python2orPython3\)，得到基本的知识：



最后一版Python2（Python2.7）于2010年发布，之后停止更新，第一版Python3于2008年发布，近几年一直在持续开发中，这就意味着，2010年之后库的更新全是在Python3上，从2到3，最显著的改变是3的所有字符串全部默认是Unicode形式。



- 在以下情况你才需要用Python2：



1.系统环境不受自己控制



2.希望使用第三方、不能和Python3直接匹配的软件包，而移植这个软件包又很不容易的时候



- 某些3.0和3.1的改进被移植进了2.6和2.7的版本中

，下面这些是3.x版本特有的功能：



strings are Unicode by default（字符串默认为Unicode形式）



clean Unicode/bytes separation（清晰的Unicode/字节分割）



exception chaining（异常链）



function annotations（函数注释）



syntax for keyword-only arguments（出现了针对只面向关键词参数的语法）



extended tuple unpacking（更长的元组解包功能）



non-local variable declarations（非本地变量声明）



翻译感觉漏洞百出...看文档像是隔靴搔痒一样没劲儿，要真正上手了才能理解是什么意思。



- 不仅仅是语法和语义上的变化，还涉及了标准库的改进，有些改进只有Python3才有，不会被反向移植进Python2.



- 好的2.x代码很像3.x的代码，That can mean many things, including using new-style classes, not using ancient deprecated arcane incantations of print, using lazy iterators where available, etc.



英文部分先存着，留着以后检验



\#\#\#\# · 接着阅读Python创始人Guido van Rossum写的，\[What’s New In Python 3.0\]\(https://docs.python.org/3/whatsnew/3.0.html\)







\#\#\#文档提供上手的起点，接着和练习结合起来，一步步从做中发现不同



- 练习：lpthw ex01、ex02



发现：



1.print这个命令被print\(\)函数代替，另，一开始用的括号是中文输入法的括号，但这个在terminal里面是不被识别的



2.用""和''都一样，没有区别，\#写评论的用法也没有区别



3.Python2连\#后面都不可以写中文，不能被ASCII码识别，但Python3 \#后面可以写简体中文、繁体中文、日文，可是print出来就会变成乱码，法文的特殊字符也print不出来



- 练习：lpthw ex03、ex04



发现：



1.如果不把像是100 - 25 \* 3 % 4这样的计算公式用\(\)括起来，在Terminal里面是显示不出来的，但不会报错。另外试了一下不在文字外面加""能不能print，结果不行，但是数字、公式外面就不需要加""



2.原本在Python2里面需要加floating point,才能显示不能整除的数字在小数点之后的计算结果，但在python3里，默认的除法计算结果就是显示小数点之后的,而且即使除出来是整数，也会显示小数点。



有一个疑问是，为什么ex03里面：print \("Hens", 25 + 30 / 6\)，



print \("Roosters", 100 - 25 \* 3 % 4\)



两行代码第一行计算显示小数点之后的结果，而第二个没有



只有除法会自动生成小数点，其余算式如果没有加上floating point，就不会显示小数点



尝试改写ex03最后一行的代码为 print \("Is it less or equal?", None &lt;= -2\)，或者print \("Is it less or equal?", '' &lt;= -2\)

None（注意N要大写，小写会被认为是一个变量）、''这样无意义的字符不会被python3读取，结果会显示TypeError，而不是判断 对错的False/True







- 练习：lpthw ex05、ex06、ex07、ex08、ex09、ex10



发现：



1.%s 和 %d要被涵括在print\(\)这个函数的括号里面才能显示出来



2.ex07，原先print一行太长的代码，在末尾加逗号可以不分行，但是加了\(\)之后，末尾加不加逗号都一样



- 练习：lpthw ex11、ex12、ex13、ex14、ex15



发现：



raw\_input\(\)函数被改成input\(\)函数了







\#\#\#总结:



1. Print 指令被Print\(\)函数替代



2. “\#” 后面可以写中文、日文一类的非ASCII码



3. 除法结果默认为有小数点，不需要额外添加Floating Point



4. &lt;,&gt;这类表比较的代码中，出现了无意义的操作，会被认为是TypeError，而不会出现True/False的陈述



5. raw\_input\(\)改成了input\(\)







