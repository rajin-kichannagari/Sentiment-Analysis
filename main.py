from models.advanced_sentiment_model import analyze_sentiment

def main():
    print("Welcome to Social Media Sentiment Analyzer!")
    with open("data/sample_tweets.txt", "r") as file:
        tweets = file.readlines()

    for i, tweet in enumerate(tweets):
        sentiment_label, sentiment_score = analyze_sentiment(tweet)
        print(f"Tweet {i + 1} Sentiment: {sentiment_label}")
        print(f"Confidence Score: {sentiment_score:.4f}")
        print()

if __name__ == "__main__":
    main()
