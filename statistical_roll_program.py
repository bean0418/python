# start

from random import *

line_15 = '-'*15
line_25 = '-'*25

appearance_list = [] # default
n = 0

while True:
	ans = input("[주사위 굴리기 프로그램]\n* 주사위를 굴리려면 r, 중지하려면 stop을 입력해주세요.\n* 주사위는 1부터 6까지 있으며, r을 입력할 때마다 1회씩 굴립니다.\n자동으로 주사위를 굴리시려면 auto를 입력해주세요.\n입력(r or stop or auto):")
	
	if ans == 'r':
		roll_result = randint(1, 6)
		print("%s\n%s이(가) 나왔습니다.\n%s"%(line_15, roll_result, line_15))
		appearance_list.append(roll_result)
		n = 1
		continue
		
	elif ans == 'stop':
		print("***** 주사위 굴리기가 중지되었습니다. *****")
		break
		
	elif ans == 'auto':
		if n == 1:
			print("***** r(수동)을 실행시킨 이후에는 auto를 실행시킬 수 없습니다. *****")
			continue
			
		else:	
			ans_auto = input("***** 주사위를 굴릴 횟수를 입력해주세요.(숫자만 입력해주세요.): ")
			for i in range(int(ans_auto)):
				roll_result = randint(1, 6)
				appearance_list.append(roll_result)
				
			print("%s\n1이(가) %s번\n2이(가) %s번\n3이(가) %s번\n4이(가) %s번\n5이(가) %s번\n6이(가) %s번 나왔습니다.\n%s" %(line_25, appearance_list.count(1), appearance_list.count(2), appearance_list.count(3), appearance_list.count(4), appearance_list.count(5), appearance_list.count(6), line_25))	
			break
		
	else:
		print("***** 잘못된 입력입니다. r 또는 stop 또는 auto를 입력해주세요. *****")
		continue

num_value = []

for i in range(1, 7):
	num_value.append(appearance_list.count(i))

while True:
	
	ans2 = input("그래프로 결과를 출력하시겠습니까? (enter yes or no)")
	
	if ans2 == 'yes':
		
		import matplotlib.pyplot as plt
		import numpy as np
		
		x = np.arange(6)
		num = ['1', '2', '3', '4', '5', '6']
		plt.bar(x, num_value, width = 0.3, color = "green")
		plt.xticks(x, num)
		plt.show()
		break
		
	elif ans2 == 'no':
		print("***** 프로그램을 종료합니다. *****")
		break
	
	else:
		print("***** 잘못된 입력입니다. yes 또는 no를 입력해주세요. *****")
		continue
		
# end