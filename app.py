import requests
import streamlit as st
import json

st.set_page_config(page_title="Webpage Summarization AI Assistant - Open Source Version", layout="wide")
st.subheader("Webpage Summarization AI Assistant - Open Source Version")
st.write('Important notice: This webpage summarization AI Assistant is offered ONLY for the purpose of assisting users to read legal website page contents and by no means for any other use. Any user should never interact with the AI Assistant in any way that is against any related promulgated regulations. The user is the only entity responsible for interactions taken between the user and the AI Assistant.')

css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def call_chatbot_api(target_url):
    #url = 'https://binqiangliu-flask-inference-api.hf.space/api/chat'
    url = 'https://ishare-langchainsummarizationchainflaskapi.hf.space/api/chat'
    json_data_for_api = {'target_url': target_url}
    #response = requests.post(url, json=json_data_for_api)
    #response = requests.post(url, headers=headers, data=json.dumps(json_data_for_api))   #This format needs 'import json', or else NameError: name 'json' is not defined
    response = requests.post(url, data=json.dumps(json_data_for_api))   #This format needs 'import json', or else NameError: name 'json' is not defined
   
    result = response.json()
    return result['response']
    
target_url = st.text_input("Enter the URL of the webpage your want to summarize:")
with st.spinner("AI Thinking...Please wait a while to Cheers!"):    
    if target_url !="" and not target_url.strip().isspace() and not target_url == "" and not target_url.strip() == "" and not target_url.isspace():
        response = call_chatbot_api(target_url)
        st.write("AI Response:")
        st.write(response)
        print(response)  # 打印Chatbot的响应
