'''
Author Name: Sai Kiran Reddy Pitta
Date: 04-08-2018
'''
def main():
    '''
    Here we have to do the product using given Numbers
    '''
    int_input = int(input())
    flag = 0
    if int_input < 0:
        flag = 1
        str_input = str(int_input)
        str_input = int_input[1:]
    else:
        str_input = str(int_input)
        int_input = abs(int_input)
        temp2 = 0
        temp1 = 1
    for var in str_input:
        temp2 = int(var)
        temp1 = temp1 * temp2
    if int_input == 0:
        print(temp2)
    else:
        if flag == 1:
            temp1 = - temp1
            print(temp1)
        else:
            print(temp1)

if __name__ == "__main__":
    main()
