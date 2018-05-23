from tkinter import *
from PIL import ImageTk, Image
import os
import pymysql 
# import time
import matplotlib.pyplot as plt
import time, sys, threading, datetime, shutil
#import cv2 as cvx
import numpy as np
import matplotlib.pyplot as plt


def gps():
    db = pymysql.connect("localhost","root","","map")
    print(db)
    cursor = db.cursor()
#retrive1 = "Select Longitude from my_table;"
    retrive = "Select Latitude1,Longitude1,Latitude2,Longitude2,Latitude3,Longitude3,Speed from impk;"
#executing the quires
    cursor.execute(retrive)
#cursor.execute(retrive1)
    rows = cursor.fetchmany(90000)
# print(type(rows))
#rows1 = cursor.fetchmany(90000)
    for row in rows:
        cursor.execute(retrive)
        lats1 = float(row[0])
        longs1 = float(row[1])
        lats2 = float(row[2])
        longs2 = float(row[3])
        lats3 = float(row[4])
        longs3 = float(row[5])
#     x.append(lats)
#     y.append(longs)
    
#     dic = {'lat':lats,'log':longs}
#     dic.append(dic)
#     print(dic)
#     speed = row[2]
#     cumu = row[3]
#     dist = row[4]
#     time = row[5]
#     n = n+1
        print(lats1,longs1,lats2,longs2,lats3,longs3)
        with open("position.kml","w") as pos:
            pos.write( """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
<Style id="icon">
    <IconStyle>
        <Icon>
          <href>redBall.png</href>
        </Icon>
    </IconStyle>
 </Style>
<Placemark>
<name>yuvi</name>
    <styleUrl>#icon</styleUrl>    
    <Point>
        <coordinates>%s,%s,0</coordinates>
    </Point>
</Placemark>
<Style id="icon2">
    <IconStyle>
        <Icon>
          <href>greenBall.png</href>
        </Icon>
    </IconStyle>
 </Style>
<Placemark>
<name>Sachin</name>
    <styleUrl>#icon2</styleUrl>    
    <Point>
        <coordinates>%s,%s,0</coordinates>
    </Point>
</Placemark>
<Style id="icon3">
    <IconStyle>
        <Icon>
          <href>yellowBall.png</href>
        </Icon>
    </IconStyle>
 </Style>
<Placemark>
<name>Dhoni</name>
    <styleUrl>#icon3</styleUrl>  
    <Point>
        <coordinates>%s,%s,0</coordinates>
    </Point>
</Placemark>
</Document>
</kml>"""%(longs1,lats1,longs2,lats2,longs3,lats3))
#"""<kml xmlns="http://www.opengis.net/kml/2.2"
#        xmlns:gx="http://www.google.com/kml/ext/2.2">
#        <Placemark>
#            <name>gps</name>
#            <description>hello world</description>
#            <Point>
#                <coordinates>%s,%s,0</coordinates>
#            </Point>
#        </Placemark></kml>"""%(longs, lats))
   
    
    #dist = float(row[2])
    
    #cv2.Point(img,(0,0),(150,150),(255,0,0),15)
    #print(dist)
    time.sleep(1)
#commiting the connection then closing it.
    db.commit()
    db.close()


def raise_frame(frame):
    if(frame==f1):
        
        frame.tkraise()
    if(frame==f2):
        panel = Label(f2, image = img3)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        frame.tkraise()
    if(frame==f3):
        panel2 = Label(f3, image = img2)
        panel2.pack(side = "bottom", fill = "both", expand = "yes")
        frame.tkraise()
    if(frame==f4):
        gps()
        frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
# img4 = ImageTk.PhotoImage(Image.open("map4.png"))
img5 = ImageTk.PhotoImage(Image.open("map5.png"))

img3 = ImageTk.PhotoImage(Image.open("map3.png"))
img2 = ImageTk.PhotoImage(Image.open("map2.png"))
img1 = ImageTk.PhotoImage(Image.open("map1.png"))

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')
Label(f1, text='START').pack()
Button(f1, text='GRAPH ONE', command=lambda:raise_frame(f2)).pack()
Button(f1, text='GRAPH TWO', command=lambda:raise_frame(f3)).pack()
Button(f1, text='GOOGLE EARTH', command=lambda:raise_frame(f4)).pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='GRAPH TWO', command=lambda:raise_frame(f3)).pack()
Button(f2, text='Go to START', command=lambda:raise_frame(f1)).pack()
Button(f2, text='GOOGLE EARTH', command=lambda:raise_frame(f4)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='GOOGLE EARTH', command=lambda:raise_frame(f4)).pack(side='left')
Button(f3, text='GRAPH ONE', command=lambda:raise_frame(f2)).pack(side='left')
Button(f3, text='Go to START', command=lambda:raise_frame(f3)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to START', command=lambda:raise_frame(f1)).pack()
Button(f4, text='Goto to frame 2', command=lambda:raise_frame(f2)).pack()
Button(f4, text='Goto to frame 3', command=lambda:raise_frame(f3)).pack()
raise_frame(f1)
root.mainloop()

