# 27 July 06:37AM-06:57AM Completed by SELF 20min

# Write a Python function that takes a list of words and return the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


# ------My Code--------

s="highest this is the jdifbhjvrvjkfdb peak fsm efnkfkwjf"
l=s.split()
print(l)
s=0
d=''
for i in range(len(l)):
    # print(l[i])
    for j in range(len(l)):
        # print(l[j])
        if(len(l[i])>len(l[j])):
            q=len(l[i])
            if(q>s):
                s=q
                d=l[i]
print(d,s)

# -----Solution From Website-------


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

        