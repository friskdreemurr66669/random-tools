import numpy
import has_what

basic_wordorder = [
    "subject",
    "verb",
    "object"
]
possess = [
    "possession",
    "possessed"
]
auxiliary = [
    "verb",
    "auxiliary"
]
article = []

numpy.random.shuffle(basic_wordorder)
numpy.random.shuffle(possess)
numpy.random.shuffle(auxiliary)

if has_what.article:
    article = [
        "article",
        "noun"
    ]
    numpy.random.shuffle(article)