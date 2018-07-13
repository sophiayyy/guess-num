#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話印出"終於猜對了!"
#猜錯的話要告訴他比答案大/小

import random
r = random.randint(1, 100)
while r <= 100:
	ans = input("1~100,請猜一個數字:")
	if int(r) == int(ans):
		print("終於答對了!")
		break
	else:
		print("你答錯了")
		if int(ans) > int(r):
			print("比答案小")
		else:
			print("比答案大")
		

