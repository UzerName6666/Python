import spiralmatrix
import asyncio

testurl = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
print(asyncio.run(spiralmatrix.get_matrix(testurl)))
print(asyncio.run(spiralmatrix.get_matrix(' ')))
