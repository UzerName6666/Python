import spiralmatrix

testmatrix = range(1, 17)

ans = spiralmatrix.getSpiral(testmatrix, 4)
for i in ans:
    print(i, end = ' ')