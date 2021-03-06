# coding=utf-8
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

'''
系列(Series)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维标记数组。轴标签统称为索引.
   Pandas系列可以使用以下构造函数创建
   pandas.Series( data, index, dtype, copy)
       data  数据采取各种形式，如：ndarray，list，constants
       index 索引值必须是唯一的和散列的，与数据的长度相同。 默认np.arange(n)如果没有索引被传递。
       dtype dtype用于数据类型。如果没有，将推断数据类型
       copy  复制数据，默认为false。
'''



print("==========================================================")
print("创建一个空的系列");
print("==========================================================")
#创建一个基本系列是一个空系列
s = pd.Series();
print (s);


print("==========================================================")
print("从ndarray创建一个系列");
print("==========================================================")
#如果数据是ndarray，则传递的索引必须具有相同的长度。 如果没有传递索引值，那么默认的索引将是范围(n)，其中n是数组长度
data = np.array(['a','b', 'c', 'd', 'e', 'f']);
s = pd.Series(data);
print (s);

#在这里传递了索引值
s = pd.Series(data, index=[100,101,102,105,107,109]);
print (s);


print("==========================================================")
print("从字典中创建一个系列");
print("==========================================================")
#字典(dict)可以作为输入传递，如果没有指定索引，则按排序顺序取得字典键以构造索引。 如果传递了索引，索引中与标签对应的数据中的值将被拉出。
data = {"a":1.0, "b":2.0,"c":3.0}
s = pd.Series(data);
print (s);

#字典键用于构建索引
s = pd.Series(data,index=["b",'c','d', 'a']);
print (s)
s = pd.Series(data,index=["A",'B','C']);
print (s)


print("==========================================================")
print("从标量创建一个系列");
print("==========================================================")

s = pd.Series(5,index=[0,1,2,3])
print (s);


print("==========================================================")
print("从具有位置的系列中访问数据");
print("==========================================================")

s =pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
#检索第一个元素
print (s[0])

#从开始检索三个元素
print (s[:3]);

#检索最后三个元素
print (s[-3:]);


print("==========================================================")
print("使用标签检索数据(索引)");
print("==========================================================")
#检索指定标签
print (s['a']);

#检索指定多个标签
print (s[['a','b','c']]);

#检索不存在标签值
print (s['f']);