name = input("당신의 이름은 무엇입니까?")
age = int(input("나이가 어떻게 되나요?"))
location = input("당신이 사는 지역은 어디입니까?")
school = input("당신이 현재 재학 중인 학교는 어디입니까? 없다면 '없다'라고 답해주세요.\
(졸업도 포함)")
hobby = input("당신의 취미는 무엇입니까?")

if school == "없다":
    school = "현재 재학 중이 아님"
else:
    None

# is_adult = age >= 20 # 어른인가요?

if age >= 20:
    a = "예."
else:
    a = "아니요."

print("안녕하세요 저의 이름은 " + name + "입니다.")
print("저의 나이는" , str(age) +"세이며,")
print("제가 사는 곳은" ,location+ "입니다.")
print("학교는" , school +"이고,")
print("저의 취미는" , hobby +"입니다.")
print("성인인가요? ", a)