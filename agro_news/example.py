import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv("./agro-news/.env")

API_KEY = os.getenv("GOOGLE_API_KEY")
PROMPT = os.getenv("PROMPT")
genai.configure(api_key=API_KEY)


for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

# models/gemini-1.0-pro
# models/gemini-1.0-pro-001
# models/gemini-1.0-pro-latest
# models/gemini-1.0-pro-vision-latest
# models/gemini-1.5-pro-latest
# models/gemini-pro
# models/gemini-pro-vision

model = genai.GenerativeModel("gemini-1.0-pro")

NEWS = [
    "Milho se apoia no dólar e sobe até 1,8% na B3 nesta segunda-feira",
    "Exportação de milho avança menos de 500 toneladas na semana e representa apenas 6% de abril/23",
    "USDA informa venda de milho para o México nesta 2ª feira (15)",
    "Segunda-feira começa com milho subindo na Bolsa Brasileira",
    "Milho/Cepea: Com novas quedas, Indicador volta a fechar abaixo dos R$ 60/sc",
    "Dólar ajuda milho fechar 6ªfeira em alta na B3, mas não evita desvalorização semanal",
    "Safras & Mercado eleva estimativas para produção de soja e milho do Brasil",
    "Preços futuros do milho abrem a sexta-feira em alta na B3 e em Chicago",
    "Milho: Cotação futura finaliza a sessão desta 4ª feira com ganhos na CBOT",
    "Novo leilão de frete de milho ocorrerá na quinta-feira (11)",
    "Ucrânia enviará 600 mil t de milho à China em abril e 400 mil t em maio, dizem corretores",
    "Preços futuros do milho trabalham com leves altas nesta 4ª feira em Chicago",
]

responses = []
for headline in NEWS:
    response = model.generate_content(
        f"{PROMPT}: {headline}",
    )
    if response.text.startswith("```") and response.text.endswith("```"):
        response_dict = eval(response.text[3:-3])
    else:
        response_dict = eval(response.text)
    response_dict["headline"] = headline
    responses.append(response_dict)


# {"classification": "POSITIVE", "score": 0.671}
# {"classification": "NEGATIVE", "score": -0.412}
# {"classification": "POSITIVE", "score": 0.654}
# {"classification": "POSITIVE", "score": 0.891}
# {"classification": "NEGATIVE", "score": 0.8}
# {"classification": "POSITIVE", "score": 0.56}
# {"classification": "POSITIVE", "score": 0.891}
# {"classification": "POSITIVE", "score": 0.767}
# {"classification": "POSITIVE", "score": 0.78}
# {"classification": "NEUTRAL", "score": 0}
# {"classification": "POSITIVE", "score": 0.678}
# {"classification": "NEUTRAL", "score": 0.0}
