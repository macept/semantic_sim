import spacy

# Comment out example to try something else with copy and paste
"""nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
"""
# It is interesting than the highest score in the above code is between word 1 and 2, which are both animals.

nlp = spacy.load('en_core_web_md')
word1 = nlp("lemon")
word2 = nlp("lime")
word3 = nlp("yellow")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# It is interesting to note that despite lemons being yellow, the similarity of the two words is only half
# of that of lemon and lime, which are very commonly said together. 

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]

# It is interesting to note the response with the most semantic similarity appears to be the one
# that could most reasonably be said by a human as a response to the input prompt

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Having run the example file using the small and medium language models, I have noted that when using the 
# small model, there's much less similarity recorded than when using the medium language model,
# the scores are lower. I also receive a warning from the module that I am using the simplified version
# and therefore vectors are not being used and this may impair accuracy.
