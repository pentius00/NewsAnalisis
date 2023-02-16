import pandas as pd
from pathlib import Path
import plotly 
import streamlit as st
import plotly.express as px
import os
import pandas as pd
from newsapi import NewsApiClient
from dotenv import load_dotenv
load_dotenv("key.env")
import json
from pandas.io.json import json_normalize
load_dotenv('secret.env')


import ibm_watson
#from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


################ Getting the news#############################################################################
def get_news(topic):
    load_dotenv("key.env")
    api_key = os.getenv("NEWS_API_KEY")
    newsapi = NewsApiClient(api_key=api_key)
    headlines = newsapi.get_everything(q='topic', language="en", sort_by="relevancy")
    news_df = pd.DataFrame.from_dict(headlines["articles"])
    news_df = news_df.drop(['source', 'url', 'urlToImage'], axis=1)
    text = news_df.description
    text = text.to_json(path_or_buf=None,
                  orient=None, date_format=None,
                  double_precision=10, force_ascii=True, date_unit='ms',
                  default_handler=None, lines=False, compression='infer', index=True,
                  indent=None, storage_options=None)
    
   
    return news_df


#############################analising the news using IBM watson ##############################################
#def news_analysis(df):
#    tone_api = os.getenv("tone_key")
#    tone_url = os.getenv("tone_url")
#    authenticator = IAMAuthenticator(tone_api)
#    text = df.description
#    text = text.to_json(path_or_buf=None,
#                  orient=None, date_format=None,
#                  double_precision=10, force_ascii=True, date_unit='ms',
#                  default_handler=None, lines=False, compression='infer', index=True,
#                  indent=None, storage_options=None)
#    tone_analyzer = ToneAnalyzerV3(version="2021-09-21",authenticator=authenticator)
#    tone_analyzer.set_service_url(tone_url)
#    tone_analysis = tone_analyzer.tone(
#    {"text": text},
#    content_type="application/json",
#    content_language="en",
#    accept_language="en",).get_result()
#    sentences_tone_df = json_normalize(
#    data=tone_analysis["sentences_tone"],
#    record_path=["tones"],
#    meta=["sentence_id", "text"])
#    sentences_tone_df['title'] = df['title']
#    sentences_tone_df['content'] = df['content']
#    return sentences_tone_df
   

################# Display dataframe#########################################################################


def ai_news_analysis(news_df):
    load_dotenv("key.env")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key = OPENAI_API_KEY
    completion = openai.Completion()
    prompt = "Summary of the news: " + news_df['description'].str.cat(sep=', ')
    openai_url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + OPENAI_API_KEY}
    payload = {
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1024}
    
    response = requests.post(openai_url, headers=headers, json=payload)

# Step 4: Extract the relevant information from the response
    response_dict = response.json()
    if "choices" in response_dict:
        analysis = response_dict["choices"][0]["text"]
    else:
        analysis = "Error: Could not extract analysis from response."

    print(analysis)

##################chatGP3 Analysis##########################################################################
st.title('News Analysis Using AI')

topic = st.selectbox('Select news topic', ['Sports',
"Politics and government","Technology",
"Civil rights / civil liberties",	
"Local stories / USA",
"Social issues (abortion, gay marriage, etc.)",
"Current events",
"Arts and culture",
"Science",
"Entertainment and celebrities", "world events"])



st.write('You selected:', topic)


print(topic)
st.button('retrive data')

if st.button:
    df = get_news(topic)
    st.dataframe(df)
    
if st.button:
    news_df = ai_news_analysis(df)
    st.dataframe(news_df)