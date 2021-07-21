l = ["정보", "사문", "미적분"]

subj = input("과목을 입력해주세요.")

n = 3

while n >= 0:
    if subj != "정보" or subj != "사문" or subj != "미적분":
        print("잘못된 과목입니다.")
    else:
        print("올바르게 입력되었습니다.")
        n -= 1