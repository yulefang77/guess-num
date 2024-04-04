# 猜數字程式 讓使用者決定猜數字的範圍
# 猜對印出 “你猜對了！“
# 猜錯印出 “你猜錯了！你的數字比答案大/小。加油！再猜一次！“
# 每次猜完後列印出 “你猜了 n 次了喔！“
 
import random

while True:
	start = input('請決定猜數字遊戲的啟始值： ')
	end = input('請決定猜數字遊戲的結束值： ')
	start = int(start)
	end = int(end)

	if start >= end:
		print('啟始值必須小於結束值，請重新設定。')
	else:
		break



r = random.randint(start, end)
count = 0

while True:
	count += 1
	
	while True:
		guess = input('請猜一個數字: ')
		guess = int(guess)
		if guess < start or guess > end:
			print('你猜的數字，超出你設定的範圍: ', start, '-', end)
		else:
			break
			
	if r == guess:
		print('你猜對了！')
		print('你一共猜了 ', count, ' 次。')
		break
	elif r > guess:
		print('你猜錯了！')
		print('你的數字比答案小。加油！再猜一次！')
	elif r < guess:
		print('你猜錯了！')
		print('你的數字比答案大。加油！再猜一次！')
	print('你猜了 ', count, ' 次了喔！')