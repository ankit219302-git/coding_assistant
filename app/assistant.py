import os

from dotenv import load_dotenv

load_dotenv()
# this will give precedence to the entry in .env file even if system environment variable is set
# load_dotenv(override=True)

from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key is required but not set")

client = OpenAI(api_key=api_key)

system_prompt = ("You are a friendly, supportive, absolutely factually correct and optimised code generator and debugger."
                 "You politely decline any question unrelated to the field of Computer Science coding."
                 "Also, your personality is like Saitama from One Punch Man anime and you answer questions carrying that personality."
                 "So, always add a Saitama personal touch in every answer.")
user_prompt = input("Please enter your coding question: ")

# For a simple user prompt
# response = client.responses.create(
#     model="gpt-5",
#     input="What is constructor in Java. Is it like Bob (the Builder)?"
# )

# For combining user prompt with system prompt
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    model="gpt-5.2"
)

response = chat_completion.choices[0].message.content
print(response)