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
role = "user"

# 3 prompts 
prompt1 = "Hi !"
prompt2 = "Explain Time Travel In detail"
prompt3 = "Write an essay of 100 words on Machine Learning"

prompts = [prompt1,prompt2,prompt3]
for prompt in prompts:
    message = {
    "role":role,
    "content":prompt
    }

    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    usage=response.usage
    print(f"Prompt:{prompt}-->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}")


# prompt = "Do you know Padho with pratyush"
# message = {
#     "role":role,
#     "content":prompt
# }
# messages=[message]
