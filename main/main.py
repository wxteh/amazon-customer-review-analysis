from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

import random
app = FastAPI()


#from wherever import loadmodel()
# app.state.model = load_model(


@app.get("/")
def index():
    return {"title": "Hello Arthur"}


@app.get("/predict")
def predict(product_category, review):
    tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    tokens = tokenizer.encode(review, return_tensors="pt")
    result = model(tokens)
    score = int(torch.argmax(result.logits))+1
    #return int(torch.argmax(result.logits))+1

    df = pd.read_csv("../dataframe/summary_keywords_df.csv")

    if score < 4:
        if 5 in df['sentiment'].values:
            print(f'It looks like you are not too happy with this product. Try taking a look at these products under {product_category}:')
            return df[(df['product_category'] == product_category) & (df['sentiment'] == 5)].drop(columns=['product_category','keywords','sentiment'])
        else:
            print(f'It looks like you are not too happy with this product. Try taking a look at these products under {product_category}:')
            return df[(df['product_category'] == product_category) & (df['sentiment'] == 4)].drop(columns=['product_category','keywords','sentiment'])
    elif score == 4:
            print(f'Thank you for your feedback. Here are some other products with better reviews under {product_category}:')
            return df[(df['product_category'] == product_category) & (df['sentiment'] == 5)].drop(columns=['product_category','keywords','sentiment'])
    else:
        print('Great choice!')
