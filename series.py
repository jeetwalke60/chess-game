a=int(input('enter the value of rows'))
b=int(input('enter the values of column'))
matrix = [a][b]
for i in range(a):
for j in range(b):
c=int(input())
matrix.append(c)
for i in range(a):
for j in range(b):
print(matrix[i][j],end=" ")
  print()