import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False)  #결과튀어나옴
data = response.json()


# real_numbers = []
# for key in data:
#    if 'drwtNo' in key:
#          real_numbers.append(data[key])

# print(real_numbers)

real_numbers = []
for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number=data['bnusNo']



# real_numbers = [
#     data['drwtNo1'],
#     data['drwtNo2'],
#     data['drwtNo3'],
#     data['drwtNo4'],
#     data['drwtNo5'],
#     data['drwtNo6'],    
# ]



