# function (함수)
# func(input)

numbers = [100, 2, 3, 4, 5]

max_num = max(numbers)
# == max(1, 2, 3, 4, 5)
# print(max_num)

##################################
import random
# 모듈 사용
# 모듈.내장함수()

random_number = random.randint(0, 100)
# print(random_number)

# 랜덤으로 메뉴 고르기

menus = ['김밥', '라면', '만두']
menu = menus[random.randint(0,2)]
# print(menu)

# 강사님 solution
# random_number = random.randint(0,2)
# print(menus[random_number])

# choice 함수 활용
menu = random.choice(menus)
# print(menu)

#################################
#로또번호

numbers = range(1, 46)
lucky_number = random.sample(numbers, 6)

# print(sorted(lucky_number))

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'
# 일반적으로 상수 데이터는 대문자로 작성

# pip install requests

import requests

res = requests.get(URL)

data = res.json()
print(data)

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

print(lucky_number)
print(lotto_number)

print(set(lucky_number) & set(lotto_number))
# set 데이터를 집합의 형태로 바꿔줌
# & 교집합

