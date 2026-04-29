from execution.executor import run_code
from llm import llm
from memory.memory_store import store_memory, retrieve_memory
import time
import re

def extract_code(text):
    match = re.search(r"```(\w+)?(.*?)```", text, re.DOTALL)
    if match:
        return match.group(2).strip()
    return text.strip()


def debugger(state):
    attempts = state.get("attempts", 0)
    language = state.get("language", "python")

    success, output = run_code(state["code"], language)

    if success:
        state["success"] = True
        state["output"] = output
        return state

    if attempts >= 2:
        state["success"] = True
        state["output"] = "❌ Failed after retries"
        return state

    print(f"⚠️ Debug attempt {attempts + 1}")

    # 🔥 retrieve past fixes
    memory_context = retrieve_memory(output)

    fix_prompt = f"""
Fix this {language} code.

Previous fixes (if relevant):
{memory_context}

Rules:
- Return only code
- No explanation
- No input()

Code:
{state['code']}

Error:
{output}
"""

    time.sleep(2)

    fixed_code = extract_code(llm(fix_prompt))

    store_memory(output, fixed_code)

    state["code"] = fixed_code
    state["attempts"] = attempts + 1
    state["success"] = False

    return state
