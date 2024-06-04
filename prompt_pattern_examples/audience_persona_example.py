"""
To use this pattern, your prompt should make the following fundamental contextual statements:

Explain X to me.

Assume that I am Persona Y.

You will need to replace "Y" with an appropriate persona, such as "have limited background in computer science" or
"a healthcare expert". You will then need to specify the topic X that should be explained.

Examples:

Explain large language models to me. Assume that I am a bird.

Explain how the supply chains for US grocery stores work to me. Assume that I am Ghengis Khan.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Explain what a neural network is. Assume that I have no background in computer science or math."
        },
    ]
)

print(completion.choices[0].message.content)
