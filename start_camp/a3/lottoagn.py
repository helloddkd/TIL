import random

def pick_lotto():
    numbers = random.sample(range(1,46),6)
    return numbers

print(pick_lotto())


def get_lotto(draw_no):
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_no)

