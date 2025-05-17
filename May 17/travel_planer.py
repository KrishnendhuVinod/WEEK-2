import asyncio
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from dotenv import load_dotenv
import os

# Load environment variables (Gemini API key)
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

# Define agents
planner = AssistantAgent(
    name="Planner",
    system_message="You are a helpful planner who creates travel plans based on user requests. Ask the Researcher for information as needed.",
    llm_config=llm_config,
)

researcher = AssistantAgent(
    name="Researcher",
    system_message="You are a researcher who provides detailed information about travel destinations.",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",  # Auto reply instead of manual input
    code_execution_config=False,
)

# Define the group chat and manager
groupchat = GroupChat(
    agents=[user_proxy, planner, researcher],
    messages=[],
    max_round=5,
)
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Async function for running the chat
async def main():
    await asyncio.sleep(1)  # simulate delay before starting
    response = user_proxy.initiate_chat(
        manager,
        message="I want to plan a 3-day trip to Paris. Can you help?",
    )
    await asyncio.sleep(1)  # simulate delay after the chat
    print("\n--- Chat finished ---")

# Run using asyncio
if __name__ == "__main__":
    asyncio.run(main())
