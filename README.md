# GPT-Researcher Readme

## Overview

GPT-Researcher is a chatbot powered by GPT (Generative Pre-trained Transformer) that utilizes Google Search results to generate answers to your questions. This README provides you with detailed instructions on how to set up and run the project.

## Prerequisites

Before setting up the project, make sure you have the following:

- An OpenAI API key, which you can obtain [here](https://platform.openai.com/account/api-keys).
- A Google API key, available [here](https://console.cloud.google.com/apis/credentials).
- A Google Custom Search Engine (CSE) ID, which you can create [here](https://programmablesearchengine.google.com/controlpanel/create).
- Pinecone credentials, which can be obtained from [Pinecone](https://app.pinecone.io/).

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-repo-url.git
   cd gpt-researcher

## Installation

2. Install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project and add the following credentials:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CSE_ID=your_google_cse_id_here
PINECONE_ENVIRONMENT=your_pinecone_environment_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX=your_pinecone_index_here
```


## Running the Project
To run the GPT-Researcher chatbot, follow these steps:

In the root directory of the project, execute the following command:

```bash
streamlit run main.py
```
Once the application is running, open a web browser and navigate to the provided URL (typically http://localhost:8501).

You can now interact with the GPT-Researcher chatbot by entering your questions or queries. The chatbot will use Google Search results to provide answers and information.

## Usage
GPT-Researcher is designed to assist you in finding information from the web quickly and efficiently. Simply type your questions or queries into the chat interface, and the chatbot will generate responses based on the Google Search results it retrieves.

## Disclaimer
Please note that GPT-Researcher relies on external services and APIs, including Google Search and Pinecone. Be aware of any usage limits and terms of service associated with these services. Additionally, keep your API keys and credentials secure to protect your data and resources.




