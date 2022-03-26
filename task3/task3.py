import solve3

# Дан массив пассажиров people[] где каждый элемент является весом каждого пассажира
# limit - максимальный вес, который может выдержать лодка, также в лодке может находиться максимум 2 пассажира
# В ответ вывести минимальное кол-во лодок для перевозки всех пассажиров, или если это невозможно то вывести ошибку
# Пример вывода: 2 boats: (1,3),(2)
# Нельзя менять ничего в данной программе

people = [1, 2]
limit = 3

print(solve3.numboats(people, limit))

people = [3, 2, 2, 1]
limit = 3

print(solve3.numboats(people, limit))

people = [3, 5, 3, 4]
limit = 3

print(solve3.numboats(people, limit))

people = [3, 5, 3, 4]
limit = 5

print(solve3.numboats(people, limit))
