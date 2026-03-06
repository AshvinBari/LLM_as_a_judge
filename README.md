# LLM Judge + RAG System

This project implements a Retrieval-Augmented Generation (RAG) system with an AI judge to evaluate answers.

## Setup

1.  **Clone/Open the repository.**
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Environment Variables**:
    Ensure you have a `.env` file in the root directory with the following keys:
    ```env
    OPENAI_API_KEY=your_openai_key
    TAVILY_API_KEY=your_tavily_key
    ```

## How to Run

### 1. Start the Backend (FastAPI)
In your terminal, run:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`. You can view the API documentation at `http://localhost:8000/docs`.

### 2. Start the Frontend (Streamlit)
In a **new** terminal, run:
```bash
streamlit run dashboard/app.py
```
The dashboard will open in your browser at `http://localhost:8501`.

## Project Structure
- `app/`: Contains the FastAPI application and RAG logic.
- `dashboard/`: Contains the Streamlit frontend.
- `config/`: Configuration and environment loading.
- `evaluation/`: Prompts and logic for the AI judge.
