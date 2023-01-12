import spacy
"""nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
"""
# It is interesting than the highest score is between word 1 and 2, which are both animals.

nlp = spacy.load('en_core_web_md')
word1 = nlp("lemon")
word2 = nlp("lime")
word3 = nlp("yellow")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

