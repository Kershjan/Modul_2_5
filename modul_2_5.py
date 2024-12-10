
def get_matrix(n, m, value):
    matrix = list()
    matrix1 = list()
    for i in range(n):
        matrix.append(matrix1)
    for j in range(m):
        matrix1.append(value)
    return matrix

result = get_matrix(3, 5, 10)
result1 = get_matrix(2, 3, 5)
result2 = get_matrix(4, 2, 6)
print(result, '\n', result1, '\n', result2)
