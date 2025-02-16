# Сложность по временнЫм затратам
a = len(arr) - 1  # O(1)
out = list()  # O(1)
while a > 0: # O(log(N))
    out.append(arr[a])
    a = (a // 1.7)
out.merge_sort() # merge_sort() = O(N∗logN), out = log(N), -> out.merge_sort() = O(log(N)∗log(log(N)))

# Складываем последовательные алгоритмы
# O(1) + O(1) + O(log(N)) + O(log(N)∗log(log(N)))
# Согласно правилам вычисления выбираю доминирующий оператор, это  O(log(N)∗log(log(N)))


# Сложность по пространственным затратам
a = len(arr) - 1  # O(1)
out = list()  # O(1)
while a > 0: # O(log(N))
    out.append(arr[a])
    a = (a // 1.7)
out.merge_sort() # merge_sort() = O(n), out = O(log(N)), -> out.merge_sort() = O(log(N))

# Складываем последовательные алгоритмы
# O(1) + O(1) + O(log(N)) + O(log(N))
# Согласно правилам вычисления получаю O(log(N))