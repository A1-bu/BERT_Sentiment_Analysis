import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

# st.write("Hello World!")
# st.write("Hello Streamlit!")

# """Merged BERT Emotions"""
emotions = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval',
            'disgust', 'embarassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief',
            'remorse', 'sadness', 'surprise', 'neutral']

# Emotions
fan_emotions = pd.read_csv("Merged_Emotions.csv")

for ind in fan_emotions.index:
    fan_emotions["Prediction_1"][ind] = emotions[fan_emotions["Prediction_1"][ind]]
    fan_emotions["Prediction_2"][ind] = emotions[fan_emotions["Prediction_2"][ind]]

fan_emotions = fan_emotions[['Match','text', 'Prediction_1', 'Prediction_2']]

# Merged BERT Hate Speech
hate_speech = ['neutral', 'positive', 'hateful']

# Hate Speech
fan_speech = pd.read_csv("Merged_Hate_Speech.csv")

for ind in fan_speech.index:
    fan_speech["Prediction_1"][ind] = hate_speech[fan_speech["Prediction_1"][ind]]
    fan_speech["Prediction_2"][ind] = hate_speech[fan_speech["Prediction_2"][ind]]

fan_speech = fan_speech[['Match','text', 'Prediction_1', 'Prediction_2']]
# fan_speech.head()

# Streamlit columns
col1, col2 = st.columns([3,3])

# Plot Emotions
with col1:
    st.write("""### Predicted Emotions of Fans During Different Matches """)
    wc = fan_emotions[fan_emotions['Match'] == 'FIFA World Cup 2022'][['Match', 'Prediction_1']]
    euros = fan_emotions[fan_emotions['Match'] == 'UEFA European Championship 2024'][['Match', 'Prediction_1']]
    prem = fan_emotions[fan_emotions['Match'] == 'Premier League 2024'][['Match', 'Prediction_1']]
    cl = fan_emotions[fan_emotions['Match'] == 'Champions League 2024'][['Match', 'Prediction_1']]
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.set_figheight(18)
    fig.set_figwidth(19)
    fig.suptitle("Predicted Emotions of Fans During Different Matches", x=0.5, y=0.92)

    wc["Prediction_1"].value_counts(True).plot(ax = ax1, kind="bar", title="Argentina Vs France")
    euros["Prediction_1"].value_counts(True).plot(ax = ax2, kind="bar", title="Spain Vs England")
    prem["Prediction_1"].value_counts(True).plot(ax = ax3, kind="bar", title="Manchester City Vs Tottenham")
    cl["Prediction_1"].value_counts(True).plot(ax = ax4, kind="bar", title="Liverpool Vs Real Madrid")

    st.pyplot(fig)

# Plot Hate Speech 
with col2:
    st.write("""### Predicted Speech of Fans During Different Matches """)
    wc_hs = fan_speech[fan_speech['Match'] == 'FIFA World Cup 2022'][['Match', 'Prediction_1']]
    euros_hs = fan_speech[fan_speech['Match'] == 'UEFA European Championship 2024'][['Match', 'Prediction_1']]
    prem_hs = fan_speech[fan_speech['Match'] == 'Premier League 2024'][['Match', 'Prediction_1']]
    cl_hs = fan_speech[fan_speech['Match'] == 'Champions League 2024'][['Match', 'Prediction_1']]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.set_figheight(18)
    fig.set_figwidth(19)
    fig.suptitle("Predicted Speech of Fans During Different Matches", x=0.5, y=0.92)

    wc_hs["Prediction_1"].value_counts(True).plot(ax = ax1, kind="bar", title="Argentina Vs France")
    euros_hs["Prediction_1"].value_counts(True).plot(ax = ax2, kind="bar", title="Spain Vs England")
    prem_hs["Prediction_1"].value_counts(True).plot(ax = ax3, kind="bar", title="Manchester City Vs Tottenham")
    cl_hs["Prediction_1"].value_counts(True).plot(ax = ax4, kind="bar", title="Liverpool Vs Real Madrid")

    st.pyplot(fig)

