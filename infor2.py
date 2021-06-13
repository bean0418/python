subj_list = [] # 과목 리스트
unit_a = 0 # 총 단위
school_grades = 0 # 등급 * 단위
result = 0 # 최종 내신

while True:
    subj = input("[내신 산출 계산기]\n과목을 입력해주세요\n중지하시려면 중지를 입력해주세요: ")
    
    if subj == "중지":
        print("[과목 입력을 중지]")
        print("입력된 과목의 수는", str(len(subj_list)) + "개입니다.")
        subj_list.append("과목없음") # 리스트의 마지막
        for i in subj_list:
            if i == "과목없음":
                result = school_grades/unit_a
                print("최종 내신은" , str(result) + "입니다.")
                break
            grade = input("%s의 등급을 입력해주세요: " %(i))
            unit = input("%s의 단위수를 입력해주세요: " %(i))
            school_grades += float(grade) * float(unit)
            unit_a += float(unit) # 총 단위 더하기
        break
    else:
        subj_list.append(subj)
        continue