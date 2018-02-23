import requests

def get_html(url):#,u,p):
    re= requests.get(url)#,headers=u, proxies=p)        # отримуємо html код
    print(re)
    return re.text