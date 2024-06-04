"""
To use this pattern, your prompt should make the following fundamental contextual statements:

Ask me for input X

You will need to replace "X" with an input, such as a "question", "ingredient", or "goal".

Examples:

From now on, I am going to cut/paste email chains into our conversation. You will summarize what each person's points
are in the email chain. You will provide your summary as a series of sequential bullet points. At the end, list any open
questions or action items directly addressed to me. My name is Jill Smith.
Ask me for the first email chain.

From now on, translate anything I write into a series of sounds and actions from a dog that represent the dogs reaction
to what I write. Ask me for the first thing to translate.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "From now on, for every prompt I give you, write a few alternative approaches that would produce \
            better output then compare and contrast the pros and cons of each approach.",
        },
        {
            "role": "user",
            "content": "Ask me for the first input"
        }
    ]
)

print(completion.choices[0].message.content)
