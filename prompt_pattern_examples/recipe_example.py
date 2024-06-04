"""
To use this pattern, your prompt should make the following fundamental contextual statements:

I would like to achieve X

I know that I need to perform steps A,B,C

Provide a complete sequence of steps for me

Fill in any missing steps

(Optional) Identify any unnecessary steps

You will need to replace "X" with an appropriate task. You will then need to specify the steps A, B, C that you know
will need to be part of the recipe / complete plan.

Examples:

I would like to purchase a house. I know that I need to perform steps to make an offer and close on the house.
Provide a complete sequence of steps for me. Fill in any missing steps.

I would like to drive to NYC from Nashville. I know that I want to go through Asheville, NC on the way and that I don't
want to drive more than 300 miles per day. Provide a complete sequence of steps for me. Fill in any missing steps.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "I would like to purchase a house. I know that I need to perform steps to make an offer and \
            close on the house. Provide a complete sequence of steps for me. Fill in any missing steps. Also warn me \
            of any common missteps or pitfalls that home buyers typically make."
        },
    ]
)

print(completion.choices[0].message.content)
