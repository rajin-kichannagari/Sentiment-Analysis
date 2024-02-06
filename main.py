import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from transformers import pipeline
#Libraries for the web app
import pandas as pd
import streamlit as st
from streamlit.components.v1 import html


nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):


    # Removes special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

    return ' '.join(filtered_words)

def analyze_sentiment(text):
    sentiment_analyzer = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
    preprocessed_text = preprocess_text(text)
    result = sentiment_analyzer(preprocessed_text)
    label = result[0]['label']
    score = result[0]['score']
    return label, score

def emoji(label):
    if label == "POS":
        return "😃"
    elif label == "NEG":
        return "😔"
    else:
        return "😐"
    
def display_emoji(emoji):
    st.markdown(f'<span style="font-size: 50px;">{emoji}</span>', unsafe_allow_html=True)

def display_label(label):
    if label == "POS":
        return "Positive"
    elif label == "NEG":
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Welcome to the Sentiment Analyzer App!")

    st.header('Sentiment Analysis')
    with st.expander('Analyze Text'):
        text = st.text_input('Text here: ')
        if text:
            sentiment_label, sentiment_score = analyze_sentiment(text)
            larbel = display_label(sentiment_label)
            display_emoji(emoji(sentiment_label))
            st.write(f"Sentiment Score: {sentiment_score * 100:.2f}% {larbel}")
            

if __name__ == "__main__":
    main()
