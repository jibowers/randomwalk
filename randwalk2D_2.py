## computes x and y separately

import random

def write_out(x_list, y_list):
	f = open('randwalk2D_1.csv', 'w')
	for i in range(0,len(x_list)):
		f.write(str(x_list[i])+','+str(y_list[i])+'\n')
		
##x
seq = [1, -1]
x_list = []
y_list = []

for x in range (0, 1000):
	d = 0
	for i in range (0, 1000000):
		d += random.choice(seq)
	##print (d)
	x_list.append(d)
for x in range (0, 1000):
	d = 0
	for i in range (0, 1000000):
		d += random.choice(seq)
	##print (d)
	y_list.append(d)
	
print("Almost done!")
write_out(x_list, y_list)

print("Done!")
