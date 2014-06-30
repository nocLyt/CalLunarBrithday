CalLunarBrithday
================

一个 Python 小程序。根据阳历阴历生日，查询今年过生日的阳历日期。 

声明
----------------
引用了 [pyzh](http://code.google.com/p/pyzh) 项目。  

执行
----------------
直接运行 `python ex.py`  
  
程序需要输入文件 `birth_cin.txt`  

输入
---------------- 
生日储存在 `birth_cin.txt` 里面，`csv`文件格式：

1. 每人信息占一行  
2. 从左往右分别为 姓名、阴历？（阴历/阳历=1/0）、年、月、日  
3. 用逗号隔开  

示例  

    李天祎,1,1993,6,17  
    李悦,0,1993,5,6  
    李忠坤,1,1993,10,5  
    李法魁,1,1966,9,8  
    曹晔,1,1966,11,8  

输出
----------------
转换成今年过生日的阳历日期存储到 `birth_cout.txt` 里面，格式与输入文件 `birth_cin.txt` 相同。
  
示例  

    李天祎,1,2014,7,13  
    李悦,0,2014,5,6  
    李忠坤,1,2014,11,26  
    李法魁,1,2014,10,1  
    曹晔,1,2014,12,29  

