import requests
import random

def pick_lotto():
    numbers = random.sample(range(1,46),6)
    return numbers

# def get_lotto_jay():
#     url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'
#     response = requests.get(url, verify = False)
#     data = response.json()
#     final_dict = {}
#     listnum = []
#     for key in data:
#         if 'drwtNo' in key:
#             listnum.append(data[key])
#             final_dict['numbers']=listnum
#     final_dict['bonus']=(data['bnusNo'])
#     return final_dict
            
# jay_numbers = get_lotto_jay()
# print(jay_numbers)

def get_lotto(draw_no):
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_no)
    response = requests.get(url, verify = False)
    data = response.json()
    numbers = []
    for key, value in data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    numbers.sort()
    bonus_number = data['bnusNo']
    result = {'numbers': numbers, 'bonus': bonus_number}
    return result 

def am_i_lucky(pick, draw):
    match = set(pick) & set(draw['numbers'])
    if len(match) ==6:
        return('1등')
    elif len(match)==5 and draw['bonus'] in pick:
        return('2등')
    elif len(match) ==5:
        return('3등')
    elif len(match) ==4:
        return('4등')
    elif len(match) ==3:
        return('5등')
    else:
        return('꽝')

# list_1=[1,2,3,4,5,7]
# dict_1={
#     'numbers':[1,2,3,4,5,6],
#     'bonus':7
# }

# def am_i_lucky(picks, draws):
#     count = 0
#     for pick in picks:
#           for draw in draws['numbers']:
#             if pick==draw:
#               count +=1
#     if count ==6:
#         return '1등'
#     elif count == 5 and draws['bonus'] in picks:
#         return '2등'
#     elif count == 5:
#         return '3등'
#     elif count==4:
#         return '4등'
#     elif count==3:
#         return '5등'
#     elif count<=2:
#         return '꽝'
        

# my_numbers = pick_lotto()
# print('내번호는', my_numbers)
# real_numbers = get_lotto(827)
# print('로또번호는',real_numbers)
# result = am_i_lucky(my_numbers, real_numbers)
# print('결과는', result)

 
# count = 0
# for my_number in my_numbers:
#       for real_number in real_numbers:
#           if my_number==real_number:
#               count +=1

# if count ==6:
#     print(1)
# elif count == 5 and bonus in my_numbers:
#     print(2)


# #2번째방법 set(집합)사용하기
# my_numbers = set([1,2,7,4,5,6])
# real_numbers = set([1,2,3,4,5,6])
# bonus=7

# match_count=len(my_numbers&real_numbers)
# if match_count ==6:
#     print('1등')
# elif match_count == 5 and bonus in my_numbers:
#     print('2등')
