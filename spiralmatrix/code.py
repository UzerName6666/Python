
def getSpiral(matrix, size):
    newmatrix = [0] * size * size
    i = 0
    for loop in range(0, int(size / 2)): # Проходим по каждому кольцу
        for left in range(loop, size - 1 - loop):
            newmatrix[i] = matrix[left * 4 + loop]
            i += 1
        for down in range(loop, size - 1 - loop):
            newmatrix[i] = matrix[down + (size - loop - 1) * size]
            i += 1
        for right in range(loop, size - 1 - loop):
            newmatrix[i] = matrix[(size) * size - 1 - (size * right) - loop]
            i += 1
        for up in range(loop, size - 1 - loop):
            newmatrix[i] = matrix[loop * size + size - up - 1]
            i += 1
    if size % 2 == 1: ## Берём центр для нечётных
        newmatrix[size * size - 1] = matrix[int(size * size / 2) - 1]
    return newmatrix