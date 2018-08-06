'''
Author: Sai Kiran Reddy Pitta
Date: 06 Aug 2018
Encoding: UTF-8
'''


def evalQuadratic(a, b, c, x):
	d = (a)*(x**2)+(b)*(x)+c
	return d
    

def main():
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	# print(data)
	for x in range(len(data)):
		temp = str(data[x]).split('.')
		if(temp[1] == '0'):
			data[x] = int(float(str(data[x])))
		else:
			data[x] = data[x]
	print(evalQuadratic(data[0],data[1],data[2],data[3]))

if __name__== "__main__":
	main()

