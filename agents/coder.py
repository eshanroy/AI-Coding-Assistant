from llm import llm
from rag.retriever import retrieve_context
import re

def detect_language(text):
    text = text.lower()

    if "java" in text:
        return "java"
    else:
        return "python"


def extract_code(text):
    match = re.search(r"```(\w+)?(.*?)```", text, re.DOTALL)
    if match:
        return match.group(2).strip()
    return text.strip()


def coder(state):
    language = detect_language(state["input"])

    context = retrieve_context(state["input"])

    prompt = f"""
You are an expert {language} programmer.

Use this context if helpful:
{context}

Write ONLY code.

Rules:
- No explanation
- No markdown
- No input()
- Use fixed values
- Code must run directly

IMPORTANT for Java:
- Use class name Main
- Include public static void main

Problem:
{state['input']}
"""

    response = llm(prompt)

    code = extract_code(response)

    state["code"] = code
    state["language"] = language

    return state
