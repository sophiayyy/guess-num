import random
start = input("請輸入隨機數字開始值:")
end = input("請輸入隨機數字結束值:")
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	ans = input("請猜一個數字:")
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
		

