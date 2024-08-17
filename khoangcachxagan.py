# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:26:09 2024

@author: KieuOanh
"""

duongtoitruong=float(input("nhap do dai doan duong den truong(m):"))
if duongtoitruong<300:
        print("duong den truong qua gan. Thoi!Di bo")
elif duongtoitruong>1200:
    print("duong den truong qua xa. Thoi!Di xe may")
elif duongtoitruong>=300 and duongtoitruong<= 700:
    print("duong den truong khong xa. Thoi!Di xe dap")
else:
    print("khong xac dinh")
    
    