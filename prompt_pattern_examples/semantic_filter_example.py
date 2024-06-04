"""
To use this pattern, your prompt should make the following fundamental contextual statements:

Filter this information to remove X

You will need to replace "X" with an appropriate definition of what you want to remove, such as. "names and dates" or
"costs greater than $100".

Examples:

Filter this information to remove any personally identifying information or information that could potentially be used
to re-identify the person.

Filter this email to remove redundant information.
"""
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": ""
        },
    ]
)

print(completion.choices[0].message.content)
