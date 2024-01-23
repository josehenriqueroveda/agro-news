import os

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")


analyzer = SentimentIntensityAnalyzer()

text = (
    "Média diária de exportação de milho em janeiro/24 segue superior a de janeiro/23"
)


def sentiment_analyzer(text):
    polarity = analyzer.polarity_scores(text)
    if polarity["compound"] > 0.25:
        return "positive", polarity["compound"]
    elif polarity["compound"] < -0.25:
        return "negative", polarity["compound"]
    else:
        return "neutral", polarity["compound"]


print(
    f"{text}\nSentiment: {sentiment_analyzer(text)[0]} | Score: {sentiment_analyzer(text)[1]}"
)
