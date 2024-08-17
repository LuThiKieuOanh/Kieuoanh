# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:23:06 2024

@author: KieuOanh
"""

a= float(input("nhap a:"))
b= float(input("nhap b:"))
if a==0 and b!=0:
    print("phuong trinh vo nghiem")
elif a==0 and b==0:
    print("phuong trinh co vo so nghiem")
else:
    print("nghiem cua phuong trinh la:", -b/a)
    