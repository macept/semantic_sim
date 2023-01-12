import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

# List of movie descriptions
movies = [
    {"title": "Movie A", "description": "When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first."},
    {"title": "Movie B", "description": "After the death of Superman, several new people present themselves as possible successors."},
    {"title": "Movie C", "description": "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up."},
    {"title": "Movie D", "description": "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson."},
    {"title": "Movie E", "description": "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed."},
    {"title": "Movie F", "description": "In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from."},
    {"title": "Movie G", "description": "The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes."},
    {"title": "Movie H", "description": "A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral."},
    {"title": "Movie I", "description": "Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow."},
    {"title": "Movie J", "description": "Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."}
]

def recommend_movie(description):
    # Process the input description
    input_doc = nlp(description)

    # Compare the input description to each movie description
    similarities = []
    for movie in movies:
        movie_doc = nlp(movie["description"])
        similarity = input_doc.similarity(movie_doc)
        similarities.append({"title": movie["title"], "similarity": similarity})

    # Sort the movies by similarity and return the title of the most similar
    similarities = sorted(similarities, key=lambda x: x["similarity"], reverse=True)
    return similarities[0]["title"]

# Test the function
input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(recommend_movie(input_description))

input_description_two = "A young German fights in World War 1 and tells the story of how he dressed up in the uniform of the enemy to evade capture"
print(recommend_movie(input_description_two))
