import openai
from timestamps.settings import OPENAI_API_KEY
def generate_completion(prompt):
    api_key =  OPENAI_API_KEY
    client = openai.OpenAI(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0]
    return response.message.content