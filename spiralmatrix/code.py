import asyncio
import aiohttp
import math
## нужен pip install aiohttp
## ножно добавить 



async def loadfile(url: str):
    if url.find("http://") == -1 and url.find("https://") == -1:
        return "Error: wrong url"
    async with aiohttp.ClientSession() as session:
        for rep in range(3):   
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                code = response.status
                if 200 <= code < 300:
                    text = await response.text()
                    return text
                elif 400 <= code and code < 600 and rep == 3:
                    return "Error: " + code
                else:
                    return "Info: " + code

            

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

def getSize(matrix: str):
    matrix1 = matrix.rsplit(sep= '\n')
    matrix2 = []
    for row in matrix1:
        if(row.find('+') != 0):
            matrix2.append(row)
    height = len(matrix2)
    lenght = matrix2[0].count('|')
    if lenght == height:
        return -1
    for row in matrix2:
        if(matrix2[0].count('|') != lenght):
            return -1
    return height
    
    

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
    try:
        testmatrix = await loadfile(url)
    except aiohttp.ClientConnectorDNSError:
        return "Error: DNS Error"
    except Exception as e:
        return "Exception"

    if testmatrix.find("Error: ") != -1 or testmatrix.find("Info: ") != -1:
        return testmatrix
    ans = readMatrix(testmatrix)
    size = getSize(testmatrix)
    if size == -1:
        return "Error: Wrong matrix"
    return getSpiral(ans, size)