JUDGE_PROMPT = """
You are an AI judge.

Question:
{question}

Context:
{context}

Answer:
{answer}

Score the answer:

1. correctness
2. relevance
3. hallucination
4. completeness

Return a short evaluation.
"""