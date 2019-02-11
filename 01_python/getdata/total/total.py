import requests
import os
import csv
import pickle
import urllib.request

KOBIS_KEY = os.getenv('KOBIS_KEY')
result = []

Dates = ['20190113', '20190106', '20181230', '20181223', '20181216', '20181209', '20181202', '20181125', '20181118', '20181111']

for j in range(0,10):
    targetDt = Dates[j]
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={KOBIS_KEY}&targetDt={targetDt}&weekGb=0'
    data = requests.get(URL).json()
    data = data['boxOfficeResult']['weeklyBoxOfficeList']
    for i in range(0,10):
        data[i]['targetDt'] = targetDt
        movie_info = []
        if data[i]['movieNm'] not in sum(result, []):
            movie_info.append(data[i]['movieCd'])
            movie_info.append(data[i]['movieNm'])
            movie_info.append(data[i]['audiAcc'])
            movie_info.append(data[i]['targetDt'])
            movie_info.append('\n')
            result.append(movie_info)
            
            
f = open('boxoffice.csv', 'w+', encoding='utf-8')

f.write('movie_code, title, audience, recorded_at \n')

for movie in result:
    line = ", ".join(movie)
    f.write(line)

f.close()
f = open('boxoffice.csv', 'rt', encoding='utf8')
result = []
lines = f.readlines()
for line in lines:
    result.append(line.split(', '))
f.close()

fin = []
for num in range(1,len(result)):
    fin.append(result[num][0])



KOBIS_KEY = os.getenv('KOBIS_KEY')
movie = []
for i in range(0,43):
    movCd = fin[i]
    info = []
    URL= f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={KOBIS_KEY}&movieCd={movCd}'
    data = requests.get(URL).json()
    data = data["movieInfoResult"]['movieInfo']
    info.append(data['movieCd'])
    info.append(data['movieNm'])
    info.append(data['movieNmEn'])
    info.append(data['movieNmOg'])
    info.append(data['openDt'])
    info.append(data['showTm'])
    for num in range(0, len(data['genres'])):
        info.append(data['genres'][num]['genreNm'])
    for num in range(0, len(data['directors'])):
        info.append(data['directors'][num]['peopleNm'])
    info.append(data['audits'][0]['watchGradeNm'])
    for num in range(0, len(data['actors'])):
        if num <= 2:
            info.append(data['actors'][num]['peopleNm'])
    info.append('\n')
    movie.append(info)

f = open('movie.csv', 'w+', encoding='utf-8')

f.write('movie_code, movie_name_ko, movie_name_en, movie_name_og, prdt_year, genres, directors, watch_grade_nm, actor1, actor2, actor3, \n')

for info in movie:
    line = ", ".join(info)
    f.write(line)

f.close()

f = open('movie.csv', 'r',  encoding='utf8')
result = []
for line in f.readlines():
    result.append(line.split(', '))
f.close()

fin = []
for num in range(1,len(result)):
    fin.append(result[num][1])

fin = [0] + fin


client_id = os.getenv('NAVER_CLIENT_ID')
client_secret = os.getenv('NAVER_CLIENT_SECRET')

headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret 
}
data = []

for num in range(1, len(fin)):
    naver_uri = f'https://openapi.naver.com/v1/search/movie.json?query='
    res = requests.get(naver_uri + fin[num], headers = headers).json()
    res['movCd'] = result[num][0]
    data.append(res)
    
wr = []

for movie in data:
    info = []
    info.append(movie['movCd'])
    info.append(movie['items'][0]['image'])
    info.append(movie['items'][0]['link'])
    info.append(movie['items'][0]['userRating'])
    info.append('\n')
    wr.append(info)


f = open('movie_naver.csv', 'w+', encoding='utf-8')

f.write('movie_code, image, link, userrating, \n')

for info in wr:
    line = ", ".join(info)
    f.write(line)

f.close()

k = open('movie_naver.csv', 'r')
lines = k.readlines()
mvcode = []
imgURL = []
for line in lines:
    mvcode.append(line.split(', ')[0])
    imgURL.append(line.split(', ')[1])
del mvcode[0]
del imgURL[0]


for num in range(0, len(mvcode)):
    f = open(f'images/{mvcode[num]}.jpg', 'wb+')
    urllib.request.urlretrieve(imgURL[num], f'images/{mvcode[num]}.jpg')


