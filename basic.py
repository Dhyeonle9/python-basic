# print('hello world')

# 주의사항
# 1. apple / Apple은 다르다
# 2. git add. / git add . 띄어쓰기 주의
# 3. message / massage 오타주의

# 저장 조건 반복 (컴퓨터의 언어 3형식)

# variable (변수)

# 1. 숫자 데이터 (int, float, double)
dust = 10
# 변수 dust에 값 10을 assignment(할당)했다
# print(dust)

# 2. 글자 데이터 (string)
dust = '5'
# print(dust)

# 3. 참/거짓 (boolean)
dust = True #False
# print(dust)

# list - 같은 변수에 데이터를 순차적으로 저장할 때 (array)
dust_list = [10, 20, 0, 50, 100]
# print(dust_list)

# print(dust_list[3])

# dictionary - key에 따른 각각의 정보를 함께 나타낼 때 사용하는 자료형 (연관배열)
# var = {
#   'key1': value1,
#   'key2': value2,
# }

dust_dict = {
    '서울': 100,
    '대전': 10,
    '부산': 50,
}

# print(dust_dict)
# print(dust_dict['부산']) # 특정 key의 value에 접근하기 위함


# 2. 조건
age = 10

if age > 20:
    print('성인입니다.')
elif age > 8:
    print('청소년입니다.')
else:
    print('어린이입니다.')


# 실습 1
dust = 20
# dust 값이
# 150보다 크거나 같다면 -> 매우나쁨
# 80~149 -> 나쁨
# 30~79 -> 보통
# 0~29 -> 좋음

if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust >30:
    print('보통')
else:
    print('좋음')

# 강사님 solution
# if 150 <= dust:
    # print('매우나쁨')
# elif 80 <= dust < 150:
    # print('나쁨')
# elif 30 <= dust and dust < 80:
    # print('보통')
# else:
    # print('좋음')


# 3. 반복

menus = ['김치찜', '삼겹살', '김밥', '머핀']

n = 0
while n < 4:
    print(menus[n])
    n = n + 1

for menu in menus:
    print(menu)

