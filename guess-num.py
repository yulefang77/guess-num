# 猜數字程式 數字範圍 1-100
# 猜對印出 “你猜對了！“
# 猜錯印出 “你猜錯了！你的數字比答案大/小。加油！再猜一次！“

import random

r = random.randint(1, 100)

while True:
	guess = input('請猜一個數字')
	guess = int(guess)
	if r == guess:
		print('你猜對了！')
		break
	elif r > guess:
		print('你猜錯了！')
		print('你的數字比答案小。加油！再猜一次！')
	elif r < guess:
		print('你猜錯了！')
		print('你的數字比答案大。加油！再猜一次！')