import boto3

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')

    # 1. Extract review from event
    review = event.get('review', '')

    if not review:
        print("No review provided.")
        return {
            "status": "error",
            "message": "No review found in event"
        }

    print(f"Review: {review}")

    # 2. Analyze sentiment
    response = comprehend.detect_sentiment(
        Text=review,
        LanguageCode='en'
    )

    sentiment = response['Sentiment']
    scores = response['SentimentScore']

    # 3. Log results
    print(f"Sentiment: {sentiment}")
    print(f"Scores: {scores}")

    return {
        "review": review,
        "sentiment": sentiment,
        "scores": scores
    }
