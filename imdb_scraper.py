import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Selenium으로 Chrome 브라우저 설정
# webdriver-manager가 자동으로 드라이버를 설치하고 관리해줍니다.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.imdb.com/chart/top/"
driver.get(url)
# headers = {'User-Agent': 'Mozilla/5.0'}
# 페이지의 모든 콘텐츠가 로드될 때까지 스크롤
# 현재 페이지의 높이를 가져옵니다.
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 페이지 맨 아래로 스크롤합니다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # 새 콘텐츠가 로드될 시간을 줍니다.
    time.sleep(2) # 로딩 시간에 따라 조절
    
    # 스크롤 후의 새 페이지 높이를 가져옵니다.
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # 스크롤을 끝까지 내려서 페이지 높이에 변화가 없으면 반복을 멈춥니다.
    if new_height == last_height:
        break
    last_height = new_height

# 모든 콘텐츠가 로드된 최종 페이지 소스를 가져옵니다.
html_source = driver.page_source
driver.quit() # 브라우저 종료

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html_source, 'html.parser')

# response = requests.get(url, headers = headers)
# print(f"Status Code: {response.status_code}")

# soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.select('.ipc-metadata-list-summary-item')
print(f"가져온 영화의 개수: {len(movies)}")

titles = []
years = []
ratings = []

for movie in movies:
  title = movie.select_one('.ipc-title-link-wrapper h3').text
  year = movie.select_one('.cli-title-metadata span:nth-of-type(1)').text
  rating = movie.select_one('.ipc-rating-star--rating').text
  
  titles.append(title.split(" ", 1)[1]) # 공백을 기준으로 최대 1번만 나눔
  years.append(int(year))
  ratings.append(float(rating))

df = pd.DataFrame({
   'Title': titles,
   'Year': years,
   'Rating': ratings
})

today = datetime.today().strftime('%Y%m%d')
df.to_csv(f'data/imdb_top250_{today}.csv', index=False)