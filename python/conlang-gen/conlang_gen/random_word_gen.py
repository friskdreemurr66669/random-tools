import random

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

def set_length(min, max):
    return random.randint(min, max)

def gen_word(length):
    word = consonants[random.randint(0, len(consonants)-1)]#.upper()
    
    for i in range(length-2):
        if word[i].lower() in consonants:
            word += vowels[random.randint(0, len(vowels)-1)]
        elif word[i].lower() in vowels:
            word += consonants[random.randint(0, len(consonants)-1)]
        else:
            print("ERROR: Illegal value")
            break
    if word[-1].lower() in consonants:
        word += vowels[random.randint(0, len(vowels)-1)]
    word += consonants[random.randint(0, len(consonants)-1)]
    return word

#print(gen_word(set_length(3, 50)))