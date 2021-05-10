import urllib.request
import urllib.parse
import json
import xmltodict
import pymysql
import time
from datetime import datetime

#코드 실행 시간
starttime = time.time()

#db 연결
db = pymysql.connect(host='172.20.52.185', port=3306, user='root', password='jS8mwpmctzbp', database='dunamis_crm',charset='utf8')
cursor = db.cursor()

# 서비스키 목록
servicekeys = ['HW4VglPG%2BvKoEsgegw5IRcA58wI7IdoZFsmBQvqQsWqjOkDcz6SxW55LN5DE9me47BL2ZlehZ9pVHYaIKWXUfQ%3D%3D',
        'Fbgthodfvtv2UkK0S1yCDd0HYyhNg5qP1ZuADuqK812PN4hOsBi%2BRUgMP6ci4SudQ0fPSbbrvEocp6tj6zKrVg%3D%3D',
        '77e%2B9D0Qn4Iar4T0aU7CmV5D%2B8Rvt31TWZ5%2FySbnr6yvFLvJ5xNFyS48Sq5HNjIiUgHns9Nw3Y7m3sCcyG4jTA%3D%3D',
        'Frx53QwSZXEe2SFxttRB7xQHnfgJV16nWFaVQOUE1vjodBt%2B37ATn0ivVOzyM7dyY4dUxQLuqhSvH9v1GuOz8w%3D%3D',
        '11huxg6VVMGQgV%2FVCNiAmNhI8n%2BRDLG80UMzsTz2aO2SZoIROxiB7OagfFasI2qQ7SzJBVWLSsUEXgMmd8k%2FRg%3D%3D',
        'jquWVcN93lv%2BENb17sRquc0PQtI1SkU9jtlZii1sTQliBzi1EXxz35KePlrTqhaZ7OLx8m3y1nlVRr7MTgvWcw%3D%3D',
        'z8nIWXEfpzZxbWxiungVsSxZlfTDpMvUwyJsjngW1AV0bxvSvnimxVM9C1qzx6aK36qjZ6KDJK460YG6B1jdcg%3D%3D',
        'PeeJaolV7cHtKxV2hPpetlXYF9WwM1DkveaY0C8esbuSp5QXsKQKphaD0pZ5D7Zd1GCprNG7lJcb902EDJ32KQ%3D%3D',
        'Qsv5McUHdujpj6E6GeToPUWSjvxu6%2Fm02H4QyQJpHPfjFd0ybJuEjjZwaYkktx0WnSkWhYk9p8HEP3xlwMXjqw%3D%3D'
        ]

# URL 생성 및 접속
for servicekey in servicekeys:
  num_sql = "SELECT COUNT(*) FROM getelevatorlist2;"
  cursor.execute(num_sql)
  num_result = cursor.fetchall()
  page = num_result[0][0]
  if page == 0:
      page = 200
  page = page//200
  for no in range(page,page+150):
    URL = 'http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList?pageNo='+str(no)+'&numOfRows=200&ServiceKey='+servicekey

    headers = {
        'Host' : 'openapi.elevator.go.kr',
        'User-Agent' : 'curl/7.43.0',
        'Accept' : '*/*',
        'Content-Type' : 'application/xml'
        }

    req = urllib.request.Request(URL, headers=headers)
    text = urllib.request.urlopen(req)
    htmlsrc = text.read()

    try:
# XML to JSON
      jsonstr = json.dumps(xmltodict.parse(htmlsrc))
      jsonstr = json.loads(jsonstr)
      num_row = jsonstr['response']['body']['numOfRows']
      jsonstr = jsonstr['response']['body']['items']['item']

# JSON data parse
      now = datetime.now()
      now = now.strftime('%Y-%m-%d %H:%M:%S')
      for i in range(int(num_row)):
        columes = []
        values = []
        for key, value in jsonstr[i].items():
          columes += [key]
          values += [value]
        sql = "INSERT INTO getelevatorlist2 ("
        for colume in columes:
          sql += colume + ", "
        sql += "DownloadDate"
        sql += ") VALUES("
        for value in values:
          value = str(value).replace("'","")
          sql += "'"+value+"'" + ", "
        sql += "'"+now+"'"
        sql += ")"
        cursor.execute(sql)
        db.commit()
    except:
      print(servicekey)
      #print(htmlsrc)

# db 연결 종료
db.close()

#걸린 시간
endtime = time.time() - starttime
print(endtime)