#-*- codeing = utf-8 -*-
#@Time: 2022/8/27 上午 01:38
#@aUTHOR: 德順
#@file: gerFileJavBus.py

import os
import sys
import pathlib
import webbrowser

import pyperclip as pc

# from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# vfullname = sys.argv[1]
vfullname = 'y:\\test\\MDTM-527.mp4'
# print (vfullname)
# print ('path',pathlib.Path(sys.argv[1]))
basename =os.path.basename(vfullname)

# print('basename',basename)
name2= os.path.splitext(basename)[0]

if name2[-1:] == 'C':
    name2 = name2[:-1]
elif  name2[-3:] == '_2K':
    name2 = name2[:-3]

# print ('name2',name2)
# pc.copy(name2)
searchpath ='https://www.javbus.com/'+ name2
import requests
from tkinter import messagebox
from bs4 import BeautifulSoup
resp = requests.get(searchpath)
if resp.status_code==200:
    bs = BeautifulSoup(resp.text,'html.parser')
    vs = bs.find_all('div','star-name')
    # messagebox.showinfo(v.text,v.text)
    if len(vs)==1:
        v = vs[0]
        print (v.text)
        print (basename)
        print (os.path.abspath(vfullname))
        print ()
        if not v.text in vfullname:
            newpath = os.path.dirname(vfullname)+'\\' + v.text+"\\"
            if not os.path.exists(newpath):
                os.mkdir(newpath)
            os.rename(vfullname,newpath+basename)
    else:
        raise Exception('超過一位明星:'+str(len(vs)))
        v = vs[0]
        if not v.text in vfullname:
            print("\\")
            print (v.text ,"-",vfullname)
            newpath = os.path.dirname(vfullname) + "\\" + v.text + str(len(vs)) + "\\"

            print(newpath)
            if not os.path.exists(newpath):
                os.mkdir(newpath)
            os.rename(vfullname,newpath+basename)