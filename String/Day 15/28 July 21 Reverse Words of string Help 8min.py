# 28 July 08:03PM-08:11PM
        # Logic 3min
        # Coding 5min

# Reverse words in a given String in Python
# Difficulty Level : Easy
# Last Updated : 23 Nov, 2020
# We are given a string and we need to reverse words of a given string?

# Examples:

# Input : str = geeks quiz practice code
# Output : str = code practice quiz geeks

# ---------Logic 1----------

# s="This is my Day"
# l=[]
# for i in s:
#     l.append(i)
# print(l)

# ----Does not Work it will print by Words---

# ---------Logic 2----------

s="This is my Day"
word=s.split(' ')
print(word)
new_s=' '.join(reversed(word))
print(new_s)
