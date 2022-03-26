def numboats(people, limit):
    sorted(people)
    boats = []
    index = []
    for i in range(len(people)):
        index.append(i)
    for i in index:
        if people[i] > limit:
            return None
        elif people[i] == limit:
            boats.append(people[i])
            continue
        flag = True
        for j in index:
            if j > i:  # j = i + 1
                if people[i] + people[j] <= limit:
                    boats.append([people[i], people[j]])
                    index.pop(j)
                    flag = False
                    break
        if flag:
            boats.append(people[i])

    result = str(len(boats)) + ' boats: ' + str(boats)

    return result
