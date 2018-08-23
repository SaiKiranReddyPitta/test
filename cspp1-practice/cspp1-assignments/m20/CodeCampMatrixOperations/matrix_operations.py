row=list(map(int,input().split(','))) #input no. of row and column
b=[]
for i in range(0,row[0]):
	a=list(map(int,input().split()))
	b.append(a)
#print(b)

row=list(map(int,input().split(','))) #input no. of row and column
c=[]
for i in range(0,row[0]):
	a=list(map(int,input().split()))
	c.append(a)
#print(c)
l = []
result = [[b[i][j] + c[i][j]  for j in range(len(b[0]))] for i in range(len(b))]
  
# for r in result:
#     print(r)
l.append(result)
print(l)

# Multiplication
m = [] 
result = [[sum(b * c for b, c in zip(b_row, c_col)) 
                        for c_col in zip(*c)]
                                for b_row in b]
# for r in result:
#     print(r)
m.append(result)
print(m)
