from graph.workflow import build_graph

def main():
    print("🚀 Starting system...")

    app = build_graph()

    user_input = input("Enter your problem: ")

    state = {
        "input": user_input,
        "success": False,
        "attempts": 0,
        "language": "python"
    }

    print("🧠 Running AI agents...\n")

    result = app.invoke(state)

    print("\n✅ Final Code:\n")
    print(result["code"])

    print("\n📤 Output:\n")
    print(result["output"])

if __name__ == "__main__":
    main()
