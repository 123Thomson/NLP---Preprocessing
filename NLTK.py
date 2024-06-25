import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text_nltk(text):
    # Tokenize words
    words = word_tokenize(text)
    print("\nTokenized Words (NLTK):")
    print(words)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words_no_stopwords = [word for word in words if word.lower() not in stop_words]
    print("\nWords after Stopwords Removal (NLTK):")
    print(words_no_stopwords)

    # Stem words
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words_no_stopwords]
    print("\nStemmed Words (NLTK):")
    print(stemmed_words)

    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words_no_stopwords]
    print("\nLemmatized Words (NLTK):")
    print(lemmatized_words)

# Get user input
text = input("Enter a sentence to preprocess using NLTK: ")

# Process the text using NLTK
preprocess_text_nltk(text)
