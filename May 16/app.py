
import os
from dotenv import load_dotenv
import autogen


config_list = [ 
  {
        "model": "openai/gpt-3.5-turbo",  # or try "mistralai/mixtral-8x7b"
        "api_key": os.getenv("OPENROUTER_API_KEY"),
        "base_url": "https://openrouter.ai/api/v1",  }
]

llm_config={
    
    "seed":42,
    "config_list":config_list,
    "temperature":0
}



assistant=autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
    
)

user_proxy=autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir":"web","use_docker": False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
    Otherwise, reply CONTINUE , or the reson why the task is not solved yet."""
)

task="""
Write a python code to output numbers 1 to 100 , and store the code in a file """
user_proxy.initiate_chat(assistant, message=task)
