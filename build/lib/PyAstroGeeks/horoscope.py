import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_today_Horoscope(zodiac_sign):
    data = requests.get('https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/' + zodiac_sign)
    htmlcont = data.content

    soup = BeautifulSoup(htmlcont, 'html.parser')
    para = soup.find('p', class_='margin-top-xs-0').get_text()
    pprint(para.strip())

def get_tomorrow_Horoscope(zodiac_sign):
    data = requests.get('https://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/' + zodiac_sign)
    htmlcont = data.content

    soup = BeautifulSoup(htmlcont, 'html.parser')
    para = soup.find('p', class_='margin-top-xs-0').get_text()
    pprint(para.strip())

def get_yesterday_Horoscope(zodiac_sign):
    data = requests.get('https://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/' + zodiac_sign)
    htmlcont = data.content

    soup = BeautifulSoup(htmlcont, 'html.parser')
    para = soup.find('p', class_='margin-top-xs-0').get_text()
    pprint(para.strip())

def get_weekly_Horoscope(zodiac_sign):
    data = requests.get('https://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/' + zodiac_sign)
    htmlcont = data.content

    soup = BeautifulSoup(htmlcont, 'html.parser')
    para = soup.find('p', class_='margin-top-xs-0').get_text()
    pprint(para.strip())

def get_monthly_Horoscope(zodiac_sign):
    data = requests.get('https://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/' + zodiac_sign)
    htmlcont = data.content

    soup = BeautifulSoup(htmlcont, 'html.parser')
    para = soup.find('p', class_='margin-top-xs-0').get_text()
    pprint(para.strip())

def get_yearly_Horoscope(zodiac_sign):
    data = requests.get('https://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/' + zodiac_sign)
    htmlcont = data.content

    soup = BeautifulSoup(htmlcont, 'html.parser')
    para = soup.find('p', class_='margin-top-xs-0').get_text()
    pprint(para.strip())
