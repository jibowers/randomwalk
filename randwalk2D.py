import random

def write_out(nums):
	f = open('randwalk2D_4.csv', 'w')
	for x in nums:
		f.write(x+'\n')
		
	
nums = [0, 1, 2, 3]
dist_list = []
for z in range (0, 100000):
	x = 0
	y = 0
	for i in range (0, 10000):
		a = random.choice(nums)
		if a == 0:
			x += 1
		elif a == 1:
			x -= 1
		elif a == 2:
			y += 1
		elif a == 3:
			y -= 1
	print (str(x) + ", "  + str(y))
	dist_list.append(str(x) + ", "  + str(y))
	
print("Almost done!")
write_out(dist_list)

print("Done!")
