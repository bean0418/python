n = 20 # 횟수를 제한.

schoolgrades_infor = 0 # 변수를 모두 0으로 설정.
schoolgrades_calcul = 0
schoolgrades_economics = 0
schoolgrades_society = 0
grade = 0
subj_n = 1
result = 0

while n >= 0: # n이 0이상이면 계속 실행됨.
    subj, grade = input("과목과 등급을 공백을 두고 입력해주세요:\n예시) 정보 2\n(프로그램을 종료하거나 과목 입력이 끝났다면 끝 0을 입력해주세요.)").split()
    # 과목과 등급을 입력 받고 종료 시 입력 문구를 안내함.
    grade = float(grade) # 등급을 받을 때 마다 실수형으로 변환함.
    if subj == "끝": # 종료가 입력되었을 경우 종료 안내문을 출력.
        print("프로그램이 종료되었습니다.")
        n = -1 # n을 음수로 설정함으로써 반복문 중지.
    else:
        n -= 1 # 과목, 등급이 입력될 때마다 n이 1씩 줄어듦.

    unit = 0 # 단위수를 0으로 설정.
    
    '''
    단위 수
    미적분: 3
    경제: 3
    사회문화: 2
    정보: 5
    '''
    if subj != "끝":
        if subj == "정보":
            unit = 5
            schoolgrades_infor = grade * unit
            subj_n += 5
        elif subj == "미적분":
            unit = 3
            schoolgrades_calcul = grade * unit
            subj_n += 3
        elif subj == "경제":
            unit = 3
            schoolgrades_economics = grade * unit
            subj_n += 3
        elif subj == "사회문화":
            unit = 2
            schoolgrades_society = grade * unit
            subj_n += 2

result = (schoolgrades_infor + schoolgrades_calcul + schoolgrades_economics + schoolgrades_society)/subj_n
# 등급을 모두 더한 뒤 단위 수의 총합으로 나눔.
if result != 0:
    print("내신 산출 완료:", round(result,0))
else:
    print("등급의 합이 0점이거나 입력된 등급이 없습니다.")

print(subj_n)