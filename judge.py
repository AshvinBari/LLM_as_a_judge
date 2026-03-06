from openai import OpenAI
from config import OPENAI_API_KEY
from prompts import JUDGE_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def evaluate_answer(question, answer, context):

    prompt = JUDGE_PROMPT.format(
        question=question,
        answer=answer,
        context=context
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content