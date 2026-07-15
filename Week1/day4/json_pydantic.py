import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Structuring it reason for structuring this was the ouput before structuring
# I can extract the personal information from the ticket for you. Here it is:

# * Name: Harshit
# * Address: Gwalior
# * Phone Number: 2947492
# * Email: abc@fuckyou

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
schema = Ticket.model_json_schema()

response_format = {
    "type":"json_object"
}

system_prompt = f"""
Extract the personal information from the ticketstrictly based on this schema and give me a JSON output.
{schema}
"""

message_system = {
    "role":"system",
    "content":system_prompt
}
load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Error")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
role = "user"
text = "Hello mu name is Harshit, i purchased iPhone which is not working at all. My address is Gwalior. My phone no is 2947492 . my email is abc@fuckyou"

# kisi variable ko jab aap string me kr rhe hote toh yeh f aur triple inverted comma
prompt = f"""
This is a customer ticket.Please extract the personal information from that ticket 
{text}
"""
message = {
    "role":role,
    "content":prompt
}
messages=[message_system,message]
response = client.chat.completions.create(model=model, messages=messages,response_format=response_format)
# print(response)

print('###########################################################################################')
answer=response.choices[0].message.content
print(answer)


# Isko padte kese h 
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

# isko pass krte h 
print(ticket.name)
print(ticket.email)
print(ticket.issue)

#Homework

# take resume in pdf or word
# have hr give you a list of things like skill, experience, projects
# extract these from resume
# match against the hr list
# generate a percentage of matching or not