from bs4 import BeautifulSoup as bs
from get import get_html
from save import save
from datetime import datetime
from mydate import mydate

#https://www.dobovo.com/kiev-apartments.html?sort=price&in=2018-02-23&out=2018-02-24
#class_='item__title dbv_js_apttitle dbv_js_apt_url

#enazer syte ////div class="filter-results__item-slider" .next a['href']
def pars(html,date, id):
    soup=bs(html,'lxml')
    link=soup.find_all('div', class_='item item_extend dbv_js_aptblock')

    for url in link:
        print(url['data-apt-url'])
        data={'date':date,
              'id':id,
              'url':url['data-apt-url'],}
        save(data)

    try:
        page='https://www.dobovo.com'+soup.find('a', class_='selected').find_next('a')['href']

    except(AttributeError):page=None
    return page

def pars2(html, date, id):
    soup = bs(html, 'lxml')
    link = soup.find_all('div', class_='filter-results__item-slider')

    for url in link:
        print(url.find_next('a')['href'])
        data = {'date': date,
                'id':id,
                'url': url.find_next('a')['href'], }
        save(data)

    try:
        page = 'https://oktv.ua' + soup.find('li', class_='active').find_next('li').find_next('a') ['href']

    except(AttributeError):
        page = None
    return page

def main():
    sity='kiev'
    sity2='Киев'
    id='https://www.dobovo.com/'
    id2='https://oktv.ua/'
    y = int(str(datetime.now().date()).split('-')[0])
    m = int(str(datetime.now().date()).split('-')[1])
    d = int(str(datetime.now().date()).split('-')[2])



    try:
        while True:
            now=str(datetime(y, m, d).date())
            day2=str(datetime(y,m,d+1).date())
            url = 'https://www.dobovo.com/' + sity + '-apartments.html?sort=price&in=' + now + '&out=' + day2
            print(url)
            date = now + '\n' + day2
            d+=1

            i=0

            while url!=None or i>50:
                url=pars(get_html(url),date, id)
                i+=1

            i=0
            url='https://oktv.ua/search?city='+sity2+'&order_start='+now+'&order_finish='+day2
            while url!=None or i>50:
                url=pars2(get_html(url),date, id2)
                i+=1

    except(ValueError):
        False


if __name__ == '__main__':
    main()