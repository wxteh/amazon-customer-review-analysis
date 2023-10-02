from fastapi import FastAPI
from fastapi.responses import JSONResponse

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import random
from googletrans import Translator, constants
from langdetect import detect


app = FastAPI()

def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, src="auto", dest="en")
    return translated.text

def translate_if_not_en(text):
    try:
        if detect(text) != "en":
            translated_text = translate_text(text)
            return translated_text
    except Exception as e:
        print(e)
        print(text)
        return text

tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
bert_model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")


@app.get("/")
def index():
    return {"title": "Hello Arthur"}


@app.get("/predict")
def predict(product_category, text):
    translated_text = translate_text(text)
    tokens = tokenizer.encode(translated_text, return_tensors="pt")
    result = bert_model(tokens)
    score = int(torch.argmax(result.logits))+1
    #return int(torch.argmax(result.logits))+1

    df = pd.read_csv("../dataframe/summary_keywords_df.csv")

    if score < 4:
        if 5 in df["sentiment"].values:
            message = f"It looks like you are not too happy with this product. Try taking a look at these products under {product_category}:"
            data = df[(df["product_category"] == product_category) & (df["sentiment"] == 5)].drop(columns=["product_category", "keywords", "sentiment"])
            if data is None or data.empty:
                data = "No products found matching your criteria."
        else:
            message = f"It looks like you are not too happy with this product. Try taking a look at these products under {product_category}:"
            data = df[(df["product_category"] == product_category) & (df["sentiment"] == 4)].drop(columns=["product_category", "keywords", "sentiment"])
            if data is None or data.empty:
                data = "No products found matching your criteria."
    elif score == 4:
        message = f"Thank you for your feedback. Here are some other products with better reviews under {product_category}:"
        data = df[(df["product_category"] == product_category) & (df["sentiment"] == 5)].drop(columns=["product_category", "keywords", "sentiment"])
        if data is None or data.empty:
            data = "No products found matching your criteria."
    else:
        message = "Great choice!"
        data = None

    response_data = {"message": message, "data": data}

    return response_data
