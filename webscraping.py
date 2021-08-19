import requests
import bs4

def get_html_data(url):
    data=requests.get(url)
    return data

def get_covid_data():
    url="https://www.worldometers.info/coronavirus/"
    html_data=get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div =bs.find("div",class_="content-inner").find_all("div",id="maincounter-wrap")
    all_data=""

    for block in info_div:
        text = block.find("h1",class_=None).get_text()
        count= block.find("span",class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"
    print(all_data)
    return all_data

get_covid_data()