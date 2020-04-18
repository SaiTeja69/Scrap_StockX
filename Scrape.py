import requests
from bs4 import BeautifulSoup
url = 'https://stockx.com/handbags'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
response = requests.get(url, headers=headers)
#print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')
def retrieve_all_products():
    return (soup.find_all('div', class_='tile browse-tile'))
list_prod=retrieve_all_products()
url_2='https://stockx.com'
def link_send():
    x=[]
    prod=[]
    for i in list_prod:
        link_prod=i.find("a")
        prod.append(link_prod.get_text())
        x.append(url_2+link_prod.get('href'))
    return x,prod
links,products=link_send()
def all_max_min():
    a=[]
    b=[]
    r=[]
    d=[]
    last=[]
    for i in links:
        response = requests.get(i, headers=headers)
        temp_var=BeautifulSoup(response.content, 'html.parser')
        var_2=temp_var.find_all('div', class_='en-us stat-value stat-small')
        y=temp_var.find_all('p',class_='value')
        z=temp_var.find_all('ul',class_='breadcrumb')
        zz=z[0].find_all('li')
        las_1=temp_var.find_all('div',class_='gauge-container')
        last.append([las_1[0].get_text(),las_1[1].get_text(),las_1[2].get_text()])
        d.append(zz[2].get_text())
        try:
            r.append(y[5].get_text())
        except:
            r.append(0)
        a.append(var_2[0].get_text())
        b.append(var_2[1].get_text())
    return a,b,r,d,last
lowest,highest,retail,brand,stats=all_max_min()

final=[]
for i in range(40):
    final.append([lowest[i],highest[i],retail[i],brand[i],stats[i]])
    print(products[i],lowest[i],highest[i],retail[i],brand[i],stats[i])
