import requests



URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

got = requests.get(URL)

print(got)


http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=555226eeca79dde09ad09563c98d1523&targetDt=20190113&weekGb=%220%22