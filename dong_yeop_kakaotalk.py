user1 = input("사용자1의 이름을 입력하세요.")
user2 = input("사용자2의 이름을 입력하세요.")
print("끝말잇기 게임을 시작합니다. \n각각 2번의 기회를 갖습니다.")
print("10초의 시간이 지나거나 답이 틀리면 하나의 기회를 잃습니다.")
input_str1 = input("첫 단어를 입력하세요. ")
last_str = input_str1[-1]
count1 = 2
count2 = 2 


while True:
    import time
    start_time = time.time()
    timer = 0
    input_str2 = input("%s님, '%s' 로 시작하는 단어를 입력하세요. " %(user2, last_str))
    timer= time.time() - start_time
    if timer > 10:
        print("시간 초과입니다.")
        count2 -= 1
        print("%s님의 기회는 %s번 남았습니다." %(user2, count2))
        if count2 == 0:
            print(user1, "님이 승리 하셨습니다.")
            break
    
    elif input_str2[0] != last_str:
        count2 -= 1
        print("틀렸습니다. %s님의 기회는 %s번 남았습니다." %(user2, count2)) 
        if count2 == 0:
            print(user1, "님이 승리 하셨습니다.")
            break    
    
    elif input_str2[0] == last_str:
        last_str = input_str2[-1]
        print(input_str2)
        if len(input_str2) < 2:
            reinput_str2 = input("두 글자 이상의 단어를 입력하세요. ")
            input_str2 = reinput_str2
            last_str = input_str2[-1]
   
    
    
    start_time = time.time()
    timer = 0    
    input_str1 = input("%s님, '%s' 로 시작하는 단어를 입력하세요. " %(user1, last_str))
    timer= time.time() - start_time
    if timer > 10:
        print("시간 초과입니다.")
        count1 -= 1
        print("%s님의 기회는 %s번 남았습니다." %(user1, count1))
        if count1 == 0:
            print(user2, "님이 승리하셨습니다.")
            break
    
    elif input_str1[0] != last_str:
        count1 -= 1
        print("틀렸습니다. %s 님의 기회는 %s번 남았습니다." %(user1, count1))
        if count1 == 0:
            print(user2, "님이 승리하셨습니다.")
            break
    elif input_str1[0] == last_str:
        last_str = input_str1[-1]
        print(input_str1)
        if len(input_str1) < 2:
            reinput_str1 = input("두 글자 이상의 단어를 입력하세요. ")
            input_str1 = reinput_str1
            last_str = input_str1[-1]