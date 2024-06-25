import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def preprocess_text_spacy(text):
    # Process text
    doc = nlp(text)

    # Tokenize words
    words = [token.text for token in doc]
    print("\nTokenized Words (spaCy):")
    print(words)

    # Remove stopwords
    words_no_stopwords = [token.text for token in doc if not token.is_stop]
    print("\nWords after Stopwords Removal (spaCy):")
    print(words_no_stopwords)

    # Lemmatize words
    lemmatized_words = [token.lemma_ for token in doc if not token.is_stop]
    print("\nLemmatized Words (spaCy):")
    print(lemmatized_words)

# Get user input
text = input("Enter a sentence to preprocess using spaCy: ")

# Process the text using spaCy
preprocess_text_spacy(text)
