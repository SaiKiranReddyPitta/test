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
result = [[b[i][j] + c[i][j]  for j in range(len(b[0]))] for i in range(len(b))]
  
for r in result:
    print(r)

# Multiplication
for i in range(len(b)):
 
    for j in range(len(c[0])):
 
        for k in range(len(c)):
            result[i][j] += b[i][k] * c[k][j]
 
for r in result:
    print(r)