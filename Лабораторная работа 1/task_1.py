numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sumOfArray = 0
for i in range(0, len(numbers)):
    if numbers[i] == None:
        wrongElement = i
        numbers[i] = 0
    sumOfArray += int(numbers[i])
averageValue = sumOfArray / len(numbers)
numbers[wrongElement] =  averageValue
print("Измененный список:",numbers)