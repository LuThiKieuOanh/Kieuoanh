# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:01:45 2024

@author: KieuOanh
"""

d= float(input("Nhập quãng đường đã đi(km):"))
if d<=1:
    print("giá là 20k")
elif d>1 and d<= 4:
    print("giá là:", d*13000)
elif d>=4 and d<=8:
    print("giá là:", (3*13000)+ (d-3)*12000)
else:
    print("giá là:", 39000+60000+(d-8)*10000)
    d= 39000+60000+(d-8)*1000
if d>=100000:
    print("giá là sau khi giảm:", d*0.92)