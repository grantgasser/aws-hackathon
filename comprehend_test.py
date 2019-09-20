## Harry Potter Group
## Comprehend

import boto3
import json

text = "I don't know how I feel about Severus Snape, \
        he's OK but sometimes he's a really tough professor"

comprehend = boto3.client(service_name='comprehend', region_name='region')

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')
