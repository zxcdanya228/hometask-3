n = int(input("Введите количество элементов в списке: "))

list_a = [int(s) for s in input().split()]

p = int(input())

list_b = [x for x in list_a if x != p]
print(list_b)