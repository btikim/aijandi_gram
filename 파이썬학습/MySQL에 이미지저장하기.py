# 이미지 저장할 테이블 만들기

# create table images(
#     image_nm int auto_increment primary key,
#     image_data blob)

# 파이썬에서 이미지 파일 저장

import pandas as pd 
from sqlalchemy import create_engine
from PIL import Image
import base64
from io import BytesIO

engine = create_engine('mysql+pymysql://monty:some_pass@15.164.83.96/python2', echo=False)
buffer = BytesIO()
im = Image.open('yu_1.jpg')
#im.show()

im.save(buffer, format='jpeg')
img_str = base64.b64encode(buffer.getvalue())
print(img_str)          # 변환된 데이터 확인 기능

img_df = pd.DataFrame({'image_data':[img_str]})
img_df.to_sql('images', con=engine, if_exists='append', index=False)

# sqlchemy 및 pandas의 to_sql 을 사용하였다.

