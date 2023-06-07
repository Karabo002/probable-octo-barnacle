
import spacy

def get_most_similar_movie(description):
    nlp = spacy.load("en_core_web_sm")
    movies = []
    with open("movies.txt", "r") as file:
        movies = file.readlines()
    
    similarity_scores = []
    for movie in movies:
        movie = movie.strip()
        doc1 = nlp(movie)
        doc2 = nlp(description)
        similarity_scores.append(doc1.similarity(doc2))

    most_similar_movie = movies[similarity_scores.index(max(similarity_scores))]
    return most_similar_movie.strip()

if __name__ == "__main__":
    description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    most_similar_movie = get_most_similar_movie(description)
    print("Next movie recommendation:", most_similar_movie)


