import requests
import os

from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup
from selenium import webdriver
from .views import RefreshMovieList, GetNewestMovie


def setDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    # return webdriver.Chrome(executable_path="D:\GitHub\moviephRestfullApi\movieph\moviephApi\chromedriver.exe",
    #                         options=chrome_options)


def getNewestMovie():
    get_newmovie = GetNewestMovie()
    # r = requests.get('http://127.0.0.1:8000/newest_movie/', headers={'accept': 'application/json'})
    print("checking newest movie")
    if get_newmovie.get(requests).status_code == 204:
        return 'empty'
    else:
        return get_newmovie.get(requests).data['url']


def startSpider():
    driver = setDriver()
    driver.get('https://pahe.ph/')  # Accessing Web
    html = driver.page_source  # Get HTML
    soup = BeautifulSoup(html, 'html.parser')
    cat_box = soup.find("div", {"class": "cat-box-content"})

    movie_container = []
    for movie in reversed(cat_box.find_all('div', {'class': 'post-thumbnail'})):
        movie_container.append(movie)

    if movie_container[-1].a['href'] == getNewestMovie():
        print("list already up to date")
    else:
        items = []
        for movie in movie_container:
            original_title = movie.a['original-title'].split("(", 1)
            title = original_title[0]
            item = {
                'title': title,
                'url': movie.a['href'],
                'image': movie.img['src']
            }
            print('added: ', item['title'])

            # requests.post('http://127.0.0.1:8000/refresh_movie/', data=item)
            refresh_movie = RefreshMovieList()
            refresh_movie.post(item)

            items.append(item)


def startScheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(startSpider, 'interval', hours=6)
    scheduler.start()
