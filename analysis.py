import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/imdb_top250_20250922.csv')

# 시각화 전처리
df['Year'] = df['Year'].astype(int) # 정수로 변환
df['Rating'] = df['Rating'].astype(float)
idx = df.groupby('Year')['Rating'].idxmax() # 최고 평점 영화 인덱스
top_rating_movies = df.loc[idx].sort_values(by='Year', ascending=False).head(10)
top_rating_movies['Y_Label'] = top_rating_movies['Title'] + ' - ' + top_rating_movies['Year'].astype(str) 
print(top_rating_movies)

# 시각화
plt.figure(figsize=(16, 6)) # 가로, 세로 크기 그래프 생성
plt.barh(top_rating_movies['Y_Label'], top_rating_movies['Rating'], color='lightgreen')
plt.title('Top10 Movie Ratings') # 그래프 제목
plt.xlabel('Rating')
plt.gca().invert_yaxis() # Y축 역순
plt.tight_layout()

# 저장
plt.savefig('plots/Top10 Movie Ratings.png')
plt.show() # 창 띄우기