#random 모듈을 꺼낸다
import random
# if for while else elif는 파이썬의 예악어

# 1 ~ 45 까지의 숫자가 들어있는 통을 만든다
numbers = range(1,46)
#range는 a <= n <b 이런느낌
# 통에서 6개를 랜덤으로 고른다.
# 고른 숫자를 출력
lucky = random.sample(numbers, 6)
#sample 비복원추출
print(lucky)