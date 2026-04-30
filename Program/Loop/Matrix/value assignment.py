#WAP TO CREATE 3x3 MATRIX AND ASSIGN VALUES 0 to 2

#METHOD-1:- Using simple for-loop
matrix = []
for i in range(3):
 matrix.append([])  #append an empty sublist inside the list
 for j in range(3):
  matrix[i].append(j)
print(matrix)

#METHOD-2:- Using list-comprehension technique
matrix = [[j for j in range(3)] for i in range(3)]   
print(matrix)