from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

import random
app = FastAPI()


#from wherever import loadmodel()
# app.state.model = load_model(


@app.get("/")
def index():
    return {"title": "Hello Arthur"}


@app.get("/predict")
def predict(review):
    tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    tokens = tokenizer.encode(review, return_tensors="pt")
    result = model(tokens)
    return int(torch.argmax(result.logits))+1
