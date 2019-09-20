## Harry Potter Group
## Comprehend

import boto3
import json

text = "I don't know how I feel about Severus Snape, \
        he's OK but sometimes he's a really tough professor"

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

print('Calling DetectSentiment')
json_response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
print(type(json_response))
print(json_response['SentimentScore'])
print('End of DetectSentiment\n')
