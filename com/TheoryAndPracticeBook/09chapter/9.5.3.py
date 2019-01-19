# -*- coding: utf-8 -*-
# !/usr/bin/pythonrrrr
import  jieba;
print ("=== 全模式 ===");
seg_list = jieba.cut("我是王小二来自技术社区", cut_all=True);
print ("Full Model:"+"/".join(seg_list));


print ("=== 精确模式 ===");
seg_list = jieba.cut("我是王小二来自技术社区", cut_all=False);
print ("Default Model:"+"/".join(seg_list));

print ("=== 默认模式 ===");
seg_list = jieba.cut("我是王小二来自技术社区");
print ("Default Model:"+"/".join(seg_list));

print ("=== 繁体字处理 ===");
str = '''燕子去了，有再來的時候；楊柳枯了，有再青的時候；桃花謝了，有再開的時候。但是，聰明的，你告訴我，我們的日子為什麼一去不複返呢？——是有人偷了他們罷：那是誰？又藏在何處呢？是他們自己逃走了罷：現在又到了哪裏呢？ 我不知道他們給了我多少日子；但我的手確乎是漸漸空虛了。在默默裏算著，八千多日子已經從我手中溜去；像針尖上一滴水滴在大海裏，我的日子滴在時間的流裏，沒有聲音，也沒有影子。我不禁頭涔涔而淚潸潸了。 去的盡管去了，來的盡管來著；去來的中間，又怎樣地匆匆呢？早上我起來的時候，小屋裏射進兩三方斜斜的太陽。太陽他有腳啊，輕輕悄悄地挪移了；我也茫茫然跟著旋轉。于是——洗手的時候，日子從水盆裏過去；吃飯的時候，日子從飯碗裏過去；默默時，便從凝然的雙眼前過去。我覺察他去的匆匆了，伸出手遮挽時，他又從遮挽著的手邊過去，天黑時，我躺在床上，他便伶伶俐俐地從我身上跨過，從我腳邊飛去了。等我睜開眼和太陽再見，這算又溜走了一日。我掩著面歎息。但是新來的日子的影兒又開始在歎息裏閃過了。 在逃去如飛的日子裏，在千門萬戶的世界裏的我能做些什麼呢？只有徘徊罷了，只有匆匆罷了；在八千多日的匆匆裏，除徘徊外，又剩些什麼呢？過去的日子如輕煙，被微風吹散了，如薄霧，被初陽蒸融了；我留著些什麼痕跡呢？我何曾留著像游絲樣的痕跡呢？我赤裸裸來到這世界，轉眼間也將赤裸裸的回去罷？但不能平的，為什麼偏要白白走這一遭啊？ 你聰明的，告訴我，我們的日子為什麼一去不複返呢？'''
str = jieba.cut(str);
print ("/".join(str));

