import openai
import variable
import os
def chatgpt():
    os.environ["OPENAI_API_KEY"] = variable.api_Key
    # 设置API密钥
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": variable.answer},
            {"role": "user", "content": variable.cache}
        ]
    )
    variable.text=response.choices[0].message.content
    #print(response.choices[0].message.content)