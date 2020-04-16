import requests
import xlsxwriter 
from bs4 import BeautifulSoup

#Create the csv sheet for the reasult
workbook = xlsxwriter.Workbook('JobExport.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

#Target website and target information
print("Start scrappting data")
URL = 'http://pythonjobs.github.io/'
page = requests.get(URL)
pageInfo = BeautifulSoup(page.content,'html.parser')
JobLists = pageInfo.find_all('div',class_='job')
headers = ['Job Title','Job location', 'Job info', 'Apply Link', 'More Info']

for headers in headers :
    worksheet.write(row,column,headers)
    column+=1
column=0
row+=1

#Sorting the data
for job in JobLists : 
    title = job.find('h1')
    applyLink = title.find('a')['href']
    infoLink = job.find('a',class_='go_button')['href']
    jobInfo = job.find('span',class_='info')
    jobDetail = job.find('p',class_='detail')
    worksheet.write(row, column, title.text.strip())
    column+=1
    worksheet.write(row, column, jobInfo.text)
    column+=1
    worksheet.write(row, column, jobDetail.text)
    column+=1
    worksheet.write(row, column, applyLink)
    column+=1
    worksheet.write(row, column, infoLink)
    column = 0
    row+=1
workbook.close() 
print("The scraping process is done")
