# 18.12.18

## 1. 리스트

## 2. 딕셔너리

컨트롤 + z 눌러서 파이썬 디렉토리 불러오기

python을 터미널에 입력해서 불러오기

pip install requests 입력해서 requests 기능 설치하기



왼쪽에는 파이썬, 오른쪽에는 그냥 파워셀 띄워놓고 작업하기



- 

- 

  - ```
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
    
    ```


# 4. Function

f(x)=y

[ ]: list

( ): 함수. 글자 뒤에 소괄호 붙으면 무조건 함수. 이건 정의





함수 존재이유: 문제를 해결하기 위해 코드를 사용. 같은 문제가 여러 번 발생할 경우 한번에 처리하기 위해서

ex) w키를 이동키로 만드는 코드: w를 사용자로부터 입력받으면 1초에 몇 픽셀씩 이동하라. w키에서 손을 뗄 때까지

​	-> move.forward()로 만들어서 여러 번 반복.

round(): 반올림  *round(1.876,2) 소수점 둘째자리까지 반올림 -> 1.88

ceil(): 올림

floor(): 내림



#### * 함수작동내용확인방법

1. 구글에 검색 -> www.w3schools.com: 믿을 수 있는 출처, https://docs.python.org: 완전한 공식문서.(검색어:  python 함수명 documentation)

2. help(함수명): 쉘에 바로 입력하기

   round(number[, ndigits]) -> number 

   ​	대괄호 안에 있는 인자는 필수가 아니라는 점 





### 5. Method

> **메서드는 함수다! 다만 주어.동사() 형식으로 이루어지면 주어 자리에 오는 객체가 할 수 있는 행동만 한다.** 

변수명.메소드명() : 메소드는 함수일까 아닐까? 뒤에 소괄호 붙었으니 함수다

ex) my_list.??() : 변수는 주어고 주어가 할 수 있는 행동(동사)를 메소드라고 한다.

정수는 개념, 클래스       100은 개체

메소드는 객체에 속한 함수다.



자료형에 따라 쓸 수 있는 메소드가 다름

>>> lang
>>> 'python'
>>> lang.capitalize()
>>> 'Python'

여전히 lang = 'python'

 'python'.index('o')
4



메소드 종류

* 원본은 그대로 두고 뭔가를 출력: index()
* 출력하지 않고 원본을 수정 :  sort(), reverse()

```
numbers = [9,5,8,1,2]
sorted_numbers = numbers.sort()
sorted_numbers #비어있다. sort는 출력함수가 아니므로
```

```
>>> samsung
['sds', 's1', 'elec']
>>> samsung+['bio']
['sds', 's1', 'elec', 'bio']
>>> samsung
['sds', 's1', 'elec']
>>> samsung.append('bio')
>>> samsung
['sds', 's1', 'elec', 'bio']
```

append 가 원본을 바꾸므로 그냥 +가 아니라 append를 많이 쓴다.



| str      | int  | list         | bool  |
| :------- | ---- | ------------ | ----- |
| 'python' | 100  | ['a',3,True] | False |
|          |      |              |       |

```
import webbrowser


keywords = [
    'python', 'study abroad', 'you',
]



for keyword in keywords:
    url = 'https://www.google.com/search?q='+keyword
    webbrowser.open_new(url)

```





```
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False)  #결과튀어나옴
data = response.json()


real_numbers = []
for key in data:
   if 'drwtNo' in key:
         real_numbers.append(data[key])

print(real_numbers)
```
