'''
Author: Sai Kiran Reddy Pitta
Date: 6 Aug 2018
Encoding: UTF-8
'''
def main():
    """
    This fucntion checks whether the given number is a perfect cube or not
    """
    n_pc = int(input())
    t_pc = 0
    for i in range(1, n_pc + 1, 1):
        if i**3 == n_pc:
            t_pc += 1
            print(str(n_pc) + " is a perfect cube")
            exit()
    if t_pc == 0:
        print(str(n_pc)+" is not a perfect cube")
if __name__ == "__main__":
    main()
