# 12.19.

### 1. morning quiz

* 평균을 구하는 함수를 스스로 정의하기

```
def average (list):

	return sum(list)/len(list)
```

```
dict average = sum(dict.values()/len(dict))
```



* 딕셔너리 자료형 다루는 방법 익히기 

  - key : values  를 모아서 출력하기 ****for문에서 양손으로 끄집어낼 수 있다!

  ```
  #교수님 답
  for city, temperatures in cities_temp.items():
      #print(city+ ' : ' +str(round(average(temperatures),3)))
      avg_temperagure = round(average(temperatures),3)
      print('{0}: {1}'.format(city, avg_temperagure))
  ```


```
items = cities_temp.items()
values = cities_temp.values()
cities = cities_temp.keys()


temp_aver =[]
for value in values:
    temp_aver.append(average(value[0:4]))

result = []
number = 0
for city in cities:
    print(city,':', temp_aver[number])
    result.insert(number,[city,temp_aver[number]])
    number=number+1
```

나는 value와 키를 각각 뽑아내느라 for문을 두 개썼지만 한꺼번에 뽑아낼 수 있다는 것을 배웠으니 다음부터는 잘 사용할 것이다~





* **이중 리스트** 값들을 통틀어서 가장 큰 값과 가장 작은 값을 찾아내기

```
cities_temp = {
    '서울':[-6,-10,5],
    '대전':[-3,-5,2],
    '광주':[0,-5,10],
    '구미':[2,-2,10]
}

#all_temp에 모든 기온을 모은다
all_temp = []
for key, value in cities_temp.items():
    all_temp += value

print(all_temp)

#all_temp에서 highest / lowest를 찾는다

highest=max(all_temp)
lowest=min(all_temp)
print(highest, lowest)

# cities_temp에서 highest / lowest가 속한 도시를 찾는다.

hottest = []
coldest = []

for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key)

print(hottest, coldest)
```

```

coldest = 1000000
hottest = -1000000
for city in cities_temp.keys():
    for temper in cities_temp[city]:
        if temper<coldest:
            coldest=temper
        if temper>hottest:
            hottest=temper

for city in cities_temp.keys():
    for temper in cities_temp[city]:
        if temper==coldest:
            print('최근 3일간 가장 추웠던 곳은 ', city)

for city in cities_temp.keys():
    for temper in cities_temp[city]:
        if temper==hottest:
            print('최근 3일간 가장 더웠던 곳은 ', city)

```

* - for문을 중복으로 돌려서 이중리스트에서 값을 뽑아낼 수 있다는 사실을 외워야 한다.
  - 최대 혹은 최소값을 찾기 위해서는 int형 변수를 만들어서 리스트 요소들과 하나하나 비교한 뒤, 더 크거나 작은 값을 변수에 저장하면 된다.



```
로또픽
import requests
import random


url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=836'

response = requests.get(url, verify = False)  #결과튀어나옴
data = response.json()


real_numbers = []
for key in data:
   if 'drwtNo' in key:
         real_numbers.append(data[key])

real_numbers.sort()
bonus_number=data['bnusNo']


count = 0
match = []
nomatch = []
numbers = list(range(1,46))


while count<1000000:
    my_numbers = random.sample(numbers,6)
    match = []
    nomatch = []
    for number in my_numbers:
        if number in real_numbers:
            match.append(number)
        else:
            nomatch.append(number)
    # if len(match)==5:
    #     print('3등',count)  
    # elif len(match)==4:
    #     print('4등',count)
    # elif len(match)==3:
    #     print('5등',count)
    # elif len(match)<=2:
    #     print('꽝',count)
    if len(match)==6:
        print('축!!!!!!!!!!!1등',count)
    elif len(match)==5:
        for num in nomatch:
            if bonus_number == num:
                print('2등',count)
    count=count+1
    continue
   
```

* - if와 elif는 각자 줄이 맞아야 (들여쓰기가 똑같이 되어야) 작동이 제대로 된다는 점을 꼭 꼭 기억하기!





### 2. 유용한 툴들



* bootstrap: html 디자인 요소 구현해주는
* start bootstrap: bootstrap 템플릿

* momentum : 크롬확장앱 이쁜사진
* onetrap: 보고있는 탭들 정리해서 닫아주고 모아줌. 시간별로 확인가능
* codecademy: 숙제. html introduction 하기
* C9: 돈내야 쓸 수 있는 컴퓨터 인터페이스 제공. 매우 성능낮지만 아무데서나 코드 짤 수 있는 혁명
* 