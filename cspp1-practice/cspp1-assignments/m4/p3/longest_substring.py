'''
Author Name: Sai Kiran Reddy Pitta
Date: 02-08-2018
'''
def main():
    '''
    Longest String in Alphabetical order
    '''
    in_s = input()
    count_initial = 0
    count_maximum = 0
    end_index = 0
    for index_s in range(len(in_s)-1):
        if ord(in_s[index_s]) <= ord(in_s[index_s+1]):
            count_initial += 1
        else:
            count_initial = 0
        if count_maximum < count_initial:
            count_maximum = count_initial
            end_index = index_s + 1
    print(in_s[end_index - count_maximum : end_index + 1])

if __name__ == "__main__":
    main()
