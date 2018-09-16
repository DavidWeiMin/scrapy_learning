import requests
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error')
        return ''

def fillHeader(header,html):
    soup = bs4.BeautifulSoup(html,'html.parser')
    [header.append((th.string)) for th in soup.find('thead').find_all('th')[:4]]
    [header.append((option.string)) for option in soup.find('thead').find('select').children]
    while '\n' in header:
        header.remove('\n')

def fillUnivList(table,html,num=10000):
    soup = bs4.BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if len(table) == num:
            break
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            tds = [td.string for td in tds]
            table.append(tds)

def saveData(year,header,table):
    table.insert(0,header)
    with open(str(year) + 'rankings.csv','w',encoding='utf-8-sig') as f:
        for i in table:
            for j in i:
                if j:
                    f.write(j)
                else:
                    f.write('——')
                f.write(',')
            f.write('\n')

def main():
    years = range(2016,2019)
    for year in years:
        header = []
        uinfo = []
        url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming' + str(year) + '.html'
        html = getHTMLText(url)
        fillHeader(header,html)
        fillUnivList(uinfo,html)
        saveData(year,header,uinfo)

if __name__=='__main__':
    main()