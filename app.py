import requests
import streamlit as st

def call_chatbot_api(query):
    #url = 'https://binqiangliu-flask-inference-api.hf.space/api/chat'
    url = 'https://ishare-langchainsummarizationchainflaskapi.hf.space/api/chat'
    json_data_for_api = {'user_question': query}
    response = requests.post(url, json=json_data_for_api) 
    result = response.json()
    return result['response']
    
user_query = st.text_input("Enter your query here:")
with st.spinner("AI Thinking...Please wait a while to Cheers!"):    
    if user_query !="" and not user_query.strip().isspace() and not user_query == "" and not user_query.strip() == "" and not user_query.isspace():
        response = call_chatbot_api(user_query)
        st.write("AI Response:")
        st.write(response)
        print(response)  # 打印Chatbot的响应