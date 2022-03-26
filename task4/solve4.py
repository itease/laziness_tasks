def longermessage(message1, message2):
    return max(message1, message2)


def vowelsscontains(message1, message2):
    vowels_lower = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_upper = ['A', 'E', 'I', 'O', 'U', 'Y']
    vowels_all = vowels_lower + vowels_upper
    vowels1 = 0
    vowels2 = 0
    for letter in message1:
        if letter in vowels_all:
            vowels1 += 1
    for letter in message2:
        if letter in vowels_all:
            vowels2 += 1
    return message1 if vowels1 > vowels2 else message2
    # return message1 if message1.count(vowels_all) > message2.count(vowels_all) else message2


def consonantscontains(message1):
    vowels_lower = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_upper = ['A', 'E', 'I', 'O', 'U', 'Y']
    vowels_all = vowels_lower + vowels_upper
    vowels = 0
    for letter in message1:
        if letter in vowels_all:
            vowels += 1
    return len(message1) - vowels


def findspaces(text1):
    return text1.count(' ')


def findwords(text1, wordtarget):
    start = 0
    complete = ''
    incomplete = ''
    for i in range(findspaces(text1) + 1):
        word = ''
        for j in range(start, len(text1)):
            if text1[j] != ' ':
                word += text1[j]
            else:
                if wordtarget == word:
                    complete = 'complete matches: ' + 'from ' + str(start) + ' to ' + str(j - 1)
                elif wordtarget in word:
                    if text1 in [start, len(wordtarget) + start - 1] == wordtarget:
                        begin = str(start)
                        finish = str(len(wordtarget) + start - 1)
                    else:
                        begin = str(j - len(wordtarget))
                        finish = str(j - 1)
                    incomplete = 'incomplete matches: ' + 'from ' + begin + ' to ' + finish
                start = j + 1
                break
    answer = complete + '\n' + incomplete
    return answer
