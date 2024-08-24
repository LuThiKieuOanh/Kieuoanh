# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:33:01 2024

@author: KieuOanh
"""

N=int(input("Nhập số nguyên dương có 2 chữ số:"))
if 10<=N<=99:
    Hangchuc=N//10
    Hangdonvi=N%10
    Tongchuso=Hangchuc+Hangdonvi
    print("Tổng các chữ số của N là:",Tongchuso)

