## 1. 





> 자신의 반에 있는 사람들의 데이터를 저장하는 Student모델을 생성합니다. Student모델이 가져야 할 필드는 아래와 같습니다.

 ```name(이름) : CharField ```

```email(이메일) : CharField ```

```birthday(생년월일) : datetimeField ```

```age(나이) : IntegerField```





답:

```
django-admin startapp ss3

#ss3/models.py에 

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)  #charfield는 무조건 max-length를 지정해줘야 한다.
    email = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    age = models.IntegerField()
    def __str__(self):
        return f'{self.name}'
```

그리고 installed-app에 ss3을 추가한다!

그리고 쉘에 입력한다.

python manage.py makemigrations ss3 : ss3의 클래스로 정의된 모든 모델들을 db로 이동시킬 준비를 한다.
python manage.py sqlmigrate artists 0001 : ss3의 migrations 폴더에 생성된 0001 기록을 sql로 변환한다.
python manage.py migrate : 해당 프로젝트에 있는 모든 sqlmigrate 상태의 파일들을 전부 옮긴다.





```
#ss3/admin.py에서

from django.contrib import admin
from .models import Student
# Register your models here.

admin.site.register(Student)
```



이렇게 하면 관리자 페이지에서 모델링을 할 수 있다.

![1548319235437](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548319235437.png)



![1548319217922](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548319217922.png)

''

![1548319251401](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548319251401.png)



인터페이스에서 바로바로 record를 추가할 수 있다.

Student 클래스를 정의할 때 이미 __str__메소드를 사용해 name이 출력되도록 했다.