from fastapi import FastAPI
app = FastAPI()




file_path = "../raw_data/reviews_cleaned.csv"
df = pd.read_csv(file_path)


#Instantiate model
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

#encode and calculate sentiment
# function to to get a review and pass through the model
def sentiment_score(review):
    tokens = tokenizer.encode(review, return_tensors="pt")
    result = model(tokens)
    return int(torch.argmax(result.logits))+1


# Split the DataFrame into batches of 512 rows
batch_size = 512
num_batches = len(df) // batch_size + 1

# Initialize an empty list to store sentiment scores
sentiment_scores = []

# Iterate through the batches
for i in range(num_batches):
    start_idx = i * batch_size
    end_idx = (i + 1) * batch_size
    batch_reviews = df["review_content"].iloc[start_idx:end_idx]

    # Iterate through the rows within the batch
    for j, review in enumerate(batch_reviews):
        # Check if the review is NaN or None
        if pd.notna(review):
            sentiment = sentiment_score(review[:512])
            sentiment_scores.append(sentiment)

            # Calculate the row number
            row_number = i * batch_size + j + 1

            # Print the progress
            print(f"Row {row_number} in Batch {i + 1} is done")

# Add the sentiment scores to the DataFrame
df["Sentiment"] = sentiment_scores
