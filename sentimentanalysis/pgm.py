import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


import streamlit as st # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('data\sentiment_analysis_results.csv')
    return df

df = load_data()

# Title and description
st.title('Technology News Sentiment Analysis Dashboard')
st.write('An interactive dashboard to visualize sentiment analysis of scraped technology news articles.')

# Data overview
st.subheader('Data Overview')
st.dataframe(df.head())

# Sentiment distribution visualization
st.subheader('Sentiment Distribution')
sentiment_counts = df['sentiment'].value_counts()
fig, ax = plt.subplots()
ax.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'red', 'gray'])
ax.set_xlabel('Sentiment')
ax.set_ylabel('Number of Articles')
ax.set_title('Distribution of Sentiments')
st.pyplot(fig)

# Filter articles by sentiment
st.subheader('Filter Articles by Sentiment')
sentiment_options = df['sentiment'].unique()
selected_sentiment = st.selectbox('Choose Sentiment', sentiment_options)
filtered_df = df[df['sentiment'] == selected_sentiment]
st.dataframe(filtered_df[['Title', 'Description']])
