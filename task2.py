# Задача 2
# Дана матрица M. Напишите функцию, которая бинаризует матрицу по некоторому threshold (то естьь, все значения, большие threshold становятся равными 1, иначе 0).
 
def binarize(M, threshold = 0.5):
    result = []
    
    for row in M:
        newRow = []
        for item in row:
            newRow.append(1 if item > threshold else 0)
        result.append(newRow)
    
    return result

inputFile = open("input.txt", "r")

testCount = int(inputFile.readline())

inputFile.readline()
 
for i in range(testCount):
    print ("Тест {}:".format(i + 1))

    n = int(inputFile.readline())
    threshold = float(inputFile.readline())
    
    matrix = []
    
    for i in range(n):
        row = list(map(float, inputFile.readline().split(" ")))

        matrix.append(row)
        
    print("Исходные данные:")
    print("Threshold = {}".format(threshold))

    for row in matrix:
        for item in row:
            print("{}".format(item), end=" ")
        print()
    
    print("\nБинарная матрица:")
    
    for row in binarize(matrix, threshold):
        for item in row:
            print("{}".format(item), end=" ")
        print()
    
    print("--------------------------------------------------")

    inputFile.readline()

inputFile.close()