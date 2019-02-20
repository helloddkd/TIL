# 20190220 

## 어제 문제 리뷰

### 색칠하기 ^^





## 3. 문자열

아스키코드값: 특수문자 < 숫자 < 대문자 < 소문자

```python
print(ord('A')) >> 65
print(chr(65)) >> A
```

다국어처리표준 : 유니코드



```
0x41: 16진수
16*4 + 1 = 65
print(0x41) >> 65
```

> 16진수 한 자리는 2진수의 4자리. 4비트로 표현할 수 있는 표현의 경우의 수가 매우 많아서. 

```
0x41의 4는 0100
1은 0001
따라서 16진수 활용 시 비트값! 사용 가능. 바이트> 비트
```



```
0x01020304
바이트 한 칸당 01, 02, 03, 04가 들어간다.
그런데 순서대로 왼->오가 아니라 오->왼 순서로 들어가는 경우가 있다. 
윈도우는 거꾸로 저장하는 순서를 사용한다. = little endian 방식

높은 자리값이 낮은 순서에 저장(정순서) : Big-endian
높은 자리값이 높은 순서에 저장(거구로) : Little-endian

```

```
자바는 메모리 맨 앞에 size 정보를 붙여준다. C는 맨 뒤에 delimited 문자를 붙여준다.

```



#### 문자열대소비교

```
#C
s1 s2
s1 > s2 -1
s1 < s2 1
s1 == s2 0
```

```
val = val*10 + x
['1','2','3','4'] 이거 1234라는 숫자로 바꾸는 법

```



#### 숫자를 자릿수별로 리스트에 담기

```python
num = 12345
re = []


while num > 0:
    re.append(num % 10)  #자릿수와 인덱스 일치시킴. 아니면 insert하기
    num = num // 10

print(re)
```

```python
# 스트링으로 변환하기 ord('0') == 48
num = 12345
re = []


while num > 0:
    re.append(chr(num % 10 + 48))
    num = num // 10

print(re)
```



### 패턴매칭

* BruteForce

```python
p = 'CATTCCCTGCGCCGC'
t = 'ATTTGTGACCCCTAGTCGGGGGACTGAGTGTGTGTCCCCATTCCCTGCGCCGCCCAGTTT'

lp = len(p)
lt = len(t)

for i in range(lt-lp+1):
    if t[i:i+lp] == p:
        print('True', i)
```

```python
i=0
while i<= lt-lp:
	j = 0
	while j < lp:
        if t[i+j] != p[j]: break
        j += 1
    if j == m:
        print(t[i:i+lp])
        i = i+m-1
    i += 1
```

```python
i=j=0
while i < lt:
    if t[i] == p[j]:
        i,j = i+1, j+1
        if j == lp:
            print(t[i-j:i])
            j=0
    else:
        i = i-j+1
        j = 0
```



* KMP 알고리즘

  > i,j 활용해서 비교하다 이미 비슷한 곳 빼고 그 다음부터 다시 비교!





#### 접미어 접두어

문자열은 문자열의 길이만큼 접미어가 있다. 문자열의 길이만큼 접두어가 있다.

'abcd' 접두어 : a, ab, abc, abcd

​	접미어 : d, cd, bcd, abcd

따라서 한 칸 빌고나서 불일치 난 데 까지의 접두어가 접미어와 같아야 비교의미가 있다.

```python
p = 'abcdabcef'
t = 'ababcdabcdabcef'
print(p)
print(t)
m, n = len(p), len(t)
next = [0] * (m+1)

next[0] = -1
i,j = 0,-1
while i < m:
    while j >= 0 and p[j] != p[i]:
        j =next[j]
    i, j = i+1, j+1
    next[i] = j
print(next)
    

i = j = 0
while i < n:
    while j >= 0 and p[j] != t[i]:
        j=next[j]
    i,j = i+1, j+1
    
    if j==m:
        print(t[i-j:])
        break
```





### 해시



직접테이블, 간접테이블

해시테이블



* id값과 테이블의 저장 인덱스값을 일치시키는 것이 해시다. (직접테이블)

* 간접테이블

  > 사용자 아이디는 8자리, 소문자만 써야 함 -> 나올 수 있는 가능한 아이디의 종류 = 26**8
  >
  > 딕셔너리면편하겠지만 배열이어야 한다면? 8차원 배열을 만들어서 저장하면 읽어올 수 있다.

  

  >  실제로 사용되는 아이디 개수가 3000만개라면 그 정도의 테이블을 만들어두고, 특정 위치를 매핑만 시켜주면 된다. key값(id정보)를 테이블의 특정 위치로 매핑할 때, 일정한 양의 정수값과 일치시켜 주는 것이 해시다!!!!!
  >
  > - 키 값이 다르면 다른 숫자로 매핑되도록 해시값을 만들어내는 과정이 복잡하다. 

* 알고리즘에서는 pattern을 해시화하고, t를 p의 크기만큼 읽어서 해시화한 후, 해시값이 같으면 찾은 거, 아니면 못찾은 거~~~

* 모듈러 연산 합동

  > (a*b)%M
  >
  > = ((a%M)*(b%M))%M

  * 나누기에는 적용 안 됨.

  > (a*b*c)%M
  >
  >  = (((a*b)%M)*c)%M

  -> 스택 오버플로우를 방지하기 위해 큰 수를 작은 수로 나누어 연산하기 위해 필요하다!

```
ph = p[0]*10^3 + p[1]*10^2 + p[2]*10^1 + p[3]
(len(p)가 4일 때 이렇게 함)
```

```
th = t[0]*10^3 + t[1]*10^2 + t[2]*10^1 + t[3]
그 다음 sliding window는
(th-t[0]*10^3)*10 + t[4]

이러는 과정에서 스택 오버플로우 걸릴까봐 모듈연산해주는 것.
```

