n = int(input("Введите количество элементов в списке: "))

list_a = [int(s) for s in input().split()]

p = int(input())

list_a.insert(0, list_a.pop(p-1))

print(' '.join([str(i) for i in list_a]))