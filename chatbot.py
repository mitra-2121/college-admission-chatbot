import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

# Load FAQ data
faq_df = pd.read_csv("data/faq.csv")

# Text cleaning function
#stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


# Clean questions
faq_df["clean_question"] = faq_df["question"].apply(clean_text)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(faq_df["clean_question"])

# Function to get chatbot response
def get_response(user_input):
    user_input = clean_text(user_input)
    user_vector = vectorizer.transform([user_input])

    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]
    
    print("Similarity score:", best_score)

    if best_score < 0.4:
        return "Sorry, I can help only with college admission–related questions."


    return faq_df.iloc[best_match_index]["answer"]

# Manual testing
if __name__ == "__main__":
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            break
        print("Bot:", get_response(user_query))
