import os
from pathlib import Path
from dotenv import load_dotenv 
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Error")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

def llm_ans(prompt):
    message={
        "role" : "user",
        "content" : prompt
    }
    messages = [message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_prompt = """
This is a user complaint:
My laptop is not working 
Classify this 
"""

# # I would classify this complaint as a:

# **Technical Issue/Computer Hardware Problem**

# More specifically, it falls under the category of:

# * **Device Malfunction**: The user's laptop is not functioning properly.
# * **General Complaint**: The complaint is brief and lacks specific details about the issue, making it a general complaint about the laptop not working.

good_prompt = """
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of three categories namely billing, technical, return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word shoud be one of the categories given in constraints
#Example
For instance if a user compalin says he wants a refund then the category is Return
#FALLBACK
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
My laptop is crazy
"""


print(llm_ans(good_prompt))