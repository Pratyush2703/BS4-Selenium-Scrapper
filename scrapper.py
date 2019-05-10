import urllib.request
import ssl
import xlwt
import sys
ssl._create_default_https_context = ssl._create_unverified_context
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
opener = AppURLopener()
#url = sys.argv[1]
#print (url)
#response = opener.open(url)

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
response = opener.open('https://www.tripadvisor.com.sg/Hotel_Review-g294265-d306143-Reviews-or5-The_Elizabeth_Hotel_by_Far_East_Hospitality-Singapore.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(response, "html.parser")

#for div in soup.find_all("span", {'class':'blckarw'}): 
#    div.decompose()

#for div in soup.find_all("script"): 
#    div.decompose()    
    
print (soup.prettify())
input("Press Enter to continue...")
#------------------------------------------------------------------
"""
right_table=soup.find_all('span', class_='jcn')
i = 0;
for row in right_table:
    for link in row.find_all('a'):
        fulllink = link.get ('title')
        #print (fulllink)
        ws.write(i, 0, fulllink,)
        i+=1
input("Press Enter to continue...")
#------------------------------------------------------------------
right_table=soup.find_all('p', class_='contact-info')
i = 0;
for row in right_table:
    for link in row.find_all('a'):
        #fulllink = link.a.string
    #    print (link.string)
        ws.write(i, 1, link.string)
        i+=1
input("Press Enter to continue...")
#------------------------------------------------------------------

right_table=soup.find_all('span', class_='mrehover dn')
i = 0;
for row in right_table:
    #print (row.contents[1].strip())
    ws.write(i, 2, row.contents[1].strip())
    i+=1


input("Press Enter to continue...")
#------------------------------------------------------------------

"""
wb.save('example.xls')
input("Press Enter to continue...")
