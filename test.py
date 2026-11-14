import spiralmatrix
import asyncio

testurl1 = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
testans1 = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
print("Тестовый вариант")
ans = asyncio.run(spiralmatrix.get_matrix(testurl1))
if(type(ans) == str):
    print(ans)
elif ans == testans1:
    print("Пройден")
else:
    print("Не пройден, иная матрица")

print("Пустая ссылка")
ans = asyncio.run(spiralmatrix.get_matrix(' '))
if(type(ans) == str):
    if(ans == "Error: wrong url"):
        print("Пройден")
    else:
        print("Не пройден: " + ans)
else:
    print("Не пройден")

testurl2 = "https://raw.githubusercontent.com/UzerName6666/Python/refs/heads/main/testmatrix1.txt"
testans2 =  [10, 50, 90, 130, 210, 220, 230, 240, 250, 200, 150, 100, 50, 40, 30, 20, 60, 100, 170, 180, 190, 140, 90, 80, 120]
print("Нечётный размер")
ans = asyncio.run(spiralmatrix.get_matrix(testurl2))
if(type(ans) == str):
    print("Не пройден: " + ans)
elif ans == testans2:
    print("Пройден")
else:
    print("Не пройден, иная матрица")

testurl3 = "https://raw.githubusercontent.com/UzerName6666/Python/refs/heads/main/testmatrix2.txt"
print("Другой размер ячеек")
ans = asyncio.run(spiralmatrix.get_matrix(testurl3))
if(type(ans) == str):
    print("Не пройден: " + ans)
elif ans == testans2:
    print("Пройден")
else:
    print("Не пройден, иная матрица")
testurl4 = "https://raw.githubusercontent.com/UzerName6666/Python/refs/heads/main/testmatrix3.txt"
ans = asyncio.run(spiralmatrix.get_matrix(testurl4))
print("Прямоугольная матрица")
if(type(ans) == str):
    if(ans == "Error: Wrong matrix"):
        print("Пройден")
    else:
        print("Не пройден: " + ans)
else:
    print("Не пройден")