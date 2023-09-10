import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):


    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

    return ' '.join(filtered_words)
