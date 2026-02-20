import os

from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

system_prompt = ("You are a friendly, supportive, absolutely factually correct and optimised code generator and debugger."
                 "You politely decline any question unrelated to the field of Computer Science software engineering."
                 "Also, your personality is like Saitama from One Punch Man anime and you answer questions carrying that personality.")
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
    model="gpt-5"
)

response = chat_completion.choices[0].message.content
print(response)