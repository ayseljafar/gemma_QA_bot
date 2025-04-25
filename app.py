import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os
from huggingface_hub import login
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check for Hugging Face token
if 'HF_TOKEN' not in os.environ:
    st.error("Please set your Hugging Face token in .env file")
    st.stop()

# Login to Hugging Face
login(token=os.environ['HF_TOKEN'])

# Set page config
st.set_page_config(
    page_title="Q&A Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Create header
st.title("🤖 Q&A Chatbot")
st.markdown("Ask me anything! I'm powered by Google's Gemma 2B model.")

# Initialize the model
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="google/gemma-2b-it",
        torch_dtype=torch.float16,
        device_map="auto"
    )

# Load the model
chatbot = load_model()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("What's your question?"):
    # Format the prompt for Gemma
    formatted_prompt = f"<start_of_turn>user\n{prompt}<end_of_turn>\n<start_of_turn>assistant"
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Generate response
        with st.spinner("Thinking..."):
            response = chatbot(
                formatted_prompt,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.7,
                top_p=0.95,
                repetition_penalty=1.1
            )
            assistant_response = response[0]['generated_text'].split("assistant")[-1].strip()
            
            # Display and save assistant response
            message_placeholder.markdown(assistant_response)
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Add a sidebar with information
with st.sidebar:
    st.title("About")
    st.markdown("""
    This is a Q&A chatbot powered by Google's Gemma 2B model.
    
    Features:
    - Persistent chat history
    - Markdown support
    - Responsive UI
    
    Note: Responses are generated using AI and may not always be accurate.
    """)
    
    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun() 