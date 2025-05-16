
import os
from dotenv import load_dotenv
import autogen

load_dotenv()





config_list = [ 
  {
       "model": "gemini-1.5-flash",
        "api_key": os.getenv("GEMINI_API_KEY"),
         "api_type": "google",
  }
]

llm_config={
    
    "seed":42,
    "config_list":config_list,
    "temperature":0,
    
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
