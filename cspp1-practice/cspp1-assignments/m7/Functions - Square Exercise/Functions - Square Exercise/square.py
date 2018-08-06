'''
Author: Sai Kiran Reddy Pitta
Date: 06 Aug 2018
Encoding: UTF-8
'''
def square(x_son):
	x_son = x_son**2
	return x_son

def main():
	data = input()
	data = float(data)
	temp = str(data).split('.')
	if(temp[1] == '0'):
		print(square(int(float(str(data)))))
	else:
		print(square(data))

if __name__== "__main__":
	main()

