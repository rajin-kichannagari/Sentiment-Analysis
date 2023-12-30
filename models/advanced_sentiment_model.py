from transformers import pipeline
from utils.text_preprocessing import preprocess_text

def analyze_sentiment(text):
    sentiment_analyzer = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
    preprocessed_text = preprocess_text(text)
    result = sentiment_analyzer(preprocessed_text)
    label = result[0]['label']
    score = result[0]['score']
    return label, score
