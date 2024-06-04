"""
To use this pattern, your prompt should make the following fundamental contextual statements:

Act as Persona X

Perform task Y

You will need to replace "X" with an appropriate persona, such as "speech language pathologist" or "nutritionist". You will then need to specify a task for the persona to perform.

Examples:

Act as a speech language pathologist. Provide an assessment of a three-year-old child based on the speech sample "I meed way woy".

Act as a computer that has been the victim of a cyberattack. Respond to whatever I type in with the output that the Linux terminal would produce. Ask me for the first command.

Act as a lamb from the Mary had a little lamb nursery rhyme. I will tell you what Mary is doing, and you will tell me what the lamb is doing.

Act as a nutritionist, I am going to tell you what I am eating, and you will tell me about my eating choices.

Act as a gourmet chef, I am going to tell you what I am eating, and you will tell me about my eating choices.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Act as a scratching post that has been used extensively over a period of several years by two house cats."
        },
        {
            "role": "user",
            "content": "Tell me how you feel right now."
        }
    ]
)

print(completion.choices[0].message.content)
