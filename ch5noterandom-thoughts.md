老脸皮厚的Bravo再次没完成任务...先来占坑，能输出一点是一点。

编程需要同时处理语言和逻辑的问题，最好是一次解决一个。在前面数周，我一直在分辨编程使用的术语上砸下了很多时间，对于阅读中文文档心存负罪感，不敢找来读，基本是在半梦半醒之间把代码写掉的，其中有许多模模糊糊没有彻底弄懂的地方。因为上周发现资优生其实也阅读了好多中文资料，这周就改换了做作业的策略，把卡包的框架和其中的关键概念写下来，先去读廖雪峰的博客，锚定了一些概念的中文定义，有了基础的框架在脑子里，再回头看卡包里的链接，两边的文档互为补充解释疏漏的地方。  
英文文档又不是看不懂，只是在某一个词的定义上纠结，个把小时被吞掉实在不值得，最重要的是资料的质量。  
这次尝试走了桥，没有用头去撞石头。  
[![](https://cloud.githubusercontent.com/assets/23642700/23107661/04122256-f73c-11e6-85c7-6b345c1c3f3d.jpg "default")](https://cloud.githubusercontent.com/assets/23642700/23107661/04122256-f73c-11e6-85c7-6b345c1c3f3d.jpg)

* 为什么要用数据库，而不是文件？  
  程序运行的时候，数据全保存在内存里，而有时候数据的大小远远超过了内存，所以我们需要数据库进行数据的存储和查询，并让我们能够通过条件快速检索。

* 数据库和数据库管理软件的关系是什么？  
  数据库是一个有组织的数据集合，数据库管理软件\(database management system, 缩写DBMS\)是一种软件，用来实现和用户、其他应用、数据本身之间的交互，可以抓取、分析数据。比较著名的DBMS包括： MySQL、PostgreSQL、MongoDB、Microsoft SQL Server、Oracle等等。自80年代起，所有流行的数据库管理系统都以关系模型为基础，该类不同的数据库管理软件之间，通过统一的SQL传输数据。有时，数据库管理系统也被认为是数据库。

* 什么是关系数据库？NoSQL呢？

  * 关系数据库是数据库的一种，是我们现在广泛使用的数据库类型。关系数据库的结构是一个层层嵌套展开的模型，但是基于表\(Table\)的形式，使用SQL作为标准，进行不同数据库之间的沟通。因为关系型数据库没办法规模化，所以适用于使用数据库的用户很少的状况。
  * NoSQL是不使用SQL标准的非关系型数据库，适合处理大量数据和应用于实时网页应用。

* SQL\(Structured Query Language\)  
  SQL是在关系型数据库里面使用的语言，语法格式为：  
  SELECT \* FROM xx WHERE yy = 'zz'

* 哪种数据库受欢迎？  
  根据[DB-Engines Ranking](http://db-engines.com/en/ranking)网站排名，截止至2016.02.16，最受欢迎的前十名数据库中有7个是关系型数据库，其中Oracle,Microsoft SQL Server, PostgreSQL, DB2, Microsoft Access, 是商业数据库系统，MySQL, SQLite是开放源代码数据库系统

* SQLite  
  SQLite是世界上使用最多的轻型关系数据库，是一种嵌入式数据库，一个数据库就是一个文件。因为体积很小，经常被集成到各种应用程序中，在移动端非常受欢迎。  
  Python中内置了sqlite3模块，直接调用就好。  
  数据库里面会包含多个表，表和表之间通过外键关联。要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。  
  示例代码：  
  import sqlite3  
  conn = sqlite3.connect\('test.db'\)  
  cursor = conn.cursor\(\)  
  cursor.execute\('create table user \(id varchar\(20\) primary key, name varchar\(20\)\)'\)  
  &lt;sqlite3.Cursor object at 0x10f8aa260&gt;  
  cursor.execute\('insert into user \(id, name\) values \('1', 'Michael'\)'\)  
  &lt;sqlite3.Cursor object at 0x10f8aa260&gt;  
  cursor.rowcount  
  1  
  cursor.close\(\)  
  conn.commit\(\)  
  conn.close\(\)

再试试查询记录：

conn = sqlite3.connect\('test.db'\)  
cursor = conn.cursor\(\)  
cursor.execute\('select \* from user where id=?', \('1',\)\)  
&lt;sqlite3.Cursor object at 0x10f8aa340&gt;  
values = cursor.fetchall\(\)  
values  
\[\('1', 'Michael'\)\]  
cursor.close\(\)  
conn.close\(\)

* CRUD  
  CRUD是SQL里最常用的四种基本操作，是creat，read，update和delete的首字母缩写。

* BGM推荐时间  
  [&lt;The Lumineers\(Deluxe Edition\)&gt; - The Lumineers](http://music.163.com/#/playlist?id=328235223)  
  美国民谣摇滚乐团，首首好听，少见地人声不影响专注，反倒能产生共振的场。



