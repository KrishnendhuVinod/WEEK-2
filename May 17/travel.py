from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from dotenv import load_dotenv
import os

# Load Gemini API key
load_dotenv()


llm_config = {
    "config_list": [
        {
            "model": "gemini-1.5-flash",
            "api_key": os.getenv("GEMINI_API_KEY"),
            "api_type": "google"
        }
    ]
}

# Planner agent
planner = AssistantAgent(
    name="Planner",
    system_message="You are a helpful planner who creates travel plans based on user requests. Ask the Researcher for information as needed.",
    llm_config=llm_config,
)

# Researcher agent
researcher = AssistantAgent(
    name="Researcher",
    system_message="You are a researcher who provides detailed information about travel destinations.",
    llm_config=llm_config,
)

# User proxy agent
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="ALWAYS",
    code_execution_config=False,
)

# Group chat and manager
groupchat = GroupChat(agents=[user_proxy, planner, researcher], messages=[], max_round=3)
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)
# Start chat
try:
    user_proxy.initiate_chat(
        manager,
        message="I want to plan a 3-day trip to Paris. Can you help?",
    )
except Exception as e:
    print(f"Error during chat: {e}")
