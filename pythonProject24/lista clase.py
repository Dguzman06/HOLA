cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)

matrix = [[j for j in range (5)] for i in range (5)]
print(matrix)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
comb = [(x,y) for x in nums1 for y in nums2]
print(comb)

#crear una lista de valores enteros en los datos ingresados
n = int(input("ingrese mumeros enteros"))
m = [int(input()) for _ in range(n)]
print(n)


