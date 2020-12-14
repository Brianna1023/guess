import random
start = input('請決定起始數字:')
end = input('請決定結束數字:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1
	num = input('請猜一個數字:')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比猜的數字大~')
	elif num < r:
		print('比猜的數字小~')
	print('這是你猜的第', count, '次')
	
