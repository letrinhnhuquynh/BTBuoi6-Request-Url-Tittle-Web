import requests
from bs4 import BeautifulSoup
import lxml
import os
import io
import re

from test_class import *

for page_number in range(1,12):

    url = f'https://nghiahsgs.com/page/{page_number}/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    titles = soup.find_all('h2', class_='entry-title') # Lấy Tittle
    links = [link.find('a').attrs["href"] for link in titles] #Lấy link

    for x in links:
        #print(x)
     write_link = File_Interact('Link.txt') #Tạo File
     write_link.write_file_line(x) #Viết link vào txt

    #print(links)
    for title in titles:
     #print(title.text)
     write = File_Interact('Ten_BV.txt') #Tạo File
     ndung_line= title.text
     write.write_file_line(ndung_line) #Viết Tittle


File_excel1 = File_Excel('BTExcel.xlsx')

ds1 = File_Interact("Link.txt")
ds1.read_file_list()

ds2 = File_Interact('Ten_BV.txt')
ds2.read_file_list()


file_path = 'BTExcel.xlsx'
sheetname = 'Sheet1'

File_excel1.update_cell(sheetname, 'A1', 'Url')
File_excel1.update_cell(sheetname, 'B1', 'Tittle')

for i in range(0, len(ds1)):
    Url = ds1[i]
    Title = ds2[i]
    cell_name = 'A%s' % (i + 2)
    File_excel1.update_cell(sheetname, cell_name, Url)
    cell_name = 'B%s' % (i + 2)
    File_excel1.update_cell(sheetname, cell_name, Title)




