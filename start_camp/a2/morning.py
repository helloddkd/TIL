

#1. 평균구하기
my_score = [79,84,66,93]

def average(list):
    return sum(list) / len(list)

my_average = average(my_score)
print('list average = ', my_average) 

#2. 
your_score = {
    '수학':87,
    '국어':83,
    '영어':76,
    '도덕':100,
}

average = sum(your_score.values()) / len(your_score)
print('dict average = ', average) 

#3. 도시별온도평균, 서울: ? 대전: ? 광주: ? 구미: ? 총 4줄
#4. 도시 중에 최근 3일간 가장 추웠던 곳과 가장 더웠던 곳 Hottest: ??, Coldest: ??


cities_temp = {
    '서울':[-6,-10,5],
    '대전':[-3,-5,2],
    '광주':[0,-5,10],
    '구미':[2,-2,9]
}

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


#교수님 답
for city, temperatures in cities_temp.items():
    #print(city+ ' : ' +str(round(average(temperatures),3)))
    avg_temperagure = round(average(temperatures),3)
    print('{0}: {1}'.format(city, avg_temperagure))




# 여기부터4번  밸류값 각각의 최대값 구한 다음 튜플로 저장해서 정렬
# sorted(cities_temp.values(), key=lambda t : t[1])

# item in sorted(items, key=lambda x:max(values))

# max_value=[]
# for value in values:
#     max(value[0:4]))

# max(item)


# temperature =[]
# for value in values:
#     temperature+=value


# values_max = []
# number = 0
# for city in cities:
#     for temper in temperature:
#         max(temper)
#     value_max.insert(number,[city,max(temperature[number])])
#     number=number+1


# from operator import itemgetter
# >>> alist = [(1,3),(2,5),(2,4),(7,5)]
# >>> min(alist)[0], max(alist)[0]
# (1, 7)
# >>> min(alist, key=itemgetter(1))[1], max(alist, key=itemgetter(1))[1]
# (3, 5)

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

# 출처: 강진우 반장님 코드


#교수님 답
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


