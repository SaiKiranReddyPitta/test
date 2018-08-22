#define the gen_primes function here
'''
Author: Sai Kiran Reddy Pitta
Date: 22-08-2018
'''
def genPrimes(a):
	p_n = 2
    p_c = 0
    while p_c < a:
        count = 0
        for i in range(1, p_n):
            if p_n%i == 0:
                count += 1
        if count == 1:
            yield n
            p_c += 1
        p_n += 1
   

def main():
	data = input()
	l = data.split()
	a = int(l[0])
	b = int(l[1])
	primeGenerator = genPrimes(a)
	for i in range(a):
	    p = primeGenerator.next()
	    if i%b == 0:
	        print p
	
if __name__ == "__main__":
	main()
