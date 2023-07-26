from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity (-1 to 1) and subjectivity (0 to 1)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity

    # Determine the sentiment label
    if sentiment_polarity > 0:
        sentiment_label = "positive"
    elif sentiment_polarity < 0:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"

    return sentiment_label, sentiment_polarity, sentiment_subjectivity

def main():
    print("Welcome to Sentiment Analysis Program!")
    text = input("Enter a sentence or a piece of text: ")
    
    sentiment_label, sentiment_polarity, sentiment_subjectivity = analyze_sentiment(text)
    
    print("\nSentiment Analysis Results:")
    print(f"Sentiment: {sentiment_label}")
    print(f"Polarity: {sentiment_polarity:.2f}")
    print(f"Subjectivity: {sentiment_subjectivity:.2f}")

if __name__ == "__main__":
    main()