# l3agi/conversational.py

from l3agi.dialogue_agent_with_tools import DialogueAgentWithTools

def run_conversation():
    """
    Run a simple conversation loop with XAgentWrapper (or fallback HuggingFace model).
    """
    agent = DialogueAgentWithTools()

    print("🤖 XAgent Conversation Started! (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["exit", "quit"]:
            print("👋 Conversation ended.")
            break

        response = agent.respond(user_input)
        print("XAgent:", response)
