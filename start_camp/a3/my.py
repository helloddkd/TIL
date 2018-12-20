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
numbers = list(range(1,46))
while count<1000:
    my_numbers = random.sample(numbers,6)
    match = []
    nomatch = []
    for number in my_numbers:
        if number in real_numbers:
            match.append(number)
        else:
            nomatch.append(number)
    if len(match)==6:
        print('축!!!!!!!!!!!1등',count)
    elif len(match)==5:
        for num in nomatch:
            if bonus_number == num:
                print('2등',count)
    count=count+1
    continue
   