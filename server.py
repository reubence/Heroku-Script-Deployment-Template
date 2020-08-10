import gspread
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googlesearch import search

df = pd.read_csv('list of companies.csv', header=None)
names = df[0].tolist()
names = names[:1601]
print("START")

gc = gspread.service_account(filename='client-access.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1QtYJW0jp0XAI-hSdfUwc0CaHKht21Ydy3FnUfd9wY8E/edit?usp=sharing')
# dataframe = pd.read_csv('list of companies.csv')

final = []
names = names[301:601]
for name in names:
    print(name)
    temp = [name]
    
    try:
        url = next(search(name + 'zauba corp', tld="co.in", num=1, stop=1, pause=2))
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
    except:
        continue
    
    try:
        df_zauba = pd.read_html(url)
        maintable = df_zauba[0]
        maintable.columns = ['1', '2']
        temp.extend([maintable['2'][2], maintable['2'][6], maintable['2'][7], maintable['2'][9]])
    except:
        temp.extend(['', '', '', ''])
    
    try:
        email = ''
        for link in soup.find_all("p"):
            a = link.text
            if 'Email ID' in a:
                b = a.split()
                email = b[-1]
                break
        temp.extend([email])
    except:
        temp.append('')
    
    try:
        link = next(search(name, tld="co.in", num=1, stop=1, pause=2))
        temp.append(link)
    except:
        temp.append('')
    
    try:
        directors = df_zauba[7]
        directors.columns = ['1', '2', '3', '4', '5']
        toplvl = ''
        linkdinlinks = []
        for ind in directors.index:
            if directors['1'][ind].isdecimal():
                toplvl += directors['2'][ind] + '(' + directors['3'][ind] + '),'
                lurl = next(search(directors['2'][ind] + name + 'linkdin', tld="co.in", num=1, stop=1, pause=2))
                linkdinlinks.append(lurl)
        temp.append(toplvl)
    except:
        temp.append('')
        linkdinlinks = []
        
        # final.append([name, maintable['2'][2], maintable['2'][6], maintable['2'][7], maintable['2'][9],  email, link, toplvl])
    
    if len(linkdinlinks) > 5:
        temp.extend(linkdinlinks[:5])
    else:
        l = len(linkdinlinks)
        count = 5
        while count != l:
            linkdinlinks.append('')
            count -= 1
        
        temp.extend(linkdinlinks)
    final.append(temp)

dataframe = pd.DataFrame(final, columns=['Name', 'Location', 'Class', 'Date of Incorporation', 'Activity',
                                         'Email', 'Website', 'Top Level Employees', 'Linkdin Link 1',
                                         'Linkdin Link 2', 'Linkdin Link 3', 'Linkdin Link 4', 'Linkdin Link 5'])

data = {}
worksheet = sh.get_worksheet(0)

worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
print("END")
