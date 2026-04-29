from llm import llm

def planner(state):
    prompt = f"""
You are an expert software planner.

Break this problem into clear step-by-step plan:

Problem:
{state['input']}
"""

    state["plan"] = llm(prompt)
    return state
