from sentiment_analyzer import SentimentAnalyzer


news = [
    "Guerra comercial entre EUA e China pode piorar o mercado de soja",
    "Fertilizantes estão mais caros e isso será ruim para produtores de grãos",
    "Agrishow tem a melhor perspectiva de negócios dos últimos anos",
    "Produção de etanol de milho pode servir de alternativa para produtores",
]

sa = SentimentAnalyzer(task="sentiment", lang="pt")

print("##### Sentiment Analysis #####")
for item in news:
    print(item)
    print(sa.analyze(item))
    print("---------------------------------")


# Output:
# ##### Sentiment Analysis #####
# Guerra comercial entre EUA e China pode piorar o mercado de soja
# AnalyzerOutput(output=NEU, probas={NEU: 0.616, NEG: 0.369, POS: 0.015})
# ---------------------------------
# Fertilizantes estão mais caros e isso será ruim para produtores de grãos
# AnalyzerOutput(output=NEG, probas={NEG: 0.506, NEU: 0.487, POS: 0.007})
# ---------------------------------
# Agrishow tem a melhor perspectiva de negócios dos últimos anos
# AnalyzerOutput(output=POS, probas={POS: 0.948, NEU: 0.047, NEG: 0.005})
# ---------------------------------
# Produção de etanol de milho pode servir de alternativa para produtores
# AnalyzerOutput(output=NEU, probas={NEU: 0.945, POS: 0.036, NEG: 0.020})
# ---------------------------------
