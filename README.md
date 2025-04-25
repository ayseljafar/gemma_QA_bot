# Gemma Chatbot

A streamlit-based chatbot powered by Google's Gemma 2B model. This chatbot can answer questions and engage in conversations using state-of-the-art AI technology.

## Features

- 🤖 Powered by Google's Gemma 2B instruction-tuned model
- 💬 Interactive chat interface
- 🔄 Persistent chat history
- 📝 Markdown support
- 🎨 Clean and responsive UI
- 🧹 Clear chat functionality

## Prerequisites

- Python 3.8 or higher
- A Hugging Face account and access token
- Accepted license terms for the Gemma model

## Setup

1. Clone the repository:
```bash
git clone [<repository-url>](https://github.com/ayseljafar/gemma_QA_bot)
cd chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up your Hugging Face token:
   - Go to https://huggingface.co/settings/tokens
   - Create a new access token
   - Create a `.env` file in the project root
   - Add your token: `HF_TOKEN=your_token_here`

5. Accept the Gemma model license:
   - Visit https://huggingface.co/google/gemma-2b-it
   - Click "Accept license and access repository"

## Running the App

Start the application with:
```bash
streamlit run app.py
```

The app will be available at http://localhost:8501

## Usage

1. Type your question in the chat input
2. Wait for the model to generate a response
3. Use the "Clear Chat" button in the sidebar to start a new conversation

## Model Information

This chatbot uses the Gemma 2B instruction-tuned model, which is:
- Smaller and faster than the 7B version
- Optimized for instruction-following
- Suitable for running on consumer hardware
- Developed by Google

## Requirements

See `requirements.txt` for a full list of dependencies:
- streamlit==1.32.2
- transformers==4.38.2
- torch==2.2.1
- accelerate==0.27.2
- bitsandbytes==0.42.0
- python-dotenv==1.1.0
- sentencepiece==0.2.0

## License

This project uses the Gemma model which is subject to Google's model license. Make sure to review and comply with the license terms at https://huggingface.co/google/gemma-2b-it/blob/main/LICENSE.

## Troubleshooting

If you encounter issues:
1. Ensure your Hugging Face token is correctly set in the `.env` file
2. Verify you've accepted the Gemma model license
3. Check that all dependencies are correctly installed
4. Make sure you have enough disk space for the model 
