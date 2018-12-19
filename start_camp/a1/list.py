team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]

new_member = ['js', 10]

# team = team + new_member

team += new_member
#len(team) == 8개

del(team[2]) #neo가 없어짐
del(team[2]) #이제 네오의 잔고 100이 사라짐

len(team)  # 요소 몇 개 들어 있는지 알려줌 ==6

del(team[2:4]) #3까지 지우고싶으면 4 입력
