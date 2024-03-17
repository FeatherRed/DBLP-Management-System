### Data-Structure
Data-Structure Scientific Document Management
##7.科学文献管理系统
科研工作者的日常工作离不开查阅科学文献，并对其中的信息进行分析、筛选、挖掘和管理。请你为科研工作者设计一个管理系统，提高科学文献的管理效率。
目标用户：科研工作者。
数据配置：请通过以下方法下载数据文件dblp.xml.gz.
http://dblp.uni-trier.de/xml/dblp.xml.gz
   将该数据文件解压后，其中包含一个dblp.xml文件。该文件由科学文献的记录序列组成，记录的格式如下所示：
 <article mdate="2002-01-03" key="persons/Codd71a">
<author>E. F. Codd</author>
<title>Further Normalization of the Data Base Relational Model.</title>
<journal>IBM Research Report, San Jose, California</journal>
<volume>RJ909</volume>
<month>August</month>
<year>1971</year>
<cdrom>ibmTR/rj909.pdf</cdrom>
<ee>db/labs/ibm/RJ909.html</ee>gg'm'j'k'k'k'k'k'k'k'k'k
</article>
每个记录对应一篇文章，其中包含对作者，题名，发表杂志，卷号，出版时间等的详细说明。请基于该数据，设计能满足后述功能的文献管理系统。
   注：1）dblp.xml的大小超过1G，所以不要直接点击打开该文件。需要通过命令行命令’more’ 或者自行编程查看。
2） 编程过程中，不允许使用数据库系统。需要自己建立管理文献数据的数据结构。
