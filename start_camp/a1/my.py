import requests
import random


url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False)  #결과튀어나옴
data = response.json()


real_numbers = []
for key in data:
   if 'drwtNo' in key:
         real_numbers.append(data[key])

real_numbers.sort()
bonus_number=data['bnusNo']


numbers = list(range(1,46))
my_numbers = random.sample(numbers,6)
print(my_numbers)


#my_numbers 와 real_numbers와 bonus_number
#1등부터 꽝까지의 조건
#1등 : my_numbers = real_numbers
#2등 : real& my가 5개가 같고 , my의 나머지 하나가 bonus number 와 같다.
#3등 : real& my가 5개가 같다.
#4등 : real& my가 4개가 같다.
#5등 : real& my가 3개가 같다.
#꽝 : 나머지 전부 꽝



