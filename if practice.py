from random import *
# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
id = range(1, 21) # 1부터 21전까지 = 1 ~ 20
id = list(id) # 타입을 list로 바꿔줌.

n = 1

shuffle(id)

a = sample(id, 10) # 치킨 당첨자
b = sample(id, 10) # 커피 당첨자

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자: " + str(a))
print("커피 당첨자: " + str(b))
print(" -- 축하합니다 -- ")

a = set(a)
b = set(b)
c = a&b
print(c)

# c의 집합의 개수가 1이상일 경우 a를 다시 추출한다.
# if c.count >= 1:
#     sample(a, 1) 이런 식으로~