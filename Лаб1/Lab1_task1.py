numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
length=len(numbers)
sum_=sum(numbers[0:4]+numbers[5:])
numbers[4]=sum_/length
print("Измененный список:",numbers)

