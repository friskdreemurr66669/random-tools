import conlang_word_list
import has_what
import random_word_gen
import wordorder

print("language name:")
cln : str = random_word_gen.gen_word(random_word_gen.set_length(3, 50)) + "лaнagyx" #conlang name
cln = cln.replace(cln[0], cln[0].upper())
print("\t" + cln)

print("language has:")
print(f"\tparticles: {has_what.particle}")
print(f"\tarticles: {has_what.article}")
print(f"\ttenses: {has_what.tense}")
print(f"\ttones: {has_what.tones}")
print(f"\tgender specific words: {has_what.gender_specific}")

print()



print("word order:")
print(f"\tbasic word order: {wordorder.basic_wordorder}")



print()

print("words:")
conlang_word_list.gen_word()
print("countries:")
conlang_word_list.gen_country()