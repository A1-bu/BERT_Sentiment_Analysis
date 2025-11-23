import tensorflow as tf
import pandas as pd
from transformers import BertTokenizer, TFBertForSequenceClassification

# Enable numpy behavior for tensorflow
tf.experimental.numpy.experimental_enable_numpy_behavior()

# tokenizer = BertTokenizer.from_pretrained("monologg/koelectra-base-v3-hate-speech")
# model = TFBertForSequenceClassification.from_pretrained("monologg/koelectra-base-v3-hate-speech", from_pt = True)

tokenizer = BertTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-original")
model = TFBertForSequenceClassification.from_pretrained("monologg/bert-base-cased-goemotions-original", from_pt = True)

# csv paths
# Change csv file to encoding: utf-8 
input_csv_path = "CL_final.csv"
output_csv_path = "Bert_emotes_CL_final.csv"

input_data = pd.read_csv(input_csv_path, encoding='utf-8')

# List to store predictions
prediction_1 = []
prediction_2 = []
count = 0

# Iterate reddit comments
for text in input_data['text']:
    inputs = tokenizer([str (text)], return_tensors="tf", max_length=512, truncation= True)
    
    outputs = model(**inputs)
    logits = outputs.logits

    # 1st pred
    pred1 = tf.argmax(logits, axis=1).numpy()[0]
    prediction_1.append(pred1)
    
    # 2nd pred
    pred2 = tf.argsort(logits, axis=1, direction='DESCENDING').numpy()[0, 1]
    prediction_2.append(pred2)

    # Visual check
    count = count+1
    if (count % 100 == 0):
        print(count)

# Add Hate prediction to df
input_data['Prediction_1'] = prediction_1
input_data['Prediction_2'] = prediction_2

# Save to csv
input_data.to_csv(output_csv_path, index=False)
print("CSV created")

