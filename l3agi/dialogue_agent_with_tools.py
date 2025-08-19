# l3agi/dialogue_agent_with_tools.py

from xagent_integration.xagent_wrapper import XAgentWrapper


class DialogueAgentWithTools:
    def __init__(self):
        self.agent = XAgentWrapper()

    def respond(self, message: str) -> str:
        """
        Generate a response using XAgentWrapper.
        """
        try:
            return self.agent.run(message)
        except Exception as e:
            return f"[DialogueAgent Error: {str(e)}]"
