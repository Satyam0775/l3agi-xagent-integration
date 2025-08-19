🚀 L3AGI + XAgent Integration

This project integrates OpenBMB’s XAgent into the L3AGI Framework, replacing the existing LangChain ReAct Agent.
The integration ensures L3AGI can now leverage the more advanced and modular XAgent framework for multi-agent collaboration.

📌 Objective

Remove the existing LangChain ReAct agent.

Integrate XAgent into the L3AGI framework.

Ensure seamless conversational flow and tool usage.

Provide documentation + working demo for evaluation.

📂 Project Structure
l3agi-xagent-integration/
│── l3agi/                        # Core L3AGI framework (with XAgent integrated)
│   ├── conversational.py         # Conversation flow (modified)
│   ├── dialogue_agent_with_tools.py # Dialogue Agent using XAgent (modified)
│   ├── test.py                   # Test runner
│── xagent_integration/           # Wrapper for XAgent
│   ├── __init__.py
│   ├── utils.py
│   ├── xagent_wrapper.py
│── docs/screenshots/             # Screenshots of working run
│── requirements.txt              # Python dependencies
│── report.md                     # Detailed report of integration
│── README.md                     # This file

⚙️ Installation

Clone this repository:

git clone https://github.com/Satyam0775/l3agi-xagent-integration.git
cd l3agi-xagent-integration


Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On Linux/Mac


Install dependencies:

pip install -r requirements.txt

▶️ Running the Test

To verify the integration:

python -m l3agi.test


Example Run:

🤖 XAgent Conversation Started! (type 'exit' to quit)

You: hello
XAgent: hello ... [model-generated response]

🖼️ Screenshot

📝 Deliverables

✅ Modified L3AGI framework with XAgent integrated

✅ requirements.txt with updated dependencies

✅ report.md with detailed process, challenges, and testing

✅ Working screenshot included

👨‍💻 Author

Satyam Kumar
