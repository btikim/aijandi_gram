# mysql에 넣은 데이터를 다시 불러와서 이미지 확인하기

import pandas as pd
from sqlalchemy import create_engine
from PIL import Image
import base64
from io import BytesIO

engine = create_engine('mysql+pymysql://monty:some_pass@15.164.83.96/python2', echo=False)

img_df = pd.read_sql(sql='select * from images', con=engine)
img_str = img_df['image_data'].values[0]

img = base64.decodestring(img_str)

im = Image.open(BytesIO(img))
im.show()







