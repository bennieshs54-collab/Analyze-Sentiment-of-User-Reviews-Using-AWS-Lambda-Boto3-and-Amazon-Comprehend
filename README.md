# AWS Sentiment Analysis using Lambda & Comprehend

## Objective
Analyze user reviews and detect sentiment automatically.

## Services Used
- AWS Lambda
- Amazon Comprehend
- CloudWatch Logs

## Workflow
1. Lambda receives review input
2. Sends text to Amazon Comprehend
3. Comprehend returns sentiment:
   - POSITIVE
   - NEGATIVE
   - NEUTRAL
   - MIXED
4. Results logged in CloudWatch

## Example Input
{
  "review": "This product is amazing!"
}

## Example Output
Sentiment: POSITIVE
Scores: {
  Positive: 0.99,
  Negative: 0.01
}
