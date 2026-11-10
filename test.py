import spiralmatrix
import asyncio

testurl1 = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
testans1 = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
print("Тестовый вариант")
ans = asyncio.run(spiralmatrix.get_matrix(testurl1))
if(type(ans) == str):
    print("Не пройден: " + ans)
elif ans == testans1:
    print("Пройден")
else:
    print("Не пройден, иная матрица")

print("Пустая ссылка")
ans = asyncio.run(spiralmatrix.get_matrix(' '))
if(type(ans) == str):
    print("Пройден") 
else:
    print("Не пройден")