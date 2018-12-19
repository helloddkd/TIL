

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
