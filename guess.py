import random
r = random.randint(1, 100)
count = 0
while r <= 100:
	count += 1
	ans = input("1~100,請猜一個數字:")
	if int(r) == int(ans):
		print("終於答對了!")
		print("這是你猜的第", count, "次!")
		break
	else:
		print("你答錯了")
		if int(ans) > int(r):
			print("比答案大")
		else:
			print("比答案小")
		print("這是你猜的第", count, "次!")
		

