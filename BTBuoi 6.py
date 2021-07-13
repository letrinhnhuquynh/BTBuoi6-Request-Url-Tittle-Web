import requests
from bs4 import BeautifulSoup
import lxml
import os
import io
import re
from test_class import *

link_total=[]
title_total=[]
page_number = 1

while True:
    url = f'https://nghiahsgs.com/page/{page_number}/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    titles = soup.find_all('h2', class_='entry-title') # Lấy Tittle
    links = [link.find('a').attrs["href"] for link in titles] #Lấy link
    if(len(titles)==0): #Nếu title rỗng thì thoát
        break
    else: #Nếu title khác rỗng thì chạy tiếp tục
        link_total += links
        title_total += titles
        page_number +=1

for x in link_total:
        #print(x)
     write_link = File_Interact('Link.txt') #Tạo File
     write_link.write_file_line(x) #Viết link vào txt

for title in title_total:
     #print(title.text)
     write = File_Interact('Ten_BV.txt') #Tạo File'''
     ndung_line= title.text
     write.write_file_line(ndung_line) #Viết Tittle

File_excel1 = File_Excel('BTExcel.xlsx')
ds1 = write_link.read_file_list()
ds2 = write.read_file_list()
sheetname = 'Sheet1'

File_excel1.update_cell(sheetname, 'A1','Url')
File_excel1.update_cell(sheetname, 'B1','Title')

for i in range(0, len(ds1)):
    Url = ds1[i]
    Title = ds2[i]
    cell_name = 'A%s' % (i + 2)
    File_excel1.update_cell(sheetname, cell_name, Url)
    cell_name = 'B%s' % (i + 2)
    File_excel1.update_cell(sheetname, cell_name, Title)




