# Python 샘플 코드 #

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('sido') : '서울특별시', quote_plus('sigungu') : '은평구', quote_plus('buld_nm') : '씨엔빌' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body