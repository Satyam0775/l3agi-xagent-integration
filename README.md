# 🚀 L3AGI + XAgent Integration

This project integrates **OpenBMB’s XAgent** into the **L3AGI Framework**, replacing the existing **LangChain ReAct Agent**.  
The integration ensures L3AGI can now leverage the more advanced and modular XAgent framework for **multi-agent collaboration**.

---

## 📌 Objective

- 🔹 Remove the existing **LangChain ReAct agent**  
- 🔹 Integrate **XAgent** into the L3AGI framework  
- 🔹 Ensure seamless **conversational flow** and **tool usage**  
- 🔹 Provide **documentation + working demo** for evaluation  

---

## 📂 Project Structure

l3agi-xagent-integration/
│── l3agi/ # Core L3AGI framework (with XAgent integrated)
│ ├── conversational.py # Conversation flow (modified)
│ ├── dialogue_agent_with_tools.py# Dialogue Agent using XAgent (modified)
│ ├── test.py # Test runner
│

│── xagent_integration/ # Wrapper for XAgent
│ ├── init.py
│ ├── utils.py
│ ├── xagent_wrapper.py
│

│── docs/screenshots/ # Screenshots of working run
│── requirements.txt # Python dependencies
│── report.md # Detailed report of integration
│── README.md # This file

