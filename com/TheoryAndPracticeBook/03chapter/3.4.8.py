# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 标准化欧式距离 ===============");
import numpy as np;
vec1 = np.array([1, 2, 3, 4]);
vec2 = np.array([5, 6, 7, 8]);

Vec = np.vstack([vec1, vec2]);
#方法一、根据公式求解
sk = np.var(Vec, axis=0, ddof=1);
dist1 = np.sqrt(((vec1 - vec2) ** 2 /sk).sum());
print ("标准化欧氏距离测试结果是:"+str(dist1));

#方法二、根据scipy库求解
from scipy.spatial.distance import pdist;
dist2 = pdist(Vec, 'seuclidean');
print ("标准化欧氏距离测试结果是:"+str(dist2));
