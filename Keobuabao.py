# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:56:40 2024

@author: KieuOanh
"""

player=float(input("Người chọn(1.Kéo, 2.Búa, 3.Bao:)"))
from random import randint 
com=randint(1,3)
if com==1:
    print("Máy chọn Kéo")
elif com==2:
    print("Máy chọn Búa")
elif com==3:
    print("Máy chọn Bao")
if com==player:
    print("Kết quả Hòa")
elif com==1 and player==2:
    print("NgườiThắng")
elif com==1 and player==3:
    print("Người Thua")
elif com==2 and player==1:
    print("Người Thua")
elif com==2 and player==3:
    print("Người Thắng")
elif com==3 and player==1:
    print("Người Thắng")
elif com==3 and player==2:
    print("Người Thua")
else:
    print("Không hợp lệ")


