# LLM Judge + Tavily RAG

This project implements a Retrieval-Augmented Generation (RAG) system using Tavily Search, OpenAI, and a Streamlit dashboard.

## Setup

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Environment Variables**:
    Ensure you have a `.env` file in the root directory with:
    ```env
    OPENAI_API_KEY=your_openai_key
    TAVILY_API_KEY=your_tavily_key
    ```

## How to Run

1.  **Start the Application**:
    ```bash
    streamlit run app.py
    ```
2.  **Access the Dashboard**:
    Open your browser at `http://localhost:8501`.

## Project Structure
- `app.py`: Main entry point (Streamlit UI + RAG logic).
- `judge.py`: Logic for AI evaluation.
- `prompts.py`: Prompt templates.
- `tavily_search.py`: Web search integration.
- `config.py`: Environment configuration.
