import gspread
import pandas as pd

from bs4 import BeautifulSoup
import pandas as pd
import requests
from googlesearch import search

df = pd.read_csv('list of companies.csv', header=None)
names = df[0].tolist()
names = names[1601:1606]
print("START")

gc = gspread.service_account(filename='client-access.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1F9e3pi0GlBY948PSauL7nRrKc8LaIX0CZVRz9klj3YU/edit?usp=sharing')
# dataframe = pd.read_csv('list of companies.csv')

final = []
for name in names:
    print(name)

    try:
        url = next(search(name + 'zauba corp', tld="co.in", num=1, stop=1, pause=2))
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        df_zauba = pd.read_html(url)
        maintable = df_zauba[0]
        maintable.columns = ['1', '2']
        directors = df_zauba[7]

        directors.columns = ['1', '2', '3', '4', '5']
        toplvl = ''
        linkdinlinks = []
        for ind in directors.index:
            if directors['1'][ind].isdecimal():
                toplvl += directors['2'][ind] + '(' + directors['3'][ind] + '),'
                lurl = next(search(directors['2'][ind] + name + 'linkdin', tld="co.in", num=1, stop=1, pause=2))
                linkdinlinks.append(lurl)
                # print(directors['3'][ind])
        email = ''
        website = ''
        for link in soup.find_all("p"):
            a = link.text

            if 'Email ID' in a:
                b = a.split()
                email = b[-1]
            if 'Website' in a:
                b = a.split(':')
                website = b[-1]

        link = next(search(name, tld="co.in", num=1, stop=1, pause=2))

        final.append(
            [name, maintable['2'][2], maintable['2'][6], maintable['2'][7], maintable['2'][9], email, link, toplvl])
        if len(linkdinlinks) > 5:
            final[-1].extend(linkdinlinks[:5])
        else:
            l = len(linkdinlinks)
            count = 5
            while count != l:
                linkdinlinks.append('')
                count -= 1

            final[-1].extend(linkdinlinks)

    except:
        pass

dataframe = pd.DataFrame(final, columns=['Name', 'Location', 'Class', 'Date of Incorporation', 'Activity',
                                       'Email', 'Website', 'Top Level Employees', 'Linkdin Link 1',
                                       'Linkdin Link 2', 'Linkdin Link 3', 'Linkdin Link 4', 'Linkdin Link 5'])

data = {}
worksheet = sh.get_worksheet(0)

worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
print("END")