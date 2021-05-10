# 클래스에서 특정 함수만 가져다 사용하고 싶은 경우 

from mod1 import add      # mod1 class 함수에서 add 라는 함수만 가져다 사용한다.

# 클래스 파일이 있는 폴더가 다를 경우 해당 파일의 경로를 지정해줘야 한다.

import sys
sys.path.append("c:\\jetbot\\subFolder")   # 경로를 추가해준다.

import mod1                 # 이제 mod1 클래스를 import 할 수 있다.
print(mod1.add(3,4))