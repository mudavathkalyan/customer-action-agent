from openai import OpenAI

client = OpenAI(
    api_key="sk-7c3a279bed78aa796b6878d42ebdbe9d4d9da08bce13b225452acae68e76db82",
    base_url="http://localhost:4000"
)

response = client.chat.completions.create(
    model="model1",
    messages=[
        {
            "role": "user",
            "content": "Explain what a customer support ticket is in one sentence."
        }
    ]
)

print("Model:", response.model)
print("Response:", response.choices[0].message.content)
print("Usage:", response.usage)