import asyncio
import aiohttp
## нужен pip install aiohttp
## ножно добавить 



async def loadfile(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                
                text = await response.text()
                return text
                
        except aiohttp.ClientError as e:
            return f"Ошибка сети/HTTP: {e}"
        except asyncio.TimeoutError:
            return "Ошибка: Превышено время ожидания"
        except Exception as e:
            return f"Произошла ошибка: {e}"

def readMatrix(str: str):
    matrix1 = str.rsplit(sep= '\n')
    matrix2 = ""
    for row in matrix1:
        if(row.find('+') != 0):
            matrix2 += row
    matrix2 = matrix2.replace(' ', '')
    matrix2 = matrix2.replace('|', ' ')
    matrix3 = matrix2.replace('  ', ' ')
    matrix3 = matrix2.rsplit(' ')
    ans = []
    for row in matrix3:
        if(row != ''):
            ans.append(int(row))

    return ans


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

async def get_matrix(url: str):
    testmatrix = await loadfile(url)
    if type(testmatrix) == str:
        return testmatrix
    ans = readMatrix(testmatrix)
    return ans