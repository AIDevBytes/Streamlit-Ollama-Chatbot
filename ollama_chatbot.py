import streamlit as st
from helpers.llm_helper import chat, stream_parser
from config import Config
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Streamlit OpenAI Chatbot",
    initial_sidebar_state="expanded"
)

st.title("Streamlit OpenAI Chatbot")

# sets up sidebar nav widgets
with st.sidebar:   
    st.markdown("# Chat Options")
    # widget - https://docs.streamlit.io/library/api-reference/widgets/st.selectbox

    # models - https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
    model = st.selectbox('What model would you like to use?',('gpt-3.5-turbo', 'gpt-4'))
    
    # https://docs.streamlit.io/library/api-reference/widgets/st.number_input
    temperature = st.number_input('Temperature', value=0.7, min_value=0.1, max_value=1.0, step=0.1,
                                            help="The temperature setting to be used when generating output from the model.")
    
    max_token_length = st.number_input('Max Token Length', value=1000, min_value=200, max_value=1000, step=100, 
                                            help="Maximum number of tokens to be used when generating output.")
    
# checks for existing messages in session state
# https://docs.streamlit.io/library/api-reference/session-state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from session state
# https://docs.streamlit.io/library/api-reference/chat/st.chat_message
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("What questions do you have about the document?"):
    # Display user prompt in chat message container
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # adds user's prompt to session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner('Generating response...'):
        # retrieves response from OpenAI
        llm_response = chat(user_prompt, model=model, max_tokens=max_token_length,
                            temp=temperature)

        # streams the response back to the screen
        stream_output = st.write_stream(stream_parser(llm_response))

        # appends response to the message list
        st.session_state.messages.append({"role": "assistant", "content": stream_output})

    last_response =  st.session_state.messages[len(st.session_state.messages)-1]['content']

    # Display assistant response in chat message container
    if str(last_response) != str(stream_output):
        with st.chat_message("assistant"):
            st.markdown(stream_output)
        