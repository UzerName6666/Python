import spiralmatrix
import asyncio

testurl = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
testmatrix = asyncio.run(spiralmatrix.loadfile(testurl))
print(testmatrix)
ans = spiralmatrix.readMatrix(testmatrix)
print(spiralmatrix.getSpiral(ans, 4))

