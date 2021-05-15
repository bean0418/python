total = int(input("전체 학생 수를 입력해 주세요.")) # 전체 학생 수를 입력 받음.
index = total # 입력 받은 학생 수 만큼 while문을 반복해야되기 때문에 index로 변수를 지정.

from random import * # 랜덤 함수 호출
a = [] # 리스트를 공백으로 둠으로써, undefined 오류를 방지.

while index >= 1: # index가 1 이상이면,
    b = randint(0, 100) # b에 1~100 중 임의로 난수를 지정함.
    a.append(b) # 지정된 난수를 a라는 리스트의 맨 뒤에 추가.
    index -= 1 # 한 번 반복할 때마다 index를 1씩 줄임. (횟수의 의미)
    if index == 0: # 반복 진행 중에 index 값이 0이 되면(횟수가 끝나면)
        print(a) # 리스트 a가 어떻게 구성되어있는 지 출력
        print((len(a))) # 리스트 a의 구성요소들의 개수를 출력

grade = [] # undefined 방지

for m in a: # 리스트 a에 있는 요소들을 하나씩 가져와서 m에 넣는 것을 반복
    if m >= 90: # a에서 m으로 옮기면서 m이 90 이상이면, grade의 맨 뒤에 "A"를 추가
        grade.append("A")
    elif m >= 80: # m이 80 이상이면, grade의 맨 뒤에 "B"를 추가
        grade.append("B")
    elif m >= 70: # m이 70 이상이면, grade의 맨 뒤에 "C"를 추가
        grade.append("C")
    elif m >= 60: # m이 60 이상이면, grade의 맨 뒤에 "D"를 추가
        grade.append("D")
    elif m >= 50: # m이 50 이상이면, grade의 맨 뒤에 "E"를 추가
        grade.append("E")
    else: # m이 50 미만이면, grade의 맨 뒤에 "F"를 추가
        grade.append("F")

print(grade) # grade의 구성을 확인.

countA = 0 # undefined 방지.
countB = 0
countC = 0
countD = 0
countE = 0
countF = 0

for n in grade: # grade의 요소들을 n으로 하나씩 옮기는 것을 반복
    if n == "A": # 하나씩 옮기는 과정에서 "A"가 나올 때마다, countA = countA + 1
        countA += 1
    if n == "B": # 생략
        countB += 1
    if n == "C":
        countC += 1
    if n == "D":
        countD += 1
    if n == "E":
        countE += 1
    if n == "F":
        countF += 1

# 출력문
print("A를 받은 사람: ", int(countA), "명", sep="")
print("B를 받은 사람: ", int(countB), "명", sep="")
print("C를 받은 사람: ", int(countC), "명", sep="")
print("D를 받은 사람: ", int(countD), "명", sep="")
print("E를 받은 사람: ", int(countE), "명", sep="")
print("F를 받은 사람: ", int(countF), "명", sep="")

print("A를 받은 사람 비율: " , round(float(countA/total*100)) , "%", sep="")
print("B를 받은 사람 비율: " , round(float(countB/total*100)) , "%", sep="")
print("C를 받은 사람 비율: " , round(float(countC/total*100)) , "%", sep="")
print("D를 받은 사람 비율: " , round(float(countD/total*100)) , "%", sep="")
print("E를 받은 사람 비율: " , round(float(countE/total*100)) , "%", sep="")
print("F를 받은 사람 비율: " , round(float(countF/total*100)) , "%", sep="")