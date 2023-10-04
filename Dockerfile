FROM python:3.8.12-buster

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main main

COPY dataframe/absolute_final_df.csv dataframe/absolute_final_df.csv

CMD uvicorn main.main:app --host 0.0.0.0 --port 8080 --reload
