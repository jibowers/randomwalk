##
import random

def write_out(nums):
	f = open('randwalk_2.csv', 'w')
	for x in nums:
		f.write(str(x)+'\n')
	

seq = [1, -1]
dist_list = []
for x in range (0, 1000):
	d = 0
	for i in range (0, 1000000):
		d += random.choice(seq)
	##print (d)
	dist_list.append(d)

##for x in dist_list:
	##print(x)
print("Almost done!")
write_out(dist_list)
