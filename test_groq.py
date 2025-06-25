from groq import Groq

# Your actual Groq API key
client = Groq(api_key="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")

# Ask your question to the AI
response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "user", "content": "Hello! Can you help me with APK modding and coding?"}
    ]
)

# Print the AI's response
print(response.choices[1].message.content)
