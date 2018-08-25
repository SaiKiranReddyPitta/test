'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def read_the_input():
	given_string = ""
	number_1 = int(input())

	for i in range(number_1):
		given_string += input() + '\n'
	print(given_string)

def main():
	'''
	Main function
	'''
	read_the_input()

if __name__ == '__main__':
    main()
