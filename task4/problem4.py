import solve4

# 1st function shows which message is longer
# 2nd function shows which message has more vowels in it
# 3rd function shows how many consonants are more than vowels in a message
# 4th function shows number of spaces in the text
# 5th function searches for complete and incomplete matches with wordtarget in the text and displays their in 2 lines
# for example wordtarget = "apple" in text1="applejuice is made of apple",
# then -> complete matches: (22,26); incomplete matches: (0,4)
# you may assume that there is only one solution for the function 5
# You can thange this code if you want functions to work with something else, maybe a list of vowels and consonants

message1 = "big"
message2 = "small"

text1 = "The hitman committed a series of murders, ending his job on the murder of a local rich man"
wordtarget = "murder"

print(solve4.longermessage(message1, message2))
print(solve4.vowelsscontains(message1, message2))
print(solve4.consonantscontains(message1, message2))
print(solve4.findspaces(text1))
print(solve4.findwords(text1, wordtarget))
