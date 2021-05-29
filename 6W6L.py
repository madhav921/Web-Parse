import requests as req
from bs4 import BeautifulSoup
import csv as writer
fields = ['Name','Organization','Project']
filename = "gsoc2021.csv"
with open(filename, 'w', newline="") as csvfile:
        csvwriter = writer.writer(csvfile,quoting=writer.QUOTE_ALL)
        csvwriter.writerow(fields)
page_no = 1
pageSize=100
while(True):
    data = req.get("https://summerofcode.withgoogle.com/api/program/current/project/?page="+str(page_no)+"&page_size="+str(pageSize))
    for i in data.json()["results"]:
        try:
            with open(filename, 'a', newline="") as csvfile:
                row = [i["student"]["display_name"],i["organization"]["name"],i["title"]]
                csvwriter = writer.writer(csvfile,quoting=writer.QUOTE_ALL)
                csvwriter.writerow(row)
        except:
            pass
    if(page_no*pageSize > data.json()["count"]):
        break
    page_no+=1