# xagent_integration/xagent_wrapper.py

try:
    from XAgent.agent import XAgent
    from XAgent.llms import HuggingFaceLLM
    _HAS_XAGENT = True
except Exception as e:
    print("⚠️ Warning: Could not fully load OpenBMB XAgent:", e)
    _HAS_XAGENT = False

from transformers import pipeline


class XAgentWrapper:
    def __init__(self):
        if _HAS_XAGENT:
            try:
                # Safer initialization with a small HuggingFace model
                self.llm = HuggingFaceLLM(model_name="distilgpt2")
                self.agent = XAgent(llm=self.llm)
                print("✅ Running with OpenBMB XAgent + distilgpt2")
            except Exception as e:
                print("⚠️ Fallback: Using transformers pipeline due to XAgent error:", e)
                self.agent = pipeline("text-generation", model="distilgpt2")
        else:
            print("⚠️ XAgent not available, using transformers fallback.")
            self.agent = pipeline("text-generation", model="distilgpt2")

    def run(self, prompt: str, tools: dict = None) -> str:
        """
        Run the agent with a given prompt.
        """
        try:
            if _HAS_XAGENT:
                return self.agent.run(prompt)
            else:
                return self.agent(prompt, max_new_tokens=50)[0]["generated_text"]
        except Exception as e:
            return f"[XAgentWrapper Error: {str(e)}]"
