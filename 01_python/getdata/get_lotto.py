import requests



URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

got = requests.get(URL)

print(got)
KOBIS_KEY = 
NAVER_CLIENT_ID = os.getenv()