import random

#rules
    #words must start with a consonant
    #consonants must be followed by a vowel
    #vowels must be followed by a consonant

vowels = [
    "a",
    "э",
    "e",
    "и",
    "o",
    "y",
]
consonants = [
    "б",
    "д",
    "ф",
    "г",
    "ж",
    "к",
    "л",
    "м",
    "н",
    "п",
    "р",
    "c",
    "т",
    "x",
    "ц",
    "ч",
    "ш",
    "ю",
    "я"
]

chars = vowels + consonants

length = random.randint(3, 10)

word = consonants[random.randint(0, len(consonants)-1)]

for i in range(length):
    if word[i] in consonants:
        word += vowels[random.randint(0, len(vowels)-1)]
    elif word[i] in vowels:
        word += consonants[random.randint(0, len(consonants)-1)]
    else:
        print("ERROR: Illegal value")
        break

print(word)
