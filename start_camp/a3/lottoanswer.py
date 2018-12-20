import requests
import random

my_numbers = pick_lotto()
real_numbers = get_lotto()
result = am_i_lucky(my_numbers, real_numbers)





def pick_lotto():
    numbers = list(range(1,46))
    my_numbers = random.sample(numbers,6)
    my_numbers.sort()
    my_numbers = set(my_numbers)




def get_lotto():
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=836'
    response = requests.get(url, verify = False)  #결과튀어나옴
    data = response.json()
    return data


real_numbers = []
get_lotto()=data
   for keys in data:
    if 'drwtNo' in key:
            real_numbers.append(data[key])
     
real_numbers.sort()
bonus_number=data['bnusNo']



count = 0
for my_number in my_numbers:
      for real_number in real_numbers:
          if my_number==real_number:
              count +=1

if count ==6:
    print(1)
elif count == 5 and bonus in my_numbers:
    print(2)


#2번째방법 set(집합)사용하기
my_numbers = set([1,2,7,4,5,6])
real_numbers = set([1,2,3,4,5,6])
bonus=7

match_count=len(my_numbers&real_numbers)
if match_count ==6:
    print('1등')
elif match_count == 5 and bonus in my_numbers:
    print('2등')

